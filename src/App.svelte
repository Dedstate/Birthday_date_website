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
      toggleArchiveText = "Перейти в архив ⟩";
    } else {
      archived = true;
      toggleArchiveText = "⟨ Вернуться на главную";
    }
    if ('loaded' in allDates && allDates['loaded'] == false){
      let loaded = await allDatesLoading;
      loaded['loaded'] = true;
      // @ts-ignore
      allDates = loaded;
    }
    // dates = archived ? allDates["archived"] : allDates["normal"];
  }

  let archived = false;
  let toggleArchiveText = "Перейти в архив ⟩";
  let allDatesLoading = getDates();
  let allDates = { archived: [], normal: [], loaded: false };
  $: dates = archived ? allDates["archived"] : allDates["normal"];
  setArchived(false);
  let grade = getClass();
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
      {#each dates as student}
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
      <div
        class="text-center d-flex justify-content-center col-sm container text-nowrap"
      >
        <button class="btn btn-primary m-3" on:click={setArchived}
          ><p class="m-0">{toggleArchiveText}</p></button
        >
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
