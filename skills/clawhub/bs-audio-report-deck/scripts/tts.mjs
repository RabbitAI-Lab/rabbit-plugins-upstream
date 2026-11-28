#!/usr/bin/env node
/**
 * Voice every page's narration with ElevenLabs Multilingual v2.
 *
 *   node scripts/tts.mjs providers [--choose elevenlabs|heygen]
 *   node scripts/tts.mjs voices   [--lang zh]
 *   node scripts/tts.mjs estimate --narration narration.json --out-dir audio [--voice <name|id>]
 *   node scripts/tts.mjs generate --narration narration.json --out-dir audio --yes
 *        [--voice <name|id>] [--speed 1] [--lang zh] [--pronunciations pronunciations.json] [--only id1,id2]
 *        [--provider elevenlabs|heygen|fal] [--model eleven_v4]
 *
 * Providers, each with its own key and nothing else read:
 *   elevenlabs (default)  ELEVENLABS_API_KEY  Multilingual v2 by default; --model picks another
 *                                             ElevenLabs model (eleven_v4, eleven_v4_turbo, ...)
 *   heygen                HEYGEN_API_KEY      HeyGen Voice 1.0 with the workspace's own
 *                                             cloned voices or HeyGen's public voices
 *   fal                   FAL_KEY             ElevenLabs Multilingual v2 through FAL,
 *                                             $0.10 per 1,000 characters
 * Generation is paid, so `generate` refuses to run without --yes: show the
 * estimate and get the user's yes. Without --provider the provider the user
 * chose with `providers --choose` (saved in ~/.skillry/audio-ppt/preferences.json)
 * is used; the voice last used for that provider and language is the default. HeyGen returns WAV; it is converted to MP3
 * when ffmpeg is installed, otherwise kept as WAV.
 *
 * Each page is keyed by provider, voice, speed, language and text, so an
 * unchanged page is never voiced twice. A failed request is not retried; a
 * FAL request id is saved before waiting so an interrupted run resumes it.
 */
import { execFileSync } from 'node:child_process';
import { createHash, randomUUID } from 'node:crypto';
import { applyAudioSpeed, hasSkillryAuth, resolveProvider as resolveSkillryProvider, skillryGenerate } from './lib/skillry-media.mjs';
import { existsSync, mkdirSync, readFileSync, renameSync, writeFileSync } from 'node:fs';
import { homedir } from 'node:os';
import { dirname, join, resolve } from 'node:path';

const ELEVEN_API = 'https://api.elevenlabs.io';
const DEFAULT_ELEVEN_MODEL = 'eleven_multilingual_v2';
const FAL_MODEL = 'fal-ai/elevenlabs/tts/multilingual-v2';
const FAL_USD_PER_1000_CHARS = 0.1;
const HEYGEN_API = 'https://api.heygen.com';
const HEYGEN_MODEL = 'heygen-voice-1';
const HEYGEN_MAX_CHARS = 5000;
const HEYGEN_RETRY_STATUSES = [429, 502, 503, 504];
const HEYGEN_FATAL_CODES = ['voice_expired', 'voice_not_found', 'voice_not_ready', 'voice_training_failed', 'invalid_parameter'];
const CONCURRENCY = 3;
const POLL_MS = 1500;
const POLL_LIMIT_MS = 5 * 60 * 1000;
// Premade ElevenLabs voices: present in every account and speak every supported language.
const PREMADE = {
  Sarah: 'EXAVITQu4vr4xnSDxMaL',
  Alice: 'Xb7hH8MSUJpSbSDYk0k2',
  Matilda: 'XrExE9yKIg1WjnnlVkGX',
  Laura: 'FGY2WhTYpPnrIDTdsKH5',
  Jessica: 'cgSgspJ2msm6clMCkdW9',
  Lily: 'pFZP5JQG7iQjIQuC4Bku',
  Bella: 'hpp4J3VqNfWAUOO0d1Us',
  Brian: 'nPczCjzI2devNBz1zQrb',
  Daniel: 'onwK4e9ZLuTAKqWW03F9',
  George: 'JBFqnCBsd6RMkjVDRZzb',
  Eric: 'cjVigY5qzO86Huf0OWal',
  Roger: 'CwhRBWXzGAHq8TQ4Fs17',
  Chris: 'iP95p4xoKVk53GoZ742B',
  Will: 'bIHbv24MWmeRgasZH58o',
  Liam: 'TX3LPaxmHKxFdv7VOQHJ',
  Charlie: 'IKne3meq5aSn9XLyUdCD',
  Callum: 'N2lVS1w4EtoT3dr4eOWO',
  Bill: 'pqHfZKP75CvOlQylNhV4',
  River: 'SAz9YHcvj6GT2YYXdXww',
};
const FALLBACK_VOICE = 'Sarah';
// Spoken forms for terms a voice tends to misread; applied to the audio text only.
const DEFAULT_PRONUNCIATIONS = {
  zh: { Skillry: '\u65af\u5947\u5c14\u745e', Claude: '\u514b\u52b3\u5fb7', Codex: '\u79d1\u5fb7\u514b\u65af' },
  'zh-tw': { Skillry: '\u65af\u5947\u723e\u745e', Claude: '\u514b\u52de\u5fb7', Codex: '\u79d1\u5fb7\u514b\u65af' },
};

