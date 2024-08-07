<script setup>
const props = defineProps({
  titre: {
    type: String,
    default: "",
  },
  imagePath: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <div id="sticker">
    <img
      :src="'http://92.222.170.90:9000/conrad/logo' + imagePath"
      :alt="titre"
    />
    <p>{{ titre }}</p>
  </div>
</template>

<style scoped>
#sticker {
  width: 125px;
  height: 125px;
  margin: 5px;
  padding: 10px;
  border: 2px solid black;
  border-radius: 25px;
  background-color: var(--grey-500);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: none;
  background-image: linear-gradient(
    to bottom right,
    var(--brown-300),
    var(--brown-500)
  );
  box-shadow: 1px 1px 1px var(--brown-700), inset 2px 3px 5px var(--brown-700),
    inset -2px -3px 5px rgba(255, 255, 255, 0.5);
}
/* 
#sticker:hover {
  background-image: linear-gradient(
    to bottom right,
    var(--brown-100),
    var(--brown-300)
  );
  box-shadow: inset 2px 2px 1px var(--brown-700),
    inset 2px 3px 5px var(--brown-700),
    inset -2px -3px 5px rgba(255, 255, 255, 0.5);
} */

img {
  min-height: 80px;
  min-width: 80px;
  margin: 5px;

  object-fit: cover; /* Maintient les proportions de l'image */
}
</style>
