<script setup></script>

<template>
  <main>
    <img
      src="http://92.222.170.90:9000/conrad/logo/logo.png"
      alt="ConradWorld"
      height="100"
    />
    <nav>
      <RouterLink class="link" to="/app">Mes applications</RouterLink>
      <RouterLink class="link" to="/skill">Mes skills</RouterLink>
      <RouterLink class="link" to="/about">Go to About</RouterLink>
    </nav>
  </main>
</template>

<style scoped>
main {
  width: 100%;
  background-color: var(--emerald-green-800);
  padding: 10px 50px;
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
}
nav {
  /* width: 1750px; */
  display: inline-flex;
  justify-content: space-around;
  align-items: center;
  flex-grow: 1;
  padding-left: 50px;
  height: 100px;
}

.link {
  font-size: 36px;
  font-family: sans-serif;
  padding: 0px 25px;
  text-decoration: none;
  color: var(--emerald-green-200);
  transition-duration: 1s, 3s;
  height: 50px;
}

.link:hover {
  color: var(--green-200);
  border-bottom: 3px solid var(--green-200);
  padding-bottom: 10px;
}
</style>