const command = process.argv[2];
const flags = parseFlags(process.argv.slice(3));
const PREFS_PATH = join(homedir(), '.skillry', 'audio-ppt', 'preferences.json');
const PROVIDERS = {
  skillry: { name: 'Skillry API Key (Default)', env: 'SKILLRY_API_KEY' },
  elevenlabs: { name: 'ElevenLabs', env: 'ELEVENLABS_API_KEY' },
  heygen: { name: 'HeyGen Voice', env: 'HEYGEN_API_KEY' },
  fal: { name: 'ElevenLabs via FAL', env: 'FAL_KEY' },
};
const prefs = readJson(PREFS_PATH) || {};
const provider = flags.provider ? String(flags.provider) : (prefs.voiceProvider || resolveSkillryProvider('auto', { allowElevenLabs: true, allowHeygen: true }));
if (!['skillry', 'elevenlabs', 'heygen', 'fal'].includes(provider)) fail('--provider must be skillry, elevenlabs, heygen or fal.');
const HAS_FFMPEG = hasCommand('ffmpeg');
// ElevenLabs model, e.g. eleven_v4 or eleven_v4_turbo; part of each page's cache key.
const ELEVEN_MODEL = String(flags.model || DEFAULT_ELEVEN_MODEL);
if (flags.model && (provider !== 'elevenlabs' || !/^eleven_[a-z0-9_]+$/.test(ELEVEN_MODEL))) {
  fail('--model takes an ElevenLabs model ID such as eleven_v4, and only with the ElevenLabs provider.');
}

try {
  if (command === 'providers') providersCommand();
  else if (command === 'voices') await listVoices();
  else if (command === 'estimate') await estimate();
  else if (command === 'generate') await generate();
  else fail('Usage: node tts.mjs <providers|voices|estimate|generate> [flags]');
} catch (error) {
  fail(error instanceof Error ? error.message : String(error));
}

// ---------------------------------------------------------------- voices

/** Which voice services are ready (key present, never shown) and which one the user chose last. */
function providersCommand() {
  if (flags.choose) {
    const chosen = String(flags.choose);
    if (!['skillry', 'elevenlabs', 'heygen', 'fal'].includes(chosen)) fail('--choose must be skillry, elevenlabs, heygen or fal.');
    savePrefs({ voiceProvider: chosen });
  }
  const current = readJson(PREFS_PATH) || {};
  console.log(
    JSON.stringify(
      {
        lastUsed: current.voiceProvider || null,
        providers: ['skillry', 'elevenlabs', 'heygen'].map((id) => ({
          id,
          name: PROVIDERS[id].name,
          keyEnv: PROVIDERS[id].env,
          keySet: id === 'skillry' ? hasSkillryAuth() : Boolean(process.env[PROVIDERS[id].env]),
          lastUsed: (current.voiceProvider || 'skillry') === id,
        })),
        falKeySet: Boolean(process.env.FAL_KEY),
      },
      null,
      2
    )
  );
}

function savePrefs(patch) {
  const current = readJson(PREFS_PATH) || {};
  mkdirSync(dirname(PREFS_PATH), { recursive: true });
  writeJsonAtomic(PREFS_PATH, { ...current, ...patch, updatedAt: new Date().toISOString() });
}

