#!/usr/bin/env node
// Build the Social Proof Wall as an editable HyperFrames project from recorded post tiles.
// Usage: node scripts/build-wall.mjs --tiles ./tiles --out ./wall --title "Creators can't stop talking about [[Kite]]"
//        [--seconds 5.5] [--rows auto|1|2|3] [--bg black|white|#RRGGBB] [--grid on|off]
//        [--theme blue|mono|orange | --accent "#RRGGBB"] [--font smiley|inter|<font file>] [--order a.mp4,b.png,...]
// --tiles takes a folder (MP4/PNG/JPG/WebP, in name order) or a comma-separated list of files.
// Every tile keeps its own aspect ratio and is shown whole (never cropped). Render with:
//   npx hyperframes render ./wall --output wall.mp4 --fps 30 --quality high --resolution 1080p
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { args } from './lib/browser.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
// Fonts and GSAP: references/assets in this Skill, references/social-wall in the LaunchMotion library.
const assets = [path.join(root, 'references', 'assets'), path.join(root, '..', 'references', 'social-wall')].find((d) => fs.existsSync(path.join(d, 'gsap.min.js')));
const opt = args(process.argv.slice(2), ['help']);
if (opt.help || !opt.tiles || !opt.out) {
  console.log(fs.readFileSync(fileURLToPath(import.meta.url), 'utf8').split('\n').slice(1, 8).map((l) => l.replace(/^\/\/ ?/, '')).join('\n'));
  process.exit(opt.help ? 0 : 1);
}

const MEDIA = /\.(mp4|mov|webm|png|jpe?g|webp)$/i;
let files = fs.existsSync(opt.tiles) && fs.statSync(opt.tiles).isDirectory()
  ? fs.readdirSync(opt.tiles).filter((f) => MEDIA.test(f) && !/\.(probe|failed)\./.test(f)).sort().map((f) => path.join(opt.tiles, f))
  : opt.tiles.split(',').map((f) => f.trim()).filter(Boolean);
if (opt.order) files = opt.order.split(',').map((f) => files.find((x) => path.basename(x) === f.trim()) || f.trim());
files = files.map((f) => path.resolve(f));
for (const f of files) if (!fs.existsSync(f)) { console.error(`Missing tile: ${f}`); process.exit(1); }
if (files.length < 3) { console.error('A wall needs at least 3 tiles (8-12 looks best).'); process.exit(1); }

