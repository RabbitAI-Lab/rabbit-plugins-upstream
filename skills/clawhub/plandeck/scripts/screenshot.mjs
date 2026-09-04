#!/usr/bin/env node
// screenshot.mjs — render the board headlessly and save a PNG.
//
// A repeatable visual test with zero dependencies: it bakes the plan into a
// self-contained page and drives your already-installed Chrome or Edge in
// headless mode. Set PLANDECK_BROWSER to point at a specific binary.
//
//   node scripts/screenshot.mjs [planDir] [out.png]
//   npm run screenshot

import { execFileSync } from "node:child_process";
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { buildPayload } from "./lib/deck.mjs";
import { writeBoardApp } from "./lib/render.mjs";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const planDir = resolve(process.argv[2] || join(root, "examples", "ship-onboarding-flow"));
const out = resolve(process.argv[3] || join(root, "media", "board.png"));

const appDir = writeBoardApp(planDir);
const payload = buildPayload(planDir);
const read = (name) => readFileSync(join(appDir, name), "utf8");
const markPath = join(root, "media", "plandeck-mark.svg");
const mark = existsSync(markPath) ? `data:image/svg+xml;utf8,${encodeURIComponent(readFileSync(markPath, "utf8"))}` : "";

const html = read("index.html")
  .replace('<link rel="stylesheet" href="./styles.css">', `<style>${read("styles.css")}</style>`)
  .replaceAll("./plandeck-mark.svg", mark)
  .replace('<script src="./app.js" type="module"></script>', `<script>window.__PLANDECK_STATIC__=${JSON.stringify(payload)}</script><script type="module">${read("app.js")}</script>`);

const previewPath = join(appDir, "preview.html");
writeFileSync(previewPath, html);

const bin = findBrowser();
if (!bin) {
  console.error("No Chrome or Edge found. Install one, set PLANDECK_BROWSER, or run `plandeck board` and screenshot manually.");
  process.exit(1);
}

execFileSync(bin, [
  "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-color-profile=srgb",
  "--window-size=1680,1000", `--screenshot=${out}`, `file:///${previewPath.replaceAll("\\", "/")}`,
], { stdio: "ignore" });

if (!existsSync(out)) {
  console.error(`Browser ran but produced no file at ${out}.`);
  process.exit(1);
}
console.log(`Wrote ${out} (rendered by ${bin.split(/[\\/]/).pop()})`);

function findBrowser() {
  const candidates = [
    process.env.PLANDECK_BROWSER,
    "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    "C:/Program Files/Microsoft/Edge/Application/msedge.exe",
    "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser", "/usr/bin/microsoft-edge",
  ].filter(Boolean);
  return candidates.find((p) => { try { return existsSync(p); } catch { return false; } });
}
