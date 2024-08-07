<script setup></script>

<template>
  <h2>Me contacter</h2>
  <div id="footer">
    <div class="blocks">
      <h3>Adresse mail</h3>
      <ul>
        <li>
          <a href="mailto:arthur-conrad.dupriez@outlook.fr">
            arthur-conrad.dupriez@outlook.fr
          </a>
        </li>
      </ul>
    </div>
    <div class="blocks">
      <h3>Réseaux sociaux</h3>
      <ul id="reseaux">
        <li>
          <a href="https://www.instagram.com/digitalconrad/"
            ><img
              src="../assets/icons/instagram.png"
              alt="instagram"
              class="logo"
          /></a>
        </li>
        <li>
          <a href="https://fr.linkedin.com/in/arthur-conrad-dupriez-4472b0173"
            ><img
              src="../assets/icons/linkedin.png"
              alt="linkedin"
              class="logo"
          /></a>
        </li>
        <li>
          <a href="https://github.com/Conrad-Zeirpud"
            ><img src="../assets/icons/github.png" alt="github" class="logo"
          /></a>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
#footer {
  display: inline-flex;
  width: 60%;
  flex-direction: row;
  align-items: baseline;
  justify-content: center;
  margin-top: 5px;
}

.blocks {
  padding: 0px 10px;
}

h2 {
  color: var(--brown-500);
  margin: 50px 0px 0px 0px;
  width: 100%;
  text-align: center;
}
h3 {
  color: var(--brown-500);
  margin: 15px 0px 5px 0px;
}

li {
  list-style: none;
  margin: 5px;
}
.logo {
  height: 50px;
  width: 50px;
}
#reseaux {
  display: flex;
  flex-direction: row;
}
</style>
