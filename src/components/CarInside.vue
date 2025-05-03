<script>
export default {
  data() {
    return {
      images: ['in-1.png', 'in-2.png', 'in-3.png'],
      currentIndex: 0,
      hotspots: [
        {
          id: 1,
          index: 0,
          top: '54%',
          left: '8%',
          width: '120px',
          height: '40px',
          part: 'Door Handle',
          clicked: false,
        
        },
        {
          id: 2,
          index: 0,
          top: '69.8%',
          left: '13%',
          width: '30px',
          height: '30px',
          part: 'Central locking',
          clicked: false
        },
        {
          id: 3,
          index: 0,
          top: '48%',
          left: '24%',
          width: '100px',
          height: '35px',
          part: 'Turn signal and main beam lever',
          clicked: false
        },
        {
          id: 4,
          index: 0,
          top: '54%',
          left: '21%',
          width: '130px',
          height: '60px',
          part: 'Multifunction steering wheel control panels ',
          clicked: false
        },
        {
          id: 5,
          index: 0,
          top: '32%',
          left: '37%',
          width: '130px',
          height: '70px',
          part: 'Digital Cockpit',
          clicked: false
        },
        {
          id: 6,
          index: 0,
          top: '53%',
          left: '54%',
          width: '32px',
          height: '60px',
          part: 'Gear selector',
          clicked: false
        },
        {
          id: 7,
          index: 0,
          top: '53%',
          left: '54%',
          width: '32px',
          height: '60px',
          part: 'Gear selector',
          clicked: false
        },
        {
          id: 8,
          index: 0,
          top: '23%',
          left: '61%',
          width: '522px',
          height: '300px',
          part: ' Infotainment system',
          clicked: false
        },
        {
          id: 9,
          index: 0,
          top: '67%',
          left: '25%',
          width: '40px',
          height: '40px',
          part: 'Fuses ›',
          clicked: false
        },
        {
          id: 10,
          index: 0,
          top: '67%',
          left: '25%',
          width: '40px',
          height: '40px',
          part: 'Fuses ›',
          clicked: false
        },
        {
          id: 11,
          index: 0,
          top: '52%',
          left: '31%',
          width: '120px',
          height: '120px',
          part: 'wheel with horn',
          clicked: false
        },
        {
          id: 12,
          index: 1,
          top: '24.5%',
          left: '29%',
          width: '100px',
          height: '45px',
          part: 'Main menu',
          clicked: false
        },
        {
          id: 13,
          index: 1,
          top: '24.5%',
          left: '37%',
          width: '160px',
          height: '45px',
          part: 'Shortcuts to infotainment',
          clicked: false
        },
        {
          id: 14,
          index: 1,
          top: '26%',
          left: '67%',
          width: '50px',
          height: '45px',
          part: 'Active functions',
          clicked: false
        },
        {
          id: 15,
          index: 1,
          top: '26%',
          left: '71.5%',
          width: '150px',
          height: '45px',
          part: 'Status bar',
          clicked: false
        },
        {
          id: 16,
          index: 1,
          top: '83%',
          left: '35%',
          width: '580px',
          height: '35px',
          part: 'Climabar',
          clicked: false
        },
        {
          id: 17,
          index: 1,
          top: '83%',
          left: '35%',
          width: '580px',
          height: '35px',
          part: 'Climabar',
          clicked: false
        },
        {
          id: 18,
          index: 2,
          top: '47%',
          left: '24%',
          width: '40px',
          height: '55px',
          part: 'airbag',
          clicked: false
        },
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