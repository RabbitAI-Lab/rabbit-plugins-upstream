#!/usr/bin/env node
/**
 * Convert .excalidraw JSON → .excalidraw.md (Obsidian Excalidraw plugin format)
 * Uses LZ-String compression.
 *
 * Usage:
 *   node scripts/compress.js input.excalidraw [output.excalidraw.md]
 *
 * If output omitted, writes to stdout.
 */
const fs = require("fs");
const path = require("path");

let lzstring;
try {
    lzstring = require("lz-string");
} catch {
    // Try local or relative
    try { lzstring = require("/tmp/node_modules/lz-string"); }
    catch { lzstring = require(require("path").join(process.cwd(), "node_modules", "lz-string")); }
}

const inputPath = process.argv[2];
if (!inputPath) {
    console.error("Usage: compress.js input.excalidraw [output.excalidraw.md]");
    process.exit(1);
}

const raw = fs.readFileSync(inputPath, "utf8");
const data = JSON.parse(raw);

// Wrap in excalidraw export format
const outData = {
    type: "excalidraw",
    version: 2,
    source: data.source || "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag2.24.2",
    elements: data.elements || data.data?.elements || [],
    appState: data.appState || { viewBackgroundColor: "#ffffff", gridSize: null },
    files: data.files || {}
};

const jsonStr = JSON.stringify(outData);
const compressed = lzstring.compressToBase64(jsonStr);

// Text Elements section
const texts = outData.elements.filter(e => e.type === "text" && !e.containerId);
const textLines = texts.map(e => (e.text || "").replace(/\n/g, " ") + " ^" + e.id);

let md = "---\nexcalidraw-plugin: parsed\ntags:\n  - excalidraw\n---\n\n";
md += "==\u26a0  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. \u26a0== ";
md += "You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. ";
md += "For more info check in plugin settings under 'Saving'\n\n";
md += "# Excalidraw Data\n\n## Text Elements\n\n";
for (const line of textLines) md += line + "\n";
md += "\n%%\n## Drawing\n```compressed-json\n" + compressed + "\n```\n%%\n";

const outPath = process.argv[3];
if (outPath) {
    fs.writeFileSync(outPath, md, "utf8");
    console.log("Written: " + outPath + " (" + fs.statSync(outPath).size + " bytes)");

    // Verify roundtrip
    const vmd = fs.readFileSync(outPath, "utf8");
    const vm = vmd.match(/```compressed-json\n([\s\S]+?)\n```/);
    if (!vm) { console.error("VERIFY FAILED: no compressed data found"); process.exit(1); }
    const vb = vm[1].replace(/\s/g, "");
    const dec = lzstring.decompressFromBase64(vb);
    const vj = JSON.parse(dec);
    let b = 0, u = 0;
    for (const el of vj.elements) {
        if (el.type === "arrow") {
            if (el.startBinding && el.endBinding) b++;
            else { u++; console.log("UNBOUND arrow: " + el.id); }
        }
    }
    console.log("Verify: " + vj.elements.length + " elements, " + b + " arrows bound" + (u ? ", " + u + " UNBOUND!" : ""));
} else {
    process.stdout.write(md);
}
