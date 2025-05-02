<script>
export default {
  methods: {
    goToNextPage() {
      this.$emit('video-ended')  // Emite evento al padre
    },
  }
}

</script>

<template>
    <div ref="container" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%;">
      <video
        ref="video"
        autoplay
        muted
        playsinline
        @ended="goToNextPage"
        @canplay="enterFullscreen"
        style="width: 100vw; height: 100vh; object-fit: cover; background-color: black;">
        <source src="/img/videoplayback.mp4" type="video/mp4" />
      </video>
    </div>
</template>

<style scoped>

</style>
