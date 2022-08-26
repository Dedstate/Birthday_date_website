<script>
  const LETTER = "Г"; // Class letter to append to the year
  const YEAR = 2013; // Year school started
  function getClass() {
    var today = new Date();
    let y = today.getFullYear() - YEAR;
    if (today.getMonth() < 6) {
      y -= 1;
    }
    if (y > 11) {
      return "выпустников 11" + LETTER + " класса";
    }
    return y + LETTER;
  }

  import csv from "jquery-csv";
  const pages = ["/other", "/others", "/archive", "/history", "/archived"];

  let archived = false;
  let path = "birthdays.csv";
  console.log(location.pathname);
  if (pages.includes(location.pathname.replace(".html", ""))) {
    archived = true;
    path = "../birthdays_archived.csv";
  }
  let dates = [];
  let grade = getClass();

  fetch(path)
    .then((response) => response.text())
    .then((text) => {
      dates = csv.toArrays(text);
    });
</script>

<!-- Set Title -->
{#if archived}
  <title>Архив — Дни рождений {grade}</title>
{:else}
  <title>Дни рождений {grade}</title>
{/if}

<main>
  <h1 class="text-center">Дни рождений {grade}</h1>
  {#if archived}
    <h2 class="text-center">Архивные записи</h2>
  {/if}
  <div class="container-fluid mt-3">
    <div class="row row-cols-auto">
      {#each dates as student, i}
        <div class="col flex-grow-1">
          <!-- Student Card -->
          <div class="card my-2">
            <div class="card-body">
              <!-- Name -->
              <h4 class="text-center card-title fw-normal">{student[0]}</h4>
              <!-- Date of Birth -->
              {#if !student[1]}
                <h6 class="text-center card-subtitle text-muted">—</h6>
              {:else}
                <h6 class="text-center card-subtitle text-muted">
                  {student[1]}
                </h6>
              {/if}
            </div>
            <!-- Year when left, if archived mode -->
            {#if archived}
              <div class="card-footer text-center p-1">
                <small class="text-muted">{student[2]}</small>
              </div>
            {/if}
          </div>
          <!-- End Student Card -->
        </div>
      {/each}
    </div>
  </div>
  <hr />
  <div id="bottom-navbar" class="container">
    <div class="row">
      {#if archived}
        <div class="text-center col-sm container text-nowrap">
          <a href=".."><p>⟨ Вернуться на главную</p></a>
        </div>
      {:else}
        <div class="text-center col-sm container text-nowrap">
          <a href="archived"><p>Перейти в архив ⟩</p></a>
        </div>
      {/if}
      <div class="text-center col-sm container text-nowrap">
        <a href="https://github.com/germanivanov0719/birthday-dates">
          <p>Исходный код на GitHub</p>
        </a>
      </div>
      <div class="text-center col-sm container text-nowrap">
        <p id="info">© German Ivanov 2022</p>
      </div>
    </div>
  </div>
</main>
