<script setup>
import { ref, watch } from "vue";

// Définir les props
const props = defineProps({
  legend: {
    type: String,
  },
  liste: {
    type: Array,
    required: true,
  },
});

// Définir l'émetteur d'événements
const emit = defineEmits(["update:list"]);

// Créer une référence réactive pour la valeur de l'input
const listUpdate = ref([]);

// Regarder les changements de listUpdate et émettre un événement
watch(listUpdate, (newValue) => {
  emit("update:list", newValue);
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
  <fieldset class="checkbox-group">
    <legend class="checkbox-group-legend">{{ legend }}</legend>
    <div
      class="checkbox"
      v-for="(item, index) in liste"
      :key="index"
      :for="item"
    >
      <label class="checkbox-wrapper">
        <input
          type="checkbox"
          class="checkbox-input"
          v-model="listUpdate"
          :value="item"
        />
        <span class="checkbox-tile">
          <span class="checkbox-icon">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="192"
              height="192"
              fill="currentColor"
              viewBox="0 0 256 256"
            >
              <rect width="256" height="256" fill="none"></rect>
              <circle cx="96" cy="144.00002" r="10"></circle>
              <circle cx="160" cy="144.00002" r="10"></circle>
              <path
                d="M74.4017,80A175.32467,175.32467,0,0,1,128,72a175.32507,175.32507,0,0,1,53.59754,7.99971"
                fill="none"
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="12"
              ></path>
              <path
                d="M181.59717,176.00041A175.32523,175.32523,0,0,1,128,184a175.32505,175.32505,0,0,1-53.59753-7.99971"
                fill="none"
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="12"
              ></path>
              <path
                d="M155.04392,182.08789l12.02517,24.05047a7.96793,7.96793,0,0,0,8.99115,4.20919c24.53876-5.99927,45.69294-16.45908,61.10024-29.85086a8.05225,8.05225,0,0,0,2.47192-8.38971L205.65855,58.86074a8.02121,8.02121,0,0,0-4.62655-5.10908,175.85294,175.85294,0,0,0-29.66452-9.18289,8.01781,8.01781,0,0,0-9.31925,5.28642l-7.97318,23.91964"
                fill="none"
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="12"
              ></path>
              <path
                d="M100.95624,182.08757l-12.02532,24.0508a7.96794,7.96794,0,0,1-8.99115,4.20918c-24.53866-5.99924-45.69277-16.459-61.10006-29.85069a8.05224,8.05224,0,0,1-2.47193-8.38972L50.34158,58.8607a8.0212,8.0212,0,0,1,4.62655-5.1091,175.85349,175.85349,0,0,1,29.66439-9.18283,8.0178,8.0178,0,0,1,9.31924,5.28642l7.97318,23.91964"
                fill="none"
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="12"
              ></path>
            </svg>
          </span>
          <span class="checkbox-label">{{ item }}</span>
        </span>
      </label>
    </div>
  </fieldset>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap");

*,
*:after,
*:before {
  box-sizing: border-box;
}

body {
  font-family: "Inter", sans-serif;
  line-height: 1.5;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f8f8f9;
}

.checkbox-group {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 90%;
  margin-left: auto;
  margin-right: auto;
  max-width: 600px;
  user-select: none;
  border-color: var(--blue-700);
}

.checkbox-group > * {
  margin: 0.5rem 0.5rem;
}

.checkbox-group-legend {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--blue-700);
  text-align: center;
  line-height: 1.125;
  margin-bottom: 1.25rem;
}

.checkbox-input {
  /* Code to hide the input */
  clip: rect(0 0 0 0);
  clip-path: inset(100%);
  height: 1px;
  overflow: hidden;
  position: absolute;
  white-space: nowrap;
  width: 1px;
}

.checkbox-input:checked + .checkbox-tile {
  border-color: #2260ff;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  color: #2260ff;
}

.checkbox-input:checked + .checkbox-tile:before {
  transform: scale(1);
  opacity: 1;
  background-color: #2260ff;
  border-color: #2260ff;
}

.checkbox-input:checked + .checkbox-tile .checkbox-icon,
.checkbox-input:checked + .checkbox-tile .checkbox-label {
  color: #2260ff;
}

.checkbox-input:focus + .checkbox-tile {
  border-color: #2260ff;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1), 0 0 0 4px #b5c9fc;
}

.checkbox-input:focus + .checkbox-tile:before {
  transform: scale(1);
  opacity: 1;
}

.checkbox-tile {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 7rem;
  min-height: 7rem;
  border-radius: 0.5rem;
  border: 2px solid #b5bfd9;
  background-color: #fff;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  transition: 0.15s ease;
  cursor: pointer;
  position: relative;
}

.checkbox-tile:before {
  content: "";
  position: absolute;
  display: block;
  width: 1.25rem;
  height: 1.25rem;
  border: 2px solid #b5bfd9;
  background-color: #fff;
  border-radius: 50%;
  top: 0.25rem;
  left: 0.25rem;
  opacity: 0;
  transform: scale(0);
  transition: 0.25s ease;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='192' height='192' fill='%23FFFFFF' viewBox='0 0 256 256'%3E%3Crect width='256' height='256' fill='none'%3E%3C/rect%3E%3Cpolyline points='216 72.005 104 184 48 128.005' fill='none' stroke='%23FFFFFF' stroke-linecap='round' stroke-linejoin='round' stroke-width='32'%3E%3C/polyline%3E%3C/svg%3E");
  background-size: 12px;
  background-repeat: no-repeat;
  background-position: 50% 50%;
}

.checkbox-tile:hover {
  border-color: #2260ff;
}

.checkbox-tile:hover:before {
  transform: scale(1);
  opacity: 1;
}

.checkbox-icon {
  transition: 0.375s ease;
  color: #494949;
}

.checkbox-icon svg {
  width: 3rem;
  height: 3rem;
}

.checkbox-label {
  color: #707070;
  transition: 0.375s ease;
  text-align: center;
}
</style>
