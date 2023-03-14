import adapter from "@sveltejs/adapter-static";

const dev = process.env.NODE_ENV === "development";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter(),
    target: "#svelte",
    trailingSlash: "ignore",
    paths: {
      assets: "docs",
      pages: "docs",
      paths: {
        base: process.env.NODE_ENV === "production" ? "/birthday-dates" : "",
      },
    },
  },
};

// const config = {};

export default config;