function savedVoice(lang) {
  return (readJson(PREFS_PATH) || {}).voices?.[`${provider}:${lang}`] || null;
}

async function accountVoices() {
  const key = credential();
  const data = await elevenJson('/v1/voices?page_size=100', key);
  return (data.voices || []).map((voice) => ({
    id: voice.voice_id,
    name: voice.name,
    category: voice.category,
    languages: [...new Set((voice.verified_languages || []).map((item) => item.language))],
    primary: voice.verified_languages?.[0]?.language || null,
  }));
}

async function heygenVoices() {
  const key = credential();
  const all = [];
  for (const type of ['private', 'public']) {
    let token = null;
    do {
      const query = new URLSearchParams({ type, limit: '100' });
      if (token) query.set('token', token);
      const page = await heygenJson(`/v3/models/audio/voices?${query}`, key);
      for (const voice of page.data || []) {
        if (voice.status === 'ACTIVE') all.push({ id: voice.voice_id, name: voice.name, mode: voice.mode, language: voice.language, own: type === 'private' });
      }
      token = page.has_more ? page.next_token : null;
    } while (token);
  }
  return all;
}

async function listVoices() {
  if (provider === 'heygen') {
    const code = flags.lang ? languageCode(String(flags.lang).toLowerCase()) : null;
    const voices = await heygenVoices();
    const own = voices.filter((voice) => voice.own);
    console.log(own.length ? 'Your workspace voices (cloned):' : 'No cloned voices in this HeyGen workspace yet.');
    for (const voice of own) console.log(`  ${voice.name}  ${voice.id}  (${voice.mode}; ${voice.language || 'any language'})`);
    console.log('\nHeyGen public voices:');
    for (const voice of voices.filter((item) => !item.own)) {
      console.log(`  ${voice.name}  ${voice.id}  (primary ${voice.language || '?'}${code && voice.language !== code ? `; also speaks ${code}` : ''})`);
    }
    return;
  }
  if (provider === 'skillry' || provider === 'fal') {
    console.log(Object.keys(PREMADE).join('\n'));
    console.log(
      provider === 'skillry'
        ? '\nSkillry accepts these premade ElevenLabs names (or any 20-character voice ID); every one speaks all supported languages.'
        : '\nFAL accepts these premade names; every one speaks all supported languages.'
    );
    return;
  }
  const code = flags.lang ? languageCode(String(flags.lang).toLowerCase()) : null;
  const voices = await accountVoices();
  const native = code ? voices.filter((voice) => voice.primary === code) : [];
  const rest = voices.filter((voice) => !native.includes(voice));
  if (native.length) {
    console.log(`Native ${code} voices:`);
    for (const voice of native) console.log(`  ${voice.name}  ${voice.id}  (${voice.category})`);
    console.log('\nOther voices (all speak every supported language):');
  }
  for (const voice of rest) console.log(`  ${voice.name}  ${voice.id}  (${voice.category}; ${voice.languages.slice(0, 5).join(', ') || 'multilingual'})`);
}

