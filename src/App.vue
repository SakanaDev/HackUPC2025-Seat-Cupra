<script>
import CarOutside from './components/CarOutside.vue';
import CarInside from './components/CarInside.vue';
import VideoPro from './components/VideoPro.vue';

export default {
  data() {
    return {
      isOutside: true,
      showContent: false,
      inputUser: '',
      messages: [],
      isLoading: false,
      chatbotFlag: false,
    }
  },
  components: {
    CarOutside,
    CarInside,
    VideoPro,
  },
  methods: {
    handleVideoEnd() {
      this.showContent = true;
    },
    handlePartClick(part) {
      console.log(`Parte clickeada: ${part}`);
      alert(`Has seleccionado: ${part}`);
    },
    async hacerPreguntas() {
    if (!this.inputUser.trim()) return;

    this.messages.push({
      text: this.inputUser,
      sender: 'user',
      timestamp: new Date().toLocaleTimeString()
    });

    const pregunta = this.inputUser;
    this.inputUser = '';
    this.isLoading = true;

    // Agregar mensaje de carga
    this.messages.push({
      text: '...',
      sender: 'bot',
      isLoading: true,
      timestamp: new Date().toLocaleTimeString()
    });

    // Esperar al siguiente tick del DOM para renderizar el mensaje "is typing..."
    await this.$nextTick();

    try {
      const response = await fetch('http://localhost:5000/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: pregunta })
      });

      const data = await response.json();

      this.messages.pop();
      this.messages.push({
        text: data.response,
        sender: 'bot',
        timestamp: new Date().toLocaleTimeString()
      });

    } catch (error) {
      console.error('Error:', error);
      this.messages.pop();
      this.messages.push({
        text: 'Sorry, there was an error processing your request.',
        sender: 'bot',
        timestamp: new Date().toLocaleTimeString()
      });
    } finally {
      this.isLoading = false;
      this.$nextTick(() => {
        this.scrollToBottom();
      });
    }
  },
    scrollToBottom() {
      const chatContainer = this.$refs.chatContainer;
      if (chatContainer) {
        chatContainer.scrollTop = chatContainer.scrollHeight;
      }
    }
  },
  mounted() {
    // Mensaje de bienvenida inicial
    this.messages.push({
      text: 'Hello! I\'m your CUPRA assistant. How can I help you today?',
      sender: 'bot',
      timestamp: new Date().toLocaleTimeString()
    });
  }
}
</script>

<template>
  <VideoPro v-if="!showContent" @video-ended="handleVideoEnd" />

  <div v-if="showContent" class="main-content">
    <header>
      <a href="">
        <img src="https://www.cupraofficial.es/etc.clientlibs/cupra-website/components/clientlibs/resources/icons/logos/logo-cupra.svg" alt="">
      </a>

      <div class="header-button">
        <button class="header-btn" @click="chatbotFlag=!chatbotFlag">Help</button>
        <button class="header-btn">Drive it</button>
      </div>
    </header>
    
    <!-- Chat container -->
    <div class="chat-container" ref="chatContainer" v-if="chatbotFlag">
      <div class="chat-messages">
        <div v-for="(message, index) in messages" :key="index" 
             :class="['message', message.sender]">
          <div class="message-content">
            <div v-if="!message.isLoading" class="message-text">{{ message.text }}</div>
            <div v-else class="message-text loading">
              <span class="typing-indicator">
                <span class="dot"></span>
                <span class="dot"></span>
                <span class="dot"></span>
              </span>
            </div>
            <div class="message-time">{{ message.timestamp }}</div>
          </div>
        </div>
      </div>
      
      <div class="chat-input-container">
        <input 
          v-model="inputUser" 
          placeholder="Ask me anything about your CUPRA..."
          @keyup.enter="hacerPreguntas"
          :disabled="isLoading"
        >
        <button @click="hacerPreguntas" :disabled="isLoading || !inputUser.trim()">
          <span v-if="!isLoading">Send</span>
          <span v-else class="sending"></span>
        </button>
      </div>
    </div>

    <div class="car-container">
      <CarOutside v-if="isOutside" :key="'outside'"/>
      <CarInside v-if="!isOutside" :key="'inside'"/>
    </div>
    
    <div class="view-selector">
      <button @click="isOutside=true" :class="{ active: isOutside }">
        <img src="./assets/car-icon.png" alt="Exterior">
      </button>
      <button @click="isOutside=false" :class="{ active: !isOutside }">
        <img src="./assets/seat-icon.png" alt="Interior">
      </button>
    </div>
  </div>
</template>

