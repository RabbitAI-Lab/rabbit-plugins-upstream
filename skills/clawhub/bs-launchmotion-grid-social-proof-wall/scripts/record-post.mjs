#!/usr/bin/env node
// Record one public social post as a wall tile.
// Usage: node scripts/record-post.mjs --url <post url> --out tiles/name.mp4 [--start 2] [--seconds 6] [--probe]
//   --probe       only write <out>.probe.jpg: the post at one frame per second with timestamps, so you
//                 can pick the second where the product appears. Prints the video duration.
//   --start       second of the post's video to start from (default 1).
//   --seconds     tile length (default 6). Use at least the wall length + 0.5 s.
//   --scheme      dark (default) or light: the platform theme, matching a black or white wall.
// Video posts: the main video is paused and stepped 1/30 s at a time; each step screenshots the post
// area (video, author, counts, caption) and FFmpeg joins the frames into a 30 fps MP4, so the motion
// matches the original speed and never drops frames. Posts without video become a still PNG next to
// --out (same name, .png). Picture only, no sound. Overlays (cookie banners, sign-in walls, onboarding
// tips) are removed before capture.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { openBrowser, args, platformOf } from './lib/browser.mjs';

const opt = args(process.argv.slice(2), ['probe']);
if (!opt.url || !opt.out) {
  console.error('Usage: node scripts/record-post.mjs --url <post url> --out tiles/name.mp4 [--start 1] [--seconds 6] [--scheme dark|light] [--probe]');
  process.exit(1);
}
const FPS = 30;
const url = opt.url;
const out = path.resolve(opt.out.endsWith('.mp4') ? opt.out : `${opt.out}.mp4`);
const start = Number(opt.start ?? 1);
const secs = Number(opt.seconds ?? 6);
const platform = platformOf(url);
fs.mkdirSync(path.dirname(out), { recursive: true });

const vertical = platform === 'youtube';
const { browser, page } = await openBrowser({ width: vertical ? 900 : 1280, height: 860, scale: 2, colorScheme: opt.scheme === 'light' ? 'light' : 'dark' });
await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(8000);

for (const label of ['Got it', 'Not now', 'Close', 'Decline optional cookies', 'Reject all', 'Only allow essential cookies', 'Accept all']) {
  const b = page.getByText(label, { exact: true }).first();
  if (await b.isVisible().catch(() => false)) { await b.click().catch(() => {}); await page.waitForTimeout(600); }
}

async function clearOverlays() {
  await page.evaluate(() => {
    document.querySelectorAll('[role=dialog],[class*=Modal],[class*=modal],[id*=login],[data-testid=sheetDialog],[data-testid=BottomBar],#credential_picker_container,tp-yt-iron-overlay-backdrop').forEach((e) => {
      if (!e.querySelector('video') || e.getAttribute('role') === 'dialog' && !e.closest('article')) e.remove();
    });
    document.documentElement.style.overflow = 'auto';
    document.body.style.overflow = 'auto';
    for (const e of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(e);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      const r = e.getBoundingClientRect();
      if (e.querySelector('video') || e.closest('article')) continue;
      if ((r.width > innerWidth * 0.8 && r.height > innerHeight * 0.8) || (r.width > innerWidth * 0.6 && r.top > innerHeight * 0.6)) e.remove();
    }
    for (const e of document.querySelectorAll('div,section')) {
      if (e.children.length < 8 && /Scroll, use the|Got it/.test(e.innerText || '') && e.getBoundingClientRect().width > 300) {
        (e.closest('[class*=Mask],[class*=Guide],[class*=Overlay],[class*=Modal]') || e).remove();
      }
    }
    // Paused-video play badges (Instagram, X) would sit on every frame: hide small elements
    // centred on the main video.
    const main = [...document.querySelectorAll('video')].sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height)[0];
    if (main) {
      const vr = main.getBoundingClientRect();
      const cx = vr.left + vr.width / 2; const cy = vr.top + vr.height / 2;
      const badges = /instagram\.com$/.test(location.hostname) ? 'body *' : 'svg, [role=button], [aria-label*="Play" i], [data-testid=playButton]';
      for (const e of document.querySelectorAll(badges)) {
        if (e.contains(main)) continue;
        const r = e.getBoundingClientRect();
        if (r.width < 24 || r.width > 200 || r.height > 200) continue;
        if (Math.abs(r.left + r.width / 2 - cx) < vr.width * 0.12 && Math.abs(r.top + r.height / 2 - cy) < vr.height * 0.12) e.style.visibility = 'hidden';
      }
      // X draws a control bar over a paused video.
      if (/(^|\.)(x|twitter)\.com$/.test(location.hostname)) {
        const player = main.closest('[data-testid=videoPlayer]') || main.parentElement;
        for (const e of player.querySelectorAll('*')) {
          if (e.contains(main) || e === main) continue;
          const r = e.getBoundingClientRect();
          if (r.height < 90 && r.width > vr.width * 0.5 && r.bottom > vr.bottom - 90) e.style.visibility = 'hidden';
        }
      }
    }
    for (const e of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(e);
      if ((cs.filter.includes('brightness') || cs.filter.includes('blur')) && e.querySelector('video, article, img')) e.style.filter = 'none';
    }
  });
}
await clearOverlays();
if (platform === 'x' || platform === 'threads') {
  // Text-led posts: drop the sticky top bar and give the post a small margin above it.
  await page.evaluate(() => {
    for (const e of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(e);
      if ((cs.position === 'sticky' || cs.position === 'fixed') && e.getBoundingClientRect().top < 90 && e.getBoundingClientRect().height < 140 && !e.querySelector('article, video')) e.style.visibility = 'hidden';
    }
    const art = document.querySelector('article[data-testid=tweet]') || document.querySelector('[data-pressable-container]') || document.querySelector('article');
    if (art) window.scrollTo(0, art.getBoundingClientRect().top + window.scrollY - 16);
  });
  await page.waitForTimeout(800);
}

