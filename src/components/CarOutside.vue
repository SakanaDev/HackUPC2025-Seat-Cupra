<script>
export default {
  data() {
    return {
      images: ['out-1.png', 'out-2.png', 'out-3.png', 'out-4.png', 'out-5.png', 'out-6.png'],
      currentIndex: 0,
      hotspots: [
        {
          id: 1,
          index: 0,
          top: '45%',
          left: '15%',
          width: '500px',
          height: '90px',
          part: 'Motor',
          clicked: false
        },
        {
          id: 2,
          index: 0,
          top: '60%',
          left: '47%',
          width: '130px',
          height: '200px',
          part: 'Rueda',
          clicked: false
        },
        {
          id: 3,
          index: 0,
          top: '58%',
          left: '72%',
          width: '100px',
          height: '170px',
          part: 'Rueda Trasera',
          clicked: false
        },
        {
          id: 4,
          index: 0,
          top: '70%',
          left: '40%',
          width: '40px',
          height: '40px',
          part: 'Puerta',
          clicked: false
        }
      ]
    }
  },
  methods: {
    nextImage() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
    },
    prevImage() {
      this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
    },
    handleHotspotClick(hotspot) {
      hotspot.clicked = true;
      console.log(`Parte clickeada: ${hotspot.part}`);
      alert(`Has seleccionado: ${hotspot.part}`);
      
      setTimeout(() => {
        hotspot.clicked = false;
      }, 500);
    }
  },
  computed: {
    currentImage() {
      return new URL(`../assets/${this.images[this.currentIndex]}`, import.meta.url).href;
    },
    visibleHotspots() {
      // Filtrar hotspots que coincidan con el currentIndex actual
      return this.hotspots.filter(hotspot => hotspot.index === this.currentIndex);
    }
  }
}
</script>

<template>
  <div class="fullscreen-container">
    <!-- Imagen FULLSCREEN -->
    <img :src="currentImage" :alt="`Image ${currentIndex + 1}`" class="fullscreen-image">
    
    <!-- Botones de navegación -->
    <button class="nav-button left" @click="prevImage">
      &lt;
    </button>
    <button class="nav-button right" @click="nextImage">
      &gt;
    </button>
    
    <!-- Hotspots interactivos (solo los visibles) -->
    <button
      v-for="hotspot in visibleHotspots"
      :key="hotspot.id"
      class="hotspot"
      :style="{
        top: hotspot.top,
        left: hotspot.left,
        width: hotspot.width,
        height: hotspot.height,
      }"
      @click="handleHotspotClick(hotspot)"
      :class="{ 'hotspot-clicked': hotspot.clicked }"
      :title="`Ver ${hotspot.part}`"
    ></button>
  </div>
</template>

<style scoped>
/* Tus estilos existentes se mantienen igual */
.fullscreen-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  z-index: 1;
}

.fullscreen-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
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
  z-index: 1001;
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

.hotspot {
  position: absolute;
  background-color: rgba(255, 255, 0, 0.3);
  border: 2px dashed #ffcc00;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 100;
  padding: 0;
  margin: 0;
  outline: none;
}

.hotspot:hover {
  background-color: rgba(255, 200, 0, 0.5);
  transform: scale(1.1);
}

.hotspot-clicked {
  background-color: rgba(0, 255, 0, 0.5) !important;
  transform: scale(1.2);
  border: 2px solid #00ff00;
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
  
  .hotspot {
    width: 40px !important;
    height: 40px !important;
  }
}
</style>