/** --voice may be a voice ID, a premade name or the start of an account voice name. */
async function resolveVoice(lang) {
  const remembered = flags.voice ? null : savedVoice(lang);
  const wanted = flags.voice ? String(flags.voice).trim() : remembered?.id || '';
  if (provider === 'skillry') {
    if (/^[A-Za-z0-9]{20}$/.test(wanted)) return { id: wanted, name: wanted, auto: false };
    const premade = Object.keys(PREMADE).find((n) => n.toLowerCase() === wanted.toLowerCase());
    const pick = premade || FALLBACK_VOICE;
    return { id: PREMADE[pick], name: pick, auto: !premade };
  }
  if (provider === 'fal') {
    const name = wanted || FALLBACK_VOICE;
    return { id: name, name, auto: !wanted };
  }
  if (provider === 'heygen') {
    const voices = await heygenVoices();
    if (wanted) {
      const match =
        voices.find((voice) => voice.id === wanted) ||
        voices.find((voice) => voice.name.toLowerCase().startsWith(wanted.toLowerCase()));
      if (!match) throw new Error(`No HeyGen voice named "${wanted}". Run "voices --provider heygen" to see the choices.`);
      return { id: match.id, name: match.name, mode: match.mode, auto: false };
    }
    // Prefer the user's own clone in this language, then any own clone, then a public voice.
    const code = languageCode(lang);
    const pick =
      voices.find((voice) => voice.own && voice.language === code) ||
      voices.find((voice) => voice.own) ||
      voices.find((voice) => !voice.own && voice.language === code) ||
      voices.find((voice) => !voice.own);
    if (!pick) throw new Error('This HeyGen workspace has no usable voice.');
    return { id: pick.id, name: pick.name, mode: pick.mode, auto: true };
  }
  if (/^[A-Za-z0-9]{20}$/.test(wanted)) return { id: wanted, name: wanted, auto: false };
  const premade = Object.keys(PREMADE).find((name) => name.toLowerCase() === wanted.toLowerCase());
  if (premade) return { id: PREMADE[premade], name: premade, auto: false };
  let voices = [];
  try {
    voices = await accountVoices();
  } catch (error) {
    if (error.fatal) throw error;
  }
  if (wanted) {
    const match = voices.find((voice) => voice.name.toLowerCase().startsWith(wanted.toLowerCase()));
    if (!match) throw new Error(`No voice named "${wanted}". Run "voices" to see the choices.`);
    return { id: match.id, name: match.name, auto: false };
  }
  const code = languageCode(lang);
  const native = voices.find((voice) => voice.primary === code && voice.category !== 'generated');
  if (native && code !== 'en') return { id: native.id, name: native.name, auto: true };
  return { id: PREMADE[FALLBACK_VOICE], name: FALLBACK_VOICE, auto: true };
}

// ---------------------------------------------------------------- planning

async function plan() {
  const narrationPath = requiredFlag('narration');
  const outDir = resolve(requiredFlag('out-dir'));
  const narration = JSON.parse(readFileSync(narrationPath, 'utf8'));
  const lang = String(flags.lang || narration.lang || 'en').toLowerCase();
  const voice = await resolveVoice(lang);
  const remembered = flags.voice ? null : savedVoice(lang);
  if (remembered && remembered.id === voice.id) Object.assign(voice, { name: remembered.name || voice.name, auto: false, lastUsed: true });
  const speed = Number(flags.speed || 1);
  if (!(speed >= 0.7 && speed <= 1.2)) fail('--speed must be between 0.7 and 1.2.');
  const only = flags.only ? new Set(String(flags.only).split(',')) : null;
  const pronunciations = loadPronunciations(lang);
  const pages = narration.slides.filter((page) => page.text?.trim() && (!only || only.has(page.id)));
  const manifestPath = join(outDir, 'manifest.json');
  const manifest = readJson(manifestPath) || { schemaVersion: 1, slides: {} };
  const model = provider === 'skillry' ? 'eleven-v4' : provider === 'fal' ? FAL_MODEL : provider === 'heygen' ? HEYGEN_MODEL : ELEVEN_MODEL;
  const extension = provider === 'heygen' && !HAS_FFMPEG ? 'wav' : 'mp3';
  const items = pages.map((page, index) => {
    const spoken = applyPronunciations(page.text.trim(), pronunciations);
    const key = createHash('sha256')
      .update(JSON.stringify([model, voice.id, speed, lang, spoken]))
      .digest('hex')
      .slice(0, 16);
    if (provider === 'heygen' && spoken.length > HEYGEN_MAX_CHARS) {
      fail(`Page ${page.id} has ${spoken.length} characters; HeyGen accepts at most ${HEYGEN_MAX_CHARS}. Split the page.`);
    }
    const file = `${safeId(page.id)}-${key}.${extension}`;
    return {
      id: page.id,
      spoken,
      textHash: page.hash,
      key,
      file,
      cached: existsSync(join(outDir, file)),
      previousText: pages[index - 1]?.text?.trim().slice(-300),
      nextText: pages[index + 1]?.text?.trim().slice(0, 300),
    };
  });
  return { narration, lang, voice, speed, model, outDir, manifestPath, manifest, items };
}

