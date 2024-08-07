<script setup>
import { ref } from "vue";

import Header from "../components/Header.vue";
import InputCheckbox from "@/components/commonTools/InputCheckbox.vue";
import InputRadio from "@/components/commonTools/InputRadio.vue";

const listWod = ref([
  "For Time",
  "AMRAP",
  "EMOM",
  "Death By",
  "You Go I Go",
  "Random",
]);
const listDomain = ref(["gymnastique", "halterophilie", "conditionning"]);

const selectedWod = ref("");
function UpdateWod(newValue) {
  selectedWod.value = newValue;
}

const selectedDomain = ref([]);
function UpdateDomain(newValue) {
  selectedDomain.value = newValue;
}
function genWod() {
  console.log();
}
</script>

<template>
  <Header></Header>
  <form id="PanelFilter">
    <div class="zoneSelection">
      <InputRadio
        legend="Type de wod"
        :liste="listWod"
        @update:value="UpdateWod"
      ></InputRadio>
    </div>
    <div class="zoneSelection">
      <InputCheckbox
        legend="Domaines"
        :liste="listDomain"
        @update:list="UpdateDomain"
      ></InputCheckbox>
    </div>

    <input id="generatorBtn" type="button" value="Générer" @click="genWod" />
  </form>
</template>

<style scoped>
#PanelFilter {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100vh;
  background: radial-gradient(
    circle,
    var(--purple-700),
    var(--purple-300),
    var(--purple-400),
    var(--blue-300),
    var(--blue-100)
  );
  align-items: start;
}

.zoneSelection {
  width: 80%;
  height: 250px;
  /* background-color: rgb(100, 100, 155); */
  border-radius: 25px;
  padding: 25px;
  margin: 50px auto;
}

.tabsBtn {
  display: inline-flex;
  width: 100%;
  justify-content: space-around;
  align-items: center;
  margin-top: 20px;
}
input[type="radio"],
input[type="checkbox"] {
  display: none;
}
#generatorBtn {
  margin: 0px auto;
  font-size: 36px;
  background-color: var(--purple-700);
}

#generatorBtn:hover {
  background-color: var(--purple-300);
}

label {
  color: blueviolet;
  border: 3px solid blueviolet;
  background-color: white;
  padding: 3px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 36px;
}

.zoneSelection .clicked {
  color: var(--green-300);
  border: 3px solid var(--green-300);
}
</style>