<style scoped>
/* Base Styles */
header {
  position: relative;
  background-color: #000;
  padding: 0 16px;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 1000;
}

.header-btn {
  background: #000;
  border: none;
  color: #fff;
  padding: 10px 16px;
  border-radius: 20px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.header-btn:hover {
  color: #000;
  background-color: rgba(255, 255, 255, 0.5);
}

/* Car Container */
.car-container {
  position: relative;
  height: calc(100vh - 60px);
  width: 100vw;
}

/* View Selector */
.view-selector {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 15px;
  background: rgba(0, 0, 0, 0.7);
  padding: 8px;
  border-radius: 50px;
  z-index: 100;
}

.view-selector button {
  background: #000;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 0;
}

.view-selector button img {
  width: 20px;
  height: 20px;
  filter: invert(1);
}

.view-selector button.active {
  background: #fff;
}

.view-selector button.active img {
  filter: invert(0);
}

/* Chat Container */
.chat-container {
  font-family: 'CupraRegular', sans-serif;
  position: fixed;
  top: 80px;
  right: 20px;
  width: 350px;
  height: 530px;
  background-color: rgba(0, 0, 0, 0.5);
  border: 1px solid #ff5e00;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(255, 94, 0, 0.3);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  z-index: 1000;
}

.chat-messages {
  flex: 1;
  padding: 15px;
  overflow-y: auto;
  background-color: rgba(0, 0, 0, 0.5);
}

/* Messages */
.message {
  margin-bottom: 15px;
  display: flex;
}

.message.user {
  justify-content: flex-end;
}

.message.bot {
  justify-content: flex-start;
}

.message-content {
  max-width: 80%;
  padding: 12px 15px;
  border-radius: 18px;
  position: relative;
  font-size: 14px;
  line-height: 1.4;
}

.user .message-content {
  background: linear-gradient(135deg, #ff5e00, #ff8c00);
  color: #fff;
  border-bottom-right-radius: 5px;
}

.bot .message-content {
  background: #1a1a1a;
  color: #e6e6e6;
  border: 1px solid #333;
  border-bottom-left-radius: 5px;
}

.message-text {
  word-wrap: break-word;
}

.message-time {
  font-size: 11px;
  opacity: 0.7;
  text-align: right;
  margin-top: 5px;
  color: #999;
}

/* Loading Indicator */
.loading {
  display: flex;
  align-items: center;
  height: 20px;
}

.typing-indicator {
  display: flex;
  align-items: center;
  gap: 4px;
}

.typing-indicator .dot {
  width: 6px;
  height: 6px;
  background-color: #ff5e00;
  border-radius: 50%;
  animation: dotPulse 1.4s infinite ease-in-out;
}

.typing-indicator .dot:nth-child(1) {
  animation-delay: 0s;
}

.typing-indicator .dot:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-indicator .dot:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes dotPulse {
  0%, 60%, 100% { transform: translateY(0); opacity: 0.6; }
  30% { transform: translateY(-4px); opacity: 1; }
}

/* Input Container */
.chat-input-container {
  padding: 15px;
  background: #000;
  border-top: 1px solid #333;
  display: flex;
  gap: 10px;
  align-items: center;
}

.chat-input-container input {
  flex: 1;
  padding: 12px 15px;
  border-radius: 25px;
  border: 1px solid #333;
  background: #1a1a1a;
  color: #fff;
  outline: none;
  font-family: 'CupraRegular', sans-serif;
  transition: border 0.3s;
}

.chat-input-container input:focus {
  border-color: #ff5e00;
}

.chat-input-container button {
  background: linear-gradient(135deg, #ff5e00, #ff8c00);
  color: #fff;
  border: none;
  padding: 0 20px;
  height: 40px;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s;
  min-width: 80px;
  font-family: 'CupraRegular', sans-serif;
  font-weight: bold;
  text-transform: uppercase;
  font-size: 12px;
  letter-spacing: 0.5px;
}

.chat-input-container button:hover {
  background: linear-gradient(135deg, #ff8c00, #ff5e00);
  box-shadow: 0 0 10px rgba(255, 94, 0, 0.5);
}

.chat-input-container button:disabled {
  background: #333;
  cursor: not-allowed;
  box-shadow: none;
}

/* Sending Animation */
.sending {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 94, 0, 0.3);
  border-radius: 50%;
  border-top-color: #ff5e00;
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Scrollbar */
.chat-messages::-webkit-scrollbar {
  width: 6px;
}

.chat-messages::-webkit-scrollbar-track {
  background: #1a1a1a;
}

.chat-messages::-webkit-scrollbar-thumb {
  background: #ff5e00;
  border-radius: 3px;
}
</style>