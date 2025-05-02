<script>
export default {
  mounted() {
    // Intenta iniciar el video automáticamente
    this.$refs.video.play().catch(e => {
      console.log("Autoplay prevented, showing play button");
    });
  },
  methods: {
    goToNextPage() {
      this.$emit('video-ended');  // Emite evento al padre
    },
    enterFullscreen() {
      // Opcional: Intentar entrar en pantalla completa
      if (this.$refs.container.requestFullscreen) {
        this.$refs.container.requestFullscreen().catch(e => {
          console.log("Fullscreen error:", e);
        });
      }
    }
  }
}
</script>

<template>
  <div ref="container" class="video-container">
    <video
      ref="video"
      autoplay
      muted
      playsinline
      @ended="goToNextPage"
      @canplay="enterFullscreen"
      class="fullscreen-video">
      <source src="../assets/videoplayback.mp4" type="video/mp4" />
      Tu navegador no soporta videos HTML5
    </video>
  </div>
</template>

<style scoped>
.video-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 2000; /* Mayor que todo lo demás */
  background-color: black;
}

.fullscreen-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>