const info = await page.evaluate(() => {
  const v = [...document.querySelectorAll('video')].filter((x) => x.getBoundingClientRect().height > 120).sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height)[0];
  return v ? { video: true, duration: v.duration, ready: v.readyState, title: document.title.slice(0, 100) } : { video: false, title: document.title.slice(0, 100) };
});

// The post area: video plus the action rail and caption where the platform shows them.
async function postRect() {
  return page.evaluate((plat) => {
    const vids = [...document.querySelectorAll('video')].filter((x) => x.getBoundingClientRect().height > 120);
    const v = vids.sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height)[0];
    const fit = (r) => {
      const x = Math.max(0, r.left); const y = Math.max(0, r.top);
      return { x, y, width: Math.min(innerWidth, r.right) - x, height: Math.min(innerHeight, r.bottom) - y };
    };
    const union = (a, b) => ({ left: Math.min(a.left, b.left), top: Math.min(a.top, b.top), right: Math.max(a.right, b.right), bottom: Math.max(a.bottom, b.bottom) });
    if (plat === 'youtube' && v) {
      const reel = v.closest('ytd-reel-video-renderer, ytm-reel-player-overlay-renderer, #shorts-player') || v;
      let r = reel.getBoundingClientRect();
      const actions = document.querySelector('ytd-reel-video-renderer[is-active] #actions, #actions.ytd-reel-video-renderer');
      if (actions) r = union(r, actions.getBoundingClientRect());
      return fit(r);
    }
    if (plat === 'instagram' && v) {
      const vr = v.getBoundingClientRect();
      const like = document.querySelector('svg[aria-label="Like"]');
      let r = vr;
      if (like) {
        const side = like.closest('section, div').parentElement.getBoundingClientRect();
        r = { left: vr.left, top: vr.top, right: Math.max(vr.right, side.right), bottom: vr.bottom };
      }
      return fit(r);
    }
    if (plat === 'threads') {
      const box = (v || document.querySelector('[data-pressable-container]'))?.closest('[data-pressable-container]');
      if (box) return fit(box.getBoundingClientRect());
    }
    if (plat === 'x') {
      const art = (v && v.closest('article')) || document.querySelector('article[data-testid=tweet]') || document.querySelector('article');
      if (art) return fit(art.getBoundingClientRect());
    }
    if (v) {
      const art = v.closest('article');
      let el = art || v;
      if (!art) {
        let c = v;
        while (c.parentElement && c.parentElement.getBoundingClientRect().height <= innerHeight && c.parentElement.getBoundingClientRect().width < innerWidth * 0.75) c = c.parentElement;
        el = c;
      }
      let r = el.getBoundingClientRect();
      const act = document.querySelector('[data-e2e=like-icon]');
      if (act) r = union(r, { ...act.closest('section,div').getBoundingClientRect().toJSON(), right: act.closest('section,div').getBoundingClientRect().right + 8 });
      return fit(r);
    }
    const art = document.querySelector('article') || document.querySelector('main');
    return art ? fit(art.getBoundingClientRect()) : null;
  }, platform);
}

