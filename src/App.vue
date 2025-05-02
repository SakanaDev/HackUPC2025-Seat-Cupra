<script>
import CarOutside from './components/CarOutside.vue';
import CarInside from './components/CarInside.vue';

export default {
  data() {
    return {
      isOutside: true,
    }
  },
  components: {
    CarOutside,
    CarInside,
  }
}
</script>

<template>
  <header>
    <a href="">
      <img src="https://www.cupraofficial.es/etc.clientlibs/cupra-website/components/clientlibs/resources/icons/logos/logo-cupra.svg" alt="">
    </a>
  </header>
  
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
</template>

<style scoped>
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

.view-selector {
  z-index: 100; /* Menor que los botones de navegación */
}

header {
  z-index: 1000; /* El más alto */
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
</style>