async function estimate() {
  const { items, voice, lang, speed, model } = await plan();
  const todo = items.filter((item) => !item.cached);
  const chars = todo.reduce((sum, item) => sum + [...item.spoken].length, 0);
  const report = {
    provider,
    model,
    voice: voice.name,
    voiceId: voice.id,
    voiceChosenAutomatically: voice.auto,
    voiceLastUsed: Boolean(voice.lastUsed),
    lang,
    speed,
    pages: items.length,
    alreadyVoiced: items.length - todo.length,
    toGenerate: todo.length,
    characters: chars,
  };
  if (provider === 'heygen') {
    report.note = 'HeyGen Voice bills usage to the workspace; the page lists no per-character price, so show the character count and point to the HeyGen usage page.';
    report.audioFormat = HAS_FFMPEG ? 'mp3 (converted from WAV)' : 'wav (install ffmpeg to get smaller MP3 files)';
  } else if (provider === 'skillry') {
    report.note = 'Skillry ElevenLabs v4 TTS bills Skillry wallet credits per character; approve the quoted budget when generating.';
  } else if (provider === 'fal') {
    report.estimatedUsd = Math.round((chars / 1000) * FAL_USD_PER_1000_CHARS * 100) / 100;
  } else {
    let rate = 1;
    try {
      const models = await elevenJson('/v1/models', credential());
      const entry = models.find((m) => m.model_id === ELEVEN_MODEL);
      rate = Number(entry?.model_rates?.character_cost_multiplier) || 1;
    } catch {}
    report.estimatedCredits = Math.ceil(chars * rate);
    report.note = `${ELEVEN_MODEL} uses ${rate} ElevenLabs credit${rate === 1 ? '' : 's'} per character; the money value depends on the user\u2019s plan.`;
    try {
      const sub = await elevenJson('/v1/user/subscription', credential());
      report.creditsRemaining = sub.character_limit - sub.character_count;
    } catch {
      report.creditsRemaining = 'unknown (the key cannot read the subscription)';
    }
  }
  console.log(JSON.stringify(report, null, 2));
}

// ---------------------------------------------------------------- generation

async function generate() {
  if (!flags.yes) fail('Voicing is paid. Run "estimate", show it to the user, then re-run with --yes after they agree.');
  const key = credential();
  const ctx = await plan();
  mkdirSync(ctx.outDir, { recursive: true });
  const tasksPath = join(ctx.outDir, 'tasks.json');
  const tasks = readJson(tasksPath) || {};
  const queue = ctx.items.filter((item) => !item.cached);
  const failures = [];
  let stop = null;

  async function worker() {
    while (queue.length && !stop) {
      const item = queue.shift();
      try {
        const bytes =
          provider === 'skillry'
            ? await skillryVoice(item, ctx, tasks, tasksPath)
            : provider === 'fal'
              ? await falVoice(item, ctx, tasks, tasksPath, key)
              : provider === 'heygen'
                ? await heygenVoice(item, ctx, key)
                : await elevenVoice(item, ctx, key);
        if (bytes.length < 1000) throw new Error('The audio is unexpectedly small.');
        const path = join(ctx.outDir, item.file);
        writeFileSync(`${path}.tmp`, bytes);
        renameSync(`${path}.tmp`, path);
        console.error(`voiced ${item.id}`);
      } catch (error) {
        if (error.fatal || error.code === 'budget_pending') stop = error;
        failures.push({ id: item.id, error: error.message });
        console.error(`failed ${item.id}: ${error.message}`);
      }
    }
  }
  await Promise.all(Array.from({ length: CONCURRENCY }, worker));

  for (const item of ctx.items) {
    const path = join(ctx.outDir, item.file);
    if (!existsSync(path)) continue;
    const previous = ctx.manifest.slides[item.id];
    ctx.manifest.slides[item.id] = {
      file: item.file,
      textHash: item.textHash,
      chars: [...item.spoken].length,
      provider,
      voice: ctx.voice.name,
      voiceId: ctx.voice.id,
      lang: ctx.lang,
      duration: previous?.file === item.file && previous.duration ? previous.duration : probeDuration(path),
    };
  }
  // Pages whose narration was removed keep their files but leave the manifest.
  const live = new Set(ctx.narration.slides.filter((page) => page.text?.trim()).map((page) => page.id));
  for (const id of Object.keys(ctx.manifest.slides)) if (!live.has(id)) delete ctx.manifest.slides[id];
  ctx.manifest.model = ctx.model;
  ctx.manifest.updatedAt = new Date().toISOString();
  writeJsonAtomic(ctx.manifestPath, ctx.manifest);
  if (provider !== 'fal' && Object.keys(ctx.manifest.slides).length) {
    // Next time this provider and language default to the voice the user just used.
    const saved = readJson(PREFS_PATH) || {};
    savePrefs({
      // An explicit --provider is a one-off (for example a comparison); keep the user's chosen service.
      voiceProvider: flags.provider && saved.voiceProvider ? saved.voiceProvider : provider,
      voices: { ...(saved.voices || {}), [`${provider}:${ctx.lang}`]: { id: ctx.voice.id, name: ctx.voice.name } },
    });
  }

  console.log(
    JSON.stringify(
      {
        ok: failures.length === 0,
        manifest: ctx.manifestPath,
        voice: ctx.voice.name,
        voiced: Object.keys(ctx.manifest.slides).length,
        pages: ctx.items.length,
        failures,
      },
      null,
      2
    )
  );
  if (stop) fail(`Stopped: ${stop.message}`);
  if (failures.length) process.exit(2);
}

