<script>
  import csv from "jquery-csv";
  const sources = ["birthdays.csv", "birthdays_archived.csv"];
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

  async function getDates() {
    let r = [];
    for (let i = 0; i < sources.length; i++) {
      let text = await (await fetch(sources[i])).text();
      r.push(await csv.toArrays(text));
    }

    return { normal: r[0], archived: r[1] };
  }

  async function setArchived(value = null) {
    if (value !== null && typeof value == "boolean") {
      archived = value;
    } else if (archived) {
      archived = false;
    } else {
      archived = true;
    }
    if ("loaded" in allDates && allDates["loaded"] == false) {
      let loaded = await allDatesLoading;
      loaded["loaded"] = true;
      // @ts-ignore
      allDates = loaded;
    }
    // dates = archived ? allDates["archived"] : allDates["normal"];
  }

  let archived = false;
  let allDatesLoading = getDates();
  let allDates = { archived: [], normal: [], loaded: false };
  $: dates = archived ? allDates["archived"] : allDates["normal"];
  setArchived(false);
  let grade = getClass();
</script>

<!-- Set Title -->

<title>
  {#if archived}Архив — {/if}Дни рождений {grade}
</title>

<main>
  <h1 class="text-center">Дни рождений {grade}</h1>

  <h2 class="text-center text-muted" style="font-size: 1.5em">
    {#if archived}
      Архив
    {:else}
      Сейчас в классе
    {/if}
  </h2>

  <div class="container-fluid mt-3">
    <div class="row row-cols-auto">
      {#each dates as student}
        <div class="col flex-grow-1">
          <!-- Student Card -->
          <div class="card my-2">
            <div class="card-body">
              <!-- Name -->
              <h3 class="text-center card-title fw-normal">{student[0]}</h3>
              <!-- Date of Birth -->
              <h4
                class="text-center card-subtitle text-muted"
                style="font-size: 1.2em"
              >
                {#if !student[1]}
                  —
                {:else}
                  {student[1]}
                {/if}
              </h4>
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
      <div
        class="text-center d-flex justify-content-center col-sm container text-nowrap"
      >
        <button class="btn btn-primary m-3" on:click={setArchived}>
          {#if archived}
            ⟨ Вернуться на главную
          {:else}
            Перейти в архив ⟩
          {/if}
        </button>
      </div>
      <div
        class="text-center d-flex justify-content-center align-items-center col-sm container text-nowrap"
      >
        <a href="https://github.com/germanivanov0719/birthday-dates">
          <p class="m-3">Исходный код на GitHub</p>
        </a>
      </div>
      <div
        class="text-center d-flex justify-content-center align-items-center col-sm container text-nowrap"
      >
        <p class="m-3" id="info">© German Ivanov 2022</p>
      </div>
    </div>
  </div>
</main>
