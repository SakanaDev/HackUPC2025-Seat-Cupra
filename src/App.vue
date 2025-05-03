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
      
      // Agregar mensaje del usuario
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
        text: 'Gemini is typing...',
        sender: 'bot',
        isLoading: true,
        timestamp: new Date().toLocaleTimeString()
      });
      
      try {
        const response = await fetch('http://localhost:5000/ask', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({question: pregunta})
        });

        const data = await response.json();
        
        // Reemplazar mensaje de carga con la respuesta real
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
        <button class="header-btn">Drove it</button>
      </div>
    </header>
    
    <!-- Chat container -->
    <div class="chat-container" ref="chatContainer" v-if="chatbotFlag">
      <div v-for="(message, index) in messages" :key="index" 
           :class="['message', message.sender]">
        <div class="message-content">
          <div class="message-text" v-if="!message.isLoading">{{ message.text }}</div>
          <div class="message-text loading" v-else>
            <span class="dot-flashing"></span>
          </div>
          <div class="message-time">{{ message.timestamp }}</div>
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
/* Estilos existentes */
header {
  position: relative;
  background-color: black;
  padding: 0 16px;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 1000;
}

.header-buttons {
  display: flex;
  gap: 15px;
}

.header-btn {
  background: black;
  border: none;
  color: white;
  padding: 10px 16px;
  border-radius: 20px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s ease;
}

.header-btn:hover {
  background-color: rgba(255, 255, 255, 0.8);
  color: black;
}

.car-container {
  position: relative;
  height: calc(100vh - 60px);
  width: 100vw;
}

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
  background: black;
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
  background: white;
}

.view-selector button.active img {
  filter: invert(0);
}

.main-content {
  position: relative;
  z-index: 1;
}

/* Nuevos estilos para el chat */
.chat-container {
  font-family: 'CupraRegular', serif;
  position: fixed;
  top: 80px;
  right: 20px;
  width: 350px;
  height: 500px;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding: 15px;
  z-index: 1000;
}

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
  padding: 10px 15px;
  border-radius: 18px;
  position: relative;
}

.user .message-content {
  background-color: #0078FF;
  color: white;
  border-bottom-right-radius: 5px;
}

.bot .message-content {
  background-color: #f1f1f1;
  color: #333;
  border-bottom-left-radius: 5px;
}

.message-text {
  word-wrap: break-word;
}

.message-time {
  font-size: 0.7em;
  opacity: 0.7;
  text-align: right;
  margin-top: 5px;
}

.chat-input-container {
  position: fixed;
  top: 590px;
  right: 20px;
  width: 350px;
  display: flex;
  gap: 10px;
  z-index: 1000;
}

.chat-input-container input {
  flex: 1;
  padding: 12px 15px;
  border-radius: 25px;
  border: 1px solid #ccc;
  outline: none;
}

.chat-input-container button {
  background: black;
  color: white;
  border: none;
  padding: 0 20px;
  border-radius: 25px;
  cursor: pointer;
  transition: background 0.3s;
  min-width: 80px;
}

.chat-input-container button:disabled {
  background: #ccc;
  cursor: not-allowed;
}

/* Animación de carga */
.dot-flashing {
  position: relative;
  width: 10px;
  height: 10px;
  border-radius: 5px;
  background-color: #999;
  color: #999;
  animation: dotFlashing 1s infinite linear alternate;
  animation-delay: 0.5s;
}

.dot-flashing::before, .dot-flashing::after {
  content: '';
  display: inline-block;
  position: absolute;
  top: 0;
  width: 10px;
  height: 10px;
  border-radius: 5px;
  background-color: #999;
  color: #999;
}

.dot-flashing::before {
  left: -15px;
  animation: dotFlashing 1s infinite alternate;
  animation-delay: 0s;
}

.dot-flashing::after {
  left: 15px;
  animation: dotFlashing 1s infinite alternate;
  animation-delay: 1s;
}

@keyframes dotFlashing {
  0% {
    background-color: #999;
  }
  50%, 100% {
    background-color: #e0e0e0;
  }
}

.loading {
  min-height: 20px;
}

.sending {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255,255,255,.3);
  border-radius: 50%;
  border-top-color: #fff;
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>