async function seek(t) {
  await page.evaluate(async (time) => {
    const v = [...document.querySelectorAll('video')].filter((x) => x.getBoundingClientRect().height > 120).sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height)[0];
    if (!v) return;
    v.muted = true;
    v.pause();
    const d = Number.isFinite(v.duration) && v.duration > 0 ? v.duration : time + 1;
    const target = time % d;
    await new Promise((res) => {
      const done = () => { v.removeEventListener('seeked', done); res(); };
      v.addEventListener('seeked', done);
      v.currentTime = target;
      setTimeout(res, 1500);
    });
  }, t);
}

const gone = await page.evaluate(() => /content (is|isn't) (unavailable|available)|page isn't available|video (is )?(currently )?unavailable|this post (is unavailable|was deleted)|hmm\.\.\.this page doesn't exist/i.test(document.title + ' ' + document.body.innerText.slice(0, 2000)));
if (gone && !info.video) {
  await browser.close();
  console.error(`The post is unavailable (${info.title}). Drop it from the wall.`);
  process.exit(2);
}
const clip = await postRect();
if (!clip || clip.width < 80 || clip.height < 80) {
  await page.screenshot({ path: out.replace(/\.mp4$/, '.failed.png') });
  await browser.close();
  console.error(`Could not find the post on the page (${info.title}). See ${out.replace(/\.mp4$/, '.failed.png')}; record it another way or drop it.`);
  process.exit(2);
}
console.error(JSON.stringify({ platform, ...info, clip }));

if (!info.video) {
  const still = out.replace(/\.mp4$/, '.png');
  await page.screenshot({ path: still, clip });
  await browser.close();
  console.log(still);
  process.exit(0);
}

const tmp = `${out}.frames`;
fs.rmSync(tmp, { recursive: true, force: true });
fs.mkdirSync(tmp, { recursive: true });
try {
  if (opt.probe) {
    const n = Math.min(30, Math.max(1, Math.floor(info.duration || 10)));
    for (let i = 0; i < n; i += 1) {
      await seek(i);
      await page.screenshot({ path: path.join(tmp, `${String(i).padStart(3, '0')}.jpg`), type: 'jpeg', quality: 80, clip });
    }
    const cols = Math.min(6, n);
    const rows = Math.ceil(n / cols);
    const sheet = out.replace(/\.mp4$/, '.probe.jpg');
    execFileSync('ffmpeg', ['-y', '-v', 'error', '-framerate', '1', '-i', path.join(tmp, '%03d.jpg'),
      '-vf', `scale=-2:420,drawtext=text='%{n}s':x=12:y=12:fontsize=34:fontcolor=white:box=1:boxcolor=black@0.6:boxborderw=8,tile=${cols}x${rows}:padding=8:color=black`,
      '-frames:v', '1', sheet]);
    console.log(sheet);
  } else {
    const n = Math.round(secs * FPS);
    for (let i = 0; i < n; i += 1) {
      if (i % 30 === 0) await clearOverlays();
      await seek(start + i / FPS);
      await page.screenshot({ path: path.join(tmp, `${String(i).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 94, clip });
    }
    execFileSync('ffmpeg', ['-y', '-v', 'error', '-framerate', String(FPS), '-i', path.join(tmp, '%05d.jpg'),
      '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out]);
    console.log(out);
  }
} finally {
  fs.rmSync(tmp, { recursive: true, force: true });
  // Chrome sometimes never acknowledges close after long video sessions; do not wait on it.
  await Promise.race([browser.close().catch(() => {}), new Promise((r) => setTimeout(r, 5000))]);
}
process.exit(0);