const seconds = Number(opt.seconds || 5.5);
const THEMES = { blue: ['#6E9BFF', '#2F6BFF'], mono: ['#9A9A9A', '#6B6A67'], orange: ['#FF8C4A', '#F37021'] };
const bgOpt = (opt.bg || 'black').toLowerCase();
const bg = bgOpt === 'black' ? '#000000' : bgOpt === 'white' ? '#FFFFFF' : bgOpt;
if (!/^#[0-9a-f]{6}$/i.test(bg)) { console.error('--bg takes black, white or #RRGGBB'); process.exit(1); }
const lum = (h) => { const [r, g, b] = [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16) / 255); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
const dark = lum(bg) < 0.5;
const accent = opt.accent || (THEMES[opt.theme || 'blue'] || THEMES.blue)[dark ? 0 : 1];
const grid = (opt.grid || 'on') !== 'off';
const ink = dark ? '#FFFFFF' : '#0B0B0F';
const line = dark ? 'rgba(255,255,255,0.055)' : 'rgba(15,23,42,0.045)';
const edge = dark ? 'rgba(255,255,255,0.14)' : 'rgba(15,23,42,0.12)';
const tileBg = dark ? '#000' : '#fff';

function size(file) {
  const out = execFileSync('ffprobe', ['-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height:format=duration', '-of', 'json', file]).toString();
  const j = JSON.parse(out);
  return { w: j.streams[0].width, h: j.streams[0].height, d: Number(j.format?.duration || 0) };
}
const tiles = files.map((f, i) => ({ file: f, ...size(f), video: /\.(mp4|mov|webm)$/i.test(f), name: `t${i}${path.extname(f).toLowerCase()}` }));
for (const t of tiles) if (t.video && t.d && t.d + 0.05 < seconds) console.warn(`Note: ${path.basename(t.file)} is ${t.d.toFixed(1)} s, shorter than the ${seconds} s wall; it will hold its last frame.`);

// Rows: balanced by total width, in the given order.
const rowCount = opt.rows && opt.rows !== 'auto' ? Number(opt.rows) : tiles.length <= 5 ? 1 : tiles.length <= 14 ? 2 : 3;
const H = rowCount === 1 ? 760 : 600;
const GAP = 26;
const width = (t) => Math.round(H * t.w / t.h);
const total = tiles.reduce((s, t) => s + width(t) + GAP, 0);
const rows = [[]];
let acc = 0;
for (const t of tiles) {
  const target = total / rowCount;
  if (acc > target * rows.length - width(t) / 2 && rows.length < rowCount) rows.push([]);
  rows[rows.length - 1].push(t);
  acc += width(t) + GAP;
}
const rowW = rows.map((r) => r.reduce((s, t) => s + width(t), 0) + GAP * (r.length - 1));
const W = Math.max(...rowW);
const WH = rows.length * H + (rows.length - 1) * GAP;

// Camera: the wall sits back in depth so it fills the stage, turned 18 -> 12 degrees and drifting in.
const hasTitle = opt.title !== undefined && String(opt.title).trim() !== '';
const stageTop = hasTitle ? 120 : 30;
const stageH = 1080 - stageTop - 30;
const P = 2600;
const fill = Math.min(1580 / W, (0.74 * stageH) / WH);
const z0 = Math.round(P / fill - P);
const cam = { r0: 18, r1: 12, x0: 60, x1: 20, z0: -z0, z1: -z0 + Math.round(z0 * 0.06) };

const out = path.resolve(opt.out);
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(path.join(out, 'assets'), { recursive: true });
fs.copyFileSync(path.join(assets, 'gsap.min.js'), path.join(out, 'assets', 'gsap.min.js'));
fs.copyFileSync(path.join(assets, 'inter.woff2'), path.join(out, 'assets', 'inter.woff2'));
let headFont = 'smiley-sans.woff2';
if (opt.font && !['smiley', 'inter'].includes(opt.font)) { headFont = `head${path.extname(opt.font)}`; fs.copyFileSync(opt.font, path.join(out, 'assets', headFont)); }
else if (opt.font !== 'inter') fs.copyFileSync(path.join(assets, 'smiley-sans.woff2'), path.join(out, 'assets', headFont));
for (const t of tiles) fs.copyFileSync(t.file, path.join(out, 'assets', t.name));

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const titleHtml = hasTitle ? esc(opt.title).replace(/\[\[(.+?)\]\]/g, '<span class="hl">$1</span>') : '';
const headFamily = opt.font === 'inter' ? 'Inter' : 'LMHead';

let body = hasTitle ? `<div class="title" id="t">${titleHtml}</div>\n` : '';
body += `<div id="stage" style="top:${stageTop}px;height:${stageH}px">\n<div id="wall" style="left:${((1920 - W) / 2).toFixed(1)}px;top:${((stageH - WH) / 2).toFixed(1)}px;width:${W}px;height:${WH}px">\n`;
let k = 0;
rows.forEach((r, ri) => {
  let x = (W - rowW[ri]) / 2;
  const y = ri * (H + GAP);
  for (const t of r) {
    const w = width(t);
    const media = t.video
      ? `<video id="v${k}" class="clip" src="assets/${t.name}" data-start="0" data-duration="${seconds}" data-track-index="${k}" muted playsinline></video>`
      : `<img src="assets/${t.name}" alt="">`;
    body += `  <div class="tile" style="left:${x.toFixed(1)}px;top:${y}px;width:${w}px;height:${H}px">${media}</div>\n`;
    x += w + GAP;
    k += 1;
  }
});
body += '</div>\n</div>';

const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Social Proof Wall</title>
<style>
@font-face{font-family:'LMHead';src:url('assets/${opt.font === 'inter' ? 'inter.woff2' : headFont}');font-display:block}
@font-face{font-family:'Inter';src:url('assets/inter.woff2');font-weight:100 900;font-display:block}
:root{--bg:${bg};--ink:${ink};--accent:${accent};--line:${line};--edge:${edge};--tile:${tileBg}}
*{box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:var(--bg)}
#composition{position:relative;width:1920px;height:1080px;overflow:hidden;background:var(--bg);color:var(--ink);font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}
#grid{position:absolute;inset:0;${grid ? 'background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);background-size:48px 48px;background-position:center;' : ''}}
.title{position:absolute;left:0;right:0;top:46px;text-align:center;font-family:'${headFamily}','Inter',sans-serif;font-size:68px;line-height:1.08;letter-spacing:-0.01em;white-space:nowrap}
.title .hl{color:var(--accent)}
#stage{position:absolute;left:0;width:1920px;perspective:${P}px;perspective-origin:50% 45%}
#wall{position:absolute;transform-style:preserve-3d;transform-origin:50% 50%}
.tile{position:absolute;border-radius:18px;overflow:hidden;border:1px solid var(--edge);background:var(--tile)}
.tile video,.tile img{display:block;width:100%;height:100%;object-fit:contain;background:var(--tile)}
</style></head>
<body>
<div id="composition" data-composition-id="social-proof-wall" data-start="0" data-duration="${seconds}" data-width="1920" data-height="1080" data-fps="30">
<div id="grid"></div>
${body}
</div>
<script src="assets/gsap.min.js"></script>
<script>
const tl = gsap.timeline({ paused: true, defaults: { ease: 'power3.out' } });
${hasTitle ? "tl.from('#t', { opacity: 0, y: 10, duration: 0.3 }, 0);" : ''}
tl.fromTo('#wall', { rotationY: ${cam.r0}, x: ${cam.x0}, z: ${cam.z0} }, { rotationY: ${cam.r1}, x: ${cam.x1}, z: ${cam.z1}, duration: ${seconds}, ease: 'none' }, 0);
tl.from('.tile', { opacity: 0, y: 50, duration: 0.45, stagger: 0.035 }, 0);
tl.set({}, {}, ${seconds});
window.__timelines = window.__timelines || {};
window.__timelines['social-proof-wall'] = tl;
</script>
</body></html>
`;
fs.writeFileSync(path.join(out, 'index.html'), html);
fs.writeFileSync(path.join(out, 'hyperframes.json'), JSON.stringify({ $schema: 'https://hyperframes.heygen.com/schema/hyperframes.json', paths: { assets: 'assets' }, media: { autoProxy: false } }, null, 2) + '\n');
fs.writeFileSync(path.join(out, 'package.json'), JSON.stringify({ name: 'social-proof-wall', private: true, type: 'module' }, null, 2) + '\n');
console.log(`${out}\n${tiles.length} tiles in ${rows.length} row(s), ${seconds} s. Render: npx hyperframes render ${path.relative(process.cwd(), out) || '.'} --output wall.mp4 --fps 30 --quality high --resolution 1080p`);