async function elevenVoice(item, ctx, key) {
  const body = {
    text: item.spoken,
    model_id: ELEVEN_MODEL,
    voice_settings: { stability: 0.5, similarity_boost: 0.75, speed: ctx.speed },
    apply_text_normalization: 'auto',
  };
  const code = languageCode(ctx.lang);
  if (code) body.language_code = code;
  if (item.previousText) body.previous_text = item.previousText;
  if (item.nextText) body.next_text = item.nextText;
  const response = await fetch(
    `${ELEVEN_API}/v1/text-to-speech/${encodeURIComponent(ctx.voice.id)}?output_format=mp3_44100_128`,
    {
      method: 'POST',
      headers: { 'xi-api-key': key, 'Content-Type': 'application/json', Accept: 'audio/mpeg' },
      body: JSON.stringify(body),
    }
  );
  if (!response.ok) await elevenError(response);
  return Buffer.from(await response.arrayBuffer());
}

async function elevenJson(path, key) {
  const response = await fetch(`${ELEVEN_API}${path}`, { headers: { 'xi-api-key': key, Accept: 'application/json' } });
  if (!response.ok) await elevenError(response);
  return response.json();
}

async function elevenError(response) {
  const text = await response.text().catch(() => '');
  let detail = text.slice(0, 300);
  try {
    const parsed = JSON.parse(text).detail;
    detail = typeof parsed === 'string' ? parsed : parsed?.message || parsed?.status || detail;
  } catch {}
  const error = new Error(`ElevenLabs HTTP ${response.status}: ${detail}`);
  // Bad key, missing permission, no credits or an unusable voice: stop the whole run.
  if ([401, 402, 403].includes(response.status) || /quota|credits|voice_not_found/i.test(text)) error.fatal = true;
  if (response.status === 401) error.message = `ElevenLabs rejected the key (HTTP 401): ${detail}. Check ELEVENLABS_API_KEY; nothing else was tried.`;
  throw error;
}

