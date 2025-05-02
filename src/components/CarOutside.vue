<script>
export default {
  data() {
    return {
      images: ['out-1.png', 'out-2.png', 'out-3.png', 'out-4.png', 'out-5.png', 'out-6.png'],
      currentIndex: 0
    }
  },
  methods: {
    nextImage() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
    },
    prevImage() {
      this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
    }
  },
  computed: {
    currentImage() {
      return new URL(`../assets/${this.images[this.currentIndex]}`, import.meta.url).href;
    }
  }
}
</script>

<template>
  <div class="fullscreen-container">
    <!-- Imagen FULLSCREEN -->
    <img :src="currentImage" :alt="`Image ${currentIndex + 1}`" class="fullscreen-image">
    
    <!-- Botones de navegación (ahora funcionales) -->
    <button class="nav-button left" @click="prevImage">
      &lt;
    </button>
    <button class="nav-button right" @click="nextImage">
      &gt;
    </button>
  </div>
</template>

<style scoped>
.fullscreen-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  z-index: 0; /* IMPORTANTE: Cambiado de -1000 a 0 */
}

.fullscreen-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 0;
}

.nav-button {
  position: fixed;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  font-size: 28px;
  cursor: pointer;
  z-index: 1001; /* Superior al view-selector */
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.3s ease;
}

.nav-button:hover {
  background: rgba(0, 0, 0, 0.8);
  transform: translateY(-50%) scale(1.1);
}

.left {
  left: 30px;
}

.right {
  right: 30px;
}

@media (max-width: 768px) {
  .nav-button {
    width: 50px;
    height: 50px;
    font-size: 24px;
  }
  .left {
    left: 15px;
  }
  .right {
    right: 15px;
  }
}
</style>