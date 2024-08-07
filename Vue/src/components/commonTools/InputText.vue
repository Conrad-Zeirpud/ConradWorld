<script setup>
import { ref,watch } from 'vue';

defineProps({
  titre: {
    type: String,
  },
});


// Définir l'émetteur d'événements
const emit = defineEmits(['update:value']);

// Créer une référence réactive pour la valeur de l'input
const inputValue = ref('');

// Regarder les changements de inputValue et émettre un événement
watch(inputValue, (newValue) => {
  emit('update:value', newValue);
});

////////////////////////////////////////////// COTE PARENT ///////////////////////////////////////////
//                                                                                                  //
// <MonInput :titre="titre" @update:value="handleUpdate" />                                         //
//                                                                                                  //
//                                                                                                  //
// import InputText  from '../components/InputText.vue' // Assurez-vous que le chemin est correct   //
// const inputValue = ref('');                                                                      //
//                                                                                                  //
// function handleUpdate(newValue) {                                                                //
//   inputValue.value = newValue;                                                                   //
// }                                                                                                //
//////////////////////////////////////////////////////////////////////////////////////////////////////
</script>

<template>
  <div id="inputBox">
    <input type="text" v-model="inputValue" required>
    <span>{{ titre }}</span>
  </div>
</template>

<style scoped>
#inputBox {
  position: relative;
  width: 300px;
  height: 50px;
  margin-bottom: 50px;
}

#inputBox input {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  border: 2px solid #000;
  outline: none;
  background: none;
  padding: 10px;
  border-radius: 10px;
  font-size: 1.2em;
}

#inputBox span {
  position: absolute;
  top: 14px;
  left: 20px;
  font-size: 1em;
  transition: 0.6s;
  font-family: sans-serif;
}

#inputBox input:focus ~ span,
#inputBox input:valid ~ span {
  transform: translateX(-13px) translateY(-35px);
  font-size: 0.8em;
}
</style>