async function heygenVoice(item, ctx, key) {
  const body = { voice_id: ctx.voice.id, text: item.spoken, model: HEYGEN_MODEL };
  const code = languageCode(ctx.lang);
  if (code) body.language = code;
  // Speed applies to professional clones only; instant and public voices reject it.
  if (ctx.voice.mode === 'professional' && ctx.speed !== 1) body.speed = Math.min(1.25, Math.max(0.75, ctx.speed));
  const result = await heygenJson('/v3/models/audio/tts', key, { method: 'POST', body: JSON.stringify(body) });
  const url = result.data?.audio_url;
  if (!url || !url.startsWith('https://')) throw new Error('HeyGen returned no audio URL.');
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Audio download failed with HTTP ${response.status}.`);
  const wav = Buffer.from(await response.arrayBuffer());
  if (!HAS_FFMPEG) return wav;
  return execFileSync('ffmpeg', ['-v', 'error', '-i', 'pipe:0', '-codec:a', 'libmp3lame', '-b:a', '128k', '-f', 'mp3', 'pipe:1'], {
    input: wav,
    maxBuffer: 256 * 1024 * 1024,
  });
}

/** HeyGen JSON call. Rate limits and upstream hiccups are documented as safe to retry. */
async function heygenJson(path, key, init = {}) {
  for (let attempt = 0; ; attempt += 1) {
    const response = await fetch(`${HEYGEN_API}${path}`, {
      ...init,
      headers: { 'x-api-key': key, 'Content-Type': 'application/json', Accept: 'application/json' },
    });
    if (response.ok) return response.json();
    const text = await response.text().catch(() => '');
    let detail = {};
    try {
      detail = JSON.parse(text).error || {};
    } catch {}
    if (HEYGEN_RETRY_STATUSES.includes(response.status) && attempt < 2) {
      const wait = Number(response.headers.get('retry-after')) || 5 * (attempt + 1);
      await sleep(Math.min(wait, 60) * 1000);
      continue;
    }
    const error = new Error(`HeyGen HTTP ${response.status}${detail.code ? ` ${detail.code}` : ''}: ${detail.message || text.slice(0, 200)}`);
    if ([401, 402, 403].includes(response.status) || HEYGEN_FATAL_CODES.includes(detail.code)) error.fatal = true;
    if (response.status === 401) error.message = 'HeyGen rejected the key (HTTP 401). Check HEYGEN_API_KEY; nothing else was tried.';
    throw error;
  }
}


async function skillryVoice(item, ctx, tasks, tasksPath) {
  let task = tasks[item.key];
  if (!task) {
    task = {
      id: item.id,
      provider: 'skillry',
      requestId: randomUUID(),
      submittedAt: new Date().toISOString(),
    };
    tasks[item.key] = task;
    writeJsonAtomic(tasksPath, tasks);
  }
  const res = await skillryGenerate({
    model: 'eleven-v4',
    text: item.spoken,
    voiceId: ctx.voice.id,
    languageCode: languageCode(ctx.lang) || undefined,
    stability: 0.5,
    similarityBoost: 0.75,
    requestId: task.requestId,
    stepLabel: safeId(item.id),
  });
  return applyAudioSpeed(res.bytes, ctx.speed);
}

async function falVoice(item, ctx, tasks, tasksPath, key) {
  let task = tasks[item.key];
  if (!task) {
    const input = {
      text: item.spoken,
      voice: ctx.voice.id,
      speed: ctx.speed,
      stability: 0.5,
      similarity_boost: 0.75,
      apply_text_normalization: 'auto',
    };
    const code = languageCode(ctx.lang);
    if (code) input.language_code = code;
    if (item.previousText) input.previous_text = item.previousText;
    if (item.nextText) input.next_text = item.nextText;
    const submitted = await fal(`https://queue.fal.run/${FAL_MODEL}`, key, { method: 'POST', body: JSON.stringify(input) });
    if (!submitted.request_id) throw new Error('FAL did not return a request id; nothing was retried.');
    task = {
      id: item.id,
      requestId: submitted.request_id,
      statusUrl: submitted.status_url || `https://queue.fal.run/${FAL_MODEL}/requests/${submitted.request_id}/status`,
      responseUrl: submitted.response_url || `https://queue.fal.run/${FAL_MODEL}/requests/${submitted.request_id}`,
      submittedAt: new Date().toISOString(),
    };
    tasks[item.key] = task;
    writeJsonAtomic(tasksPath, tasks);
  }
  const started = Date.now();
  for (;;) {
    const status = await fal(task.statusUrl, key, { method: 'GET' });
    if (status.status === 'COMPLETED') break;
    if (status.status && !['IN_QUEUE', 'IN_PROGRESS'].includes(status.status)) {
      forget(tasks, tasksPath, item.key);
      throw new Error(`FAL reported ${status.status} for request ${task.requestId}.`);
    }
    if (Date.now() - started > POLL_LIMIT_MS) {
      throw new Error(`Still running after 5 minutes; re-run later to resume request ${task.requestId} without paying again.`);
    }
    await sleep(POLL_MS);
  }
  let result;
  try {
    result = await fal(task.responseUrl, key, { method: 'GET' });
  } catch (error) {
    if (!error.fatal) forget(tasks, tasksPath, item.key);
    throw error;
  }
  const url = result.audio?.url;
  if (!url || !url.startsWith('https://')) {
    forget(tasks, tasksPath, item.key);
    throw new Error(`Request ${task.requestId} returned no audio URL.`);
  }
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Audio download failed with HTTP ${response.status}.`);
  return Buffer.from(await response.arrayBuffer());
}

/** A request that definitely failed is dropped, so a later run the user asks for submits afresh. */
function forget(tasks, tasksPath, key) {
  delete tasks[key];
  writeJsonAtomic(tasksPath, tasks);
}

async function fal(url, key, init) {
  const response = await fetch(url, {
    ...init,
    headers: { Authorization: `Key ${key}`, 'Content-Type': 'application/json', Accept: 'application/json' },
  });
  const text = await response.text();
  if ([401, 402, 403].includes(response.status)) {
    const error = new Error(`FAL refused the request (HTTP ${response.status}). Check FAL_KEY and its balance; nothing else was tried.`);
    error.fatal = true;
    throw error;
  }
  if (!response.ok && response.status !== 202) throw new Error(`FAL HTTP ${response.status}: ${text.slice(0, 300)}`);
  try {
    return JSON.parse(text);
  } catch {
    throw new Error(`FAL returned non-JSON (HTTP ${response.status}).`);
  }
}

// ---------------------------------------------------------------- helpers

function credential() {
  if (provider === 'skillry') return '';
  const name = { fal: 'FAL_KEY', heygen: 'HEYGEN_API_KEY', elevenlabs: 'ELEVENLABS_API_KEY' }[provider];
  const value = process.env[name];
  if (!value) fail(`${name} is required. Ask the user to set it in their environment; never paste it into the chat.`);
  return value;
}

function languageCode(lang) {
  if (lang.startsWith('zh')) return 'zh';
  if (lang.startsWith('pt')) return 'pt';
  const code = lang.split('-')[0];
  return /^[a-z]{2}$/.test(code) ? code : null;
}

function loadPronunciations(lang) {
  const table = { ...(DEFAULT_PRONUNCIATIONS[lang] || {}) };
  if (flags.pronunciations) {
    const custom = JSON.parse(readFileSync(flags.pronunciations, 'utf8'));
    Object.assign(table, custom[lang] || custom['*'] || {});
  }
  return table;
}

function applyPronunciations(text, table) {
  const terms = Object.keys(table).sort((a, b) => b.length - a.length);
  let out = text;
  for (const term of terms) {
    const escaped = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const pattern = /^[\w\s.-]+$/.test(term)
      ? new RegExp(`(?<![A-Za-z0-9])${escaped}(?![A-Za-z0-9])`, 'gi')
      : new RegExp(escaped, 'g');
    out = out.replace(pattern, () => table[term]);
  }
  return out;
}

function probeDuration(path) {
  try {
    const out = execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path], {
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'ignore'],
    });
    const seconds = Number.parseFloat(out);
    return Number.isFinite(seconds) ? Math.round(seconds * 100) / 100 : null;
  } catch {
    return null;
  }
}

function hasCommand(name) {
  try {
    execFileSync(name, ['-version'], { stdio: 'ignore' });
    return true;
  } catch {
    return false;
  }
}

function safeId(id) {
  return String(id).replace(/[^A-Za-z0-9_-]/g, '_').slice(0, 60);
}

function parseFlags(args) {
  const out = {};
  for (let i = 0; i < args.length; i += 1) {
    if (!args[i].startsWith('--')) continue;
    const name = args[i].slice(2);
    const next = args[i + 1];
    if (next === undefined || next.startsWith('--')) out[name] = true;
    else {
      out[name] = next;
      i += 1;
    }
  }
  return out;
}

function requiredFlag(name) {
  if (!flags[name] || flags[name] === true) fail(`--${name} is required.`);
  return flags[name];
}

function readJson(path) {
  try {
    return JSON.parse(readFileSync(path, 'utf8'));
  } catch {
    return null;
  }
}

function writeJsonAtomic(path, value) {
  const temp = `${path}.${process.pid}.tmp`;
  writeFileSync(temp, `${JSON.stringify(value, null, 2)}\n`);
  renameSync(temp, path);
}

function sleep(ms) {
  return new Promise((done) => setTimeout(done, ms));
}

function fail(message) {
  console.error(message);
  process.exit(1);
}
