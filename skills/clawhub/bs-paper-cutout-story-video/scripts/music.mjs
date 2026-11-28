#!/usr/bin/env node
// Generates an instrumental music bed through Skillry (default, --provider skillry),
// FAL (--provider fal, FAL_KEY), or ElevenLabs direct (--provider elevenlabs).
//
//   node music.mjs --seconds 58 --out assets/music.mp3 [--provider auto|skillry|fal|elevenlabs] [--prompt "..."]
import fs from 'node:fs';
import path from 'node:path';
import { randomUUID } from 'node:crypto';
import { Ledger, inputHash, submit, waitFor, download } from './lib/fal.mjs';
import { resolveProvider, skillryGenerate } from './lib/skillry-media.mjs';

const DEFAULT_PROMPT = "Warm, playful acoustic underscore for a paper-cutout storybook animation. Ukulele and nylon guitar picking, glockenspiel and soft marimba melody, light hand claps and shaker, gentle upright bass, a hint of whistling. Bright and cosy, around 100 BPM, steady and uncluttered, a small lift two thirds in, then a clean resolved ending on a soft final chord. Instrumental, no vocals, no heavy drums, no risers.";

const args = parseArgs(process.argv.slice(2));
if (!args.out) {
  console.error('Usage: node music.mjs [--provider auto|skillry|fal|elevenlabs] --seconds 58 --out music.mp3 [--prompt "..."]');
  process.exit(2);
}
const OUT = path.resolve(args.out);
const seconds = Math.max(10, Math.min(300, Number(args.seconds || 60)));
const prompt = String(args.prompt || DEFAULT_PROMPT);
const provider = resolveProvider(args.provider, { allowElevenLabs: true });
fs.mkdirSync(path.dirname(OUT), { recursive: true });

if (provider === 'skillry') {
  const model = 'eleven-music-v2.5';
  const ledger = new Ledger(`${OUT}.fal.json`);
  const hash = inputHash('skillry:' + model, { prompt, duration: seconds });
  const existing = ledger.get('music');
  if (existing && existing.hash === hash && existing.done && fs.existsSync(OUT) && !args.resubmit) {
    console.log(`Reusing ${OUT}`);
    process.exit(0);
  }
  const requestId = (!existing || existing.hash !== hash || args.resubmit) ? randomUUID() : (existing.requestId || randomUUID());
  ledger.set('music', { provider: 'skillry', model, hash, requestId, done: false });
  const res = await skillryGenerate({
    model,
    prompt,
    duration: seconds,
    outputPath: OUT,
    requestId,
    stepLabel: 'music',
  });
  ledger.set('music', { done: true, file: OUT, jobId: res.jobId, runId: res.runId, points: res.points });
  console.log(`Wrote ${OUT} (${(res.bytes.length / 1024).toFixed(0)} KB) with Skillry.`);
} else if (provider === 'elevenlabs') {
  const key = process.env.ELEVENLABS_API_KEY || process.env.XI_API_KEY;
  if (!key) {
    console.error('ELEVENLABS_API_KEY is not set. Export it, or use --provider skillry or --provider fal.');
    process.exit(1);
  }
  const res = await fetch('https://api.elevenlabs.io/v1/music?output_format=mp3_44100_192', {
    method: 'POST',
    headers: { 'xi-api-key': key, 'Content-Type': 'application/json', Accept: 'audio/mpeg' },
    body: JSON.stringify({ prompt, music_length_ms: Math.round(seconds * 1000), model_id: 'music_v1', force_instrumental: true }),
  });
  if (!res.ok) {
    console.error(`ElevenLabs ${res.status}: ${(await res.text()).slice(0, 500)}`);
    process.exit(1);
  }
  const buf = Buffer.from(await res.arrayBuffer());
  fs.writeFileSync(OUT, buf);
  const rid = res.headers.get('request-id') || res.headers.get('x-request-id') || '';
  console.log(`Wrote ${OUT} (${(buf.length / 1024).toFixed(0)} KB)${rid ? `  request ${rid}` : ''}`);
} else if (provider === 'fal') {
  const model = String(args.model || 'elevenlabs/music/v2.5');
  const input = { prompt, music_length_ms: Math.round(seconds * 1000), force_instrumental: true, output_format: 'mp3_48000_192' };
  const ledger = new Ledger(`${OUT}.fal.json`);
  const hash = inputHash(model, input);
  let job = ledger.get('music');
  if (!job || job.hash !== hash || args.resubmit) {
    const sub = await submit(model, input);
    job = { model, hash, ...sub };
    ledger.set('music', job);
    console.log(`Submitted ${model}  request ${sub.requestId}`);
  } else console.log(`Polling existing request ${job.requestId}`);
  const result = await waitFor(job, { onTick: (st) => process.stdout.write(`\r  ${st.status}   `) });
  process.stdout.write('\n');
  const url = (result.audio && result.audio.url) || (result.audio_file && result.audio_file.url);
  if (!url) throw new Error(`no audio url in result: ${JSON.stringify(result).slice(0, 300)}`);
  const bytes = await download(url, OUT);
  ledger.set('music', { done: true, file: OUT });
  console.log(`Wrote ${OUT} (${(bytes / 1024).toFixed(0)} KB)  request ${job.requestId}`);
} else {
  console.error('--provider must be auto, skillry, fal, or elevenlabs.');
  process.exit(2);
}

function parseArgs(list) {
  const o = {};
  for (let i = 0; i < list.length; i += 1) {
    if (!list[i].startsWith('--')) continue;
    const k = list[i].slice(2);
    const v = list[i + 1];
    if (v === undefined || v.startsWith('--')) o[k] = true;
    else {
      o[k] = v;
      i += 1;
    }
  }
  return o;
}
