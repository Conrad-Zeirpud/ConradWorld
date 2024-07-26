<script setup>
const props = defineProps({
  front: {
    type: String,
    default: "",
  },
  back: {
    type: String,
    default: "",
  },
});
</script>

<template>
  <div class="card-container">
    <div class="card">
      <div class="card-front">
        <div>{{ props.front }}</div>
      </div>
      <div class="card-back">
        <div>{{ props.back }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-container {
  position: relative;
  height: 100px;
  min-height: 100px;
  width: 100px;
  min-width: 100px;
}
.card-container:hover .card {
  transform: rotateY(180deg);
}
.card {
  position: absolute;
  height: 100%;
  width: 100%;
  transition: all 0.3s ease;
  transform-style: preserve-3d;
}
.card-front {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  height: 100%;
  width: 100%;
  background: var(--brown-300);
  backface-visibility: hidden;
  border: 7px solid var(--brown-800);
  border-radius: 20%;
  font-size: 36px;
  cursor: pointer;
}
.card-back {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  height: 100%;
  width: 100%;
  background: var(--brown-500);
  border: 7px solid var(--brown-900);
  border-radius: 20%;
  backface-visibility: hidden;
  transform: rotateY(-180deg);
  font-size: 16px;
  cursor: pointer;
}
</style>
