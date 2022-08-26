import adapter from "@sveltejs/adapter-auto";
// import preprocess from "svelte-preprocess";
// was "@sveltejs/adapter-auto"

// const dev = "production" === "development";
const dev = process.env.NODE_ENV === "development";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // preprocess: preprocess(),
  kit: {
    adapter: adapter(),
    // hydrate the <div id="svelte"> element in src/app.html
    target: "#svelte",
    trailingSlash: "ignore",
    paths: {
      assets: "docs",
      pages: "docs",
      base: "/birthday-dates",
    },
  },
};

// const config = {};

export default config;
