#!/usr/bin/env node
/**
 * Kling AI video generation — text-to-video, image-to-video, Omni, multi-shot
 * Node.js 18+, zero external deps
 *
 * Paths and body fields follow official docs:
 * https://klingai.com/document-api/llms.txt
 */
import { existsSync } from 'node:fs';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  submitTask,
  queryTask,
  pollAndDownload,
  downloadFile,
  taskStatusOf,
  taskMessageOf,
  isTaskSucceeded,
  resultUrlOf,
} from './shared/task.mjs';
import { parseArgs, getTokenOrExit, readMediaAsValue, readOmniVideoRefUrl, resolveAllowedOutputDir } from './shared/args.mjs';

const API_TASKS = '/tasks';

const RANGE_3_15 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
const RANGE_3_10 = [3, 4, 5, 6, 7, 8, 9, 10];
const DURATION_5_10 = [5, 10];
const RES_720_1080 = ['720p', '1080p'];
const RES_720_1080_4K = ['720p', '1080p', '4k'];

/** Official video models (path-encoded). Source: klingai.com/document-api */
const BASIC_MODELS = {
  'kling-3.0': {
    t2v: '/text-to-video/kling-3.0',
    i2v: '/image-to-video/kling-3.0',
    durations: RANGE_3_15,
    resolutions: RES_720_1080_4K,
    audio: ['native', 'off'],
    multiShot: true,
    lastFrame: true,
    i2vElements: true,
    t2vPromptField: true,
  },
  'kling-3.0-turbo': {
    t2v: '/text-to-video/kling-3.0-turbo',
    i2v: '/image-to-video/kling-3.0-turbo',
    durations: RANGE_3_15,
    resolutions: RES_720_1080,
    audio: null,
    multiShot: false,
    lastFrame: false,
    t2vPromptField: true,
  },
  'kling-2.6': {
    t2v: '/text-to-video/kling-2.6',
    i2v: '/image-to-video/kling-2.6',
    durations: DURATION_5_10,
    resolutions: RES_720_1080,
    audio: ['native', 'off'],
    multiShot: false,
    lastFrame: true,
    t2vPromptField: true,
    audioRequires1080p: true,
    lastFrameRequires1080pSilent: true,
  },
  'kling-2.5-turbo': {
    t2v: '/text-to-video/kling-2.5-turbo',
    i2v: '/image-to-video/kling-2.5-turbo',
    durations: DURATION_5_10,
    resolutions: RES_720_1080,
    audio: null,
    multiShot: false,
    lastFrame: true,
    t2vPromptField: true,
    lastFrameRequires1080p: true,
  },
};

const OMNI_MODELS = {
  'kling-3.0-omni': {
    path: '/omni-video/kling-3.0-omni',
    durations: RANGE_3_15,
    resolutions: RES_720_1080_4K,
    audio: ['native', 'original', 'off'],
    multiShot: true,
    lastFrame: true,
  },
  'kling-o1': {
    path: '/omni-video/kling-o1',
    durations: RANGE_3_10,
    resolutions: RES_720_1080,
    audio: ['original', 'off'],
    multiShot: false,
    lastFrame: true,
  },
};

const LEGACY_MODEL_RENAMES = new Map([
  ['kling-v3', 'kling-3.0'],
  ['kling-v3-omni', 'kling-3.0-omni'],
  ['kling-video-o1', 'kling-o1'],
  ['kling-v2-6', 'kling-2.6'],
  ['kling-v2-5-turbo', 'kling-2.5-turbo'],
]);

function normalizeModelName(v) {
  return String(v || '').trim();
}

function normalizeModelKey(v) {
  return normalizeModelName(v).toLowerCase();
}

function normalizeAliasKey(v) {
  return String(v || '').trim().toLowerCase().replace(/[\s_]+/g, '-');
}

function getVideoModelAliasTarget(v) {
  const key = normalizeAliasKey(v);
  const aliasMap = new Map([
    ['omni3', 'kling-3.0-omni'],
    ['omni-3', 'kling-3.0-omni'],
    ['omni-v3', 'kling-3.0-omni'],
    ['kling-video-o3', 'kling-3.0-omni'],
    ['v3-omni', 'kling-3.0-omni'],
    ['o3', 'kling-3.0-omni'],
    ['kling-o3', 'kling-3.0-omni'],
    ['omni1', 'kling-o1'],
    ['omni-1', 'kling-o1'],
    ['o1', 'kling-o1'],
    ['kling-video-o1', 'kling-o1'],
  ]);
  return aliasMap.get(key) || '';
}

function validateModelAliasInput(rawModel) {
  if (!rawModel) return;
  const model = normalizeModelKey(rawModel);
  const renamed = LEGACY_MODEL_RENAMES.get(model);
  if (renamed) {
    throw new Error(
      `Invalid --model / 请改用官网模型名: ${rawModel} → ${renamed}`,
    );
  }
  const target = getVideoModelAliasTarget(rawModel);
  if (!target || model === target) return;
  throw new Error(
    `Invalid --model alias / --model 使用了别名: ${rawModel}\n`
    + `Use canonical name / 请改用标准名: ${target}\n`
    + 'Alias mapping / 别名映射: omni3 | omni v3 | o3 -> kling-3.0-omni; o1 | omni1 -> kling-o1',
  );
}

function parseBoolFlag(raw, flagName) {
  if (raw === undefined || raw === null || raw === '') return undefined;
  if (raw === true) return true;
  const s = String(raw).trim().toLowerCase();
  if (s === 'true' || s === '1' || s === 'yes') return true;
  if (s === 'false' || s === '0' || s === 'no') return false;
  throw new Error(`Invalid ${flagName} / ${flagName} 须为 true 或 false`);
}

function parseDuration(raw) {
  const n = parseInt(String(raw == null || raw === '' ? '5' : raw), 10);
  if (!Number.isInteger(n)) {
    throw new Error('Invalid --duration / --duration 须为整数秒');
  }
  return n;
}

function parseResolution(raw) {
  if (!raw) return '';
  return String(raw).trim().toLowerCase();
}

function parseAudio(raw) {
  if (!raw) return '';
  return String(raw).trim().toLowerCase();
}

function normalizeReferType(v) {
  const s = String(v || '').trim().toLowerCase();
  if (!s) return 'base';
  return s;
}

function isBaseVideoEdit(args) {
  return Boolean(args.video) && normalizeReferType(args.video_refer_type) === 'base';
}

function shouldSendOmniAspectRatio(args, imageState) {
  return !imageState.hasFirstFrame && !isBaseVideoEdit(args);
}

function parseImageInputs(rawImageArg) {
  if (!rawImageArg) return [];
  const parts = String(rawImageArg).split(',').map(s => s.trim());
  if (parts.some(p => !p)) {
    throw new Error(
      'Invalid --image list / --image 列表中存在空值；请移除空项并确保每个 image_url 非空。',
    );
  }
  return parts;
}

function parseImageTypes(rawImageTypesArg, imageCount) {
  if (!rawImageTypesArg) return new Array(imageCount).fill('');
  const parts = String(rawImageTypesArg).split(',').map(s => s.trim().toLowerCase());
  if (parts.length !== imageCount) {
    throw new Error(
      `Invalid --image_types / --image_types 数量需与 --image 一致: expected ${imageCount}, got ${parts.length}`,
    );
  }
  for (const t of parts) {
    if (!t) continue;
    if (t === 'end_frame') {
      throw new Error(
        'Invalid image type end_frame / 请改用 last_frame（官网枚举）',
      );
    }
    if (t !== 'first_frame' && t !== 'last_frame' && t !== 'refer_image') {
      throw new Error(
        `Invalid image type / 无效图片 type: ${t}. Allowed / 允许: first_frame, last_frame, refer_image, empty`,
      );
    }
  }
  return parts;
}

function parseElementIds(rawElementIdsArg) {
  if (!rawElementIdsArg) return [];
  const parts = String(rawElementIdsArg).split(',').map(s => s.trim());
  if (parts.some(p => !p)) {
    throw new Error(
      'Invalid --element_ids list / --element_ids 列表中存在空值；请移除空项并确保每个 element_id 非空。',
    );
  }
  return parts;
}

function rejectRemovedVideoFlags(args) {
  if (args.mode) {
    throw new Error(
      'Removed --mode / --mode 已移除。请改用 --resolution 720p|1080p|4k（对应原 std/pro/4k）',
    );
  }
  if (args.sound) {
    throw new Error(
      'Removed --sound / --sound 已移除。请改用 --audio native|off|original',
    );
  }
  if (args.shot_type || args.multi_prompt) {
    throw new Error(
      'Removed --shot_type / --multi_prompt / 已移除。多镜头请用 --prompt「镜头 n, m, words;」并设置 --multi_shot true|false',
    );
  }
  if (args.keep_original_sound) {
    throw new Error(
      'Removed --keep_original_sound / 已移除。请改用 --audio original',
    );
  }
  if (args.negative_prompt) {
    throw new Error(
      'Unsupported --negative_prompt / 当前视频接口不支持 --negative_prompt',
    );
  }
}

function printHelp() {
  console.log(`Kling AI video generation

Usage:
  node kling.mjs video --prompt <text> [options]               # Text-to-video
  node kling.mjs video --image <path|url> [--prompt ...]       # Image-to-video
  node kling.mjs video --prompt "..." [--image ...] [--element_ids ...]  # Omni
  node kling.mjs video --multi_shot true --prompt "镜头 1, 2, ...; 镜头 2, 3, ...;"
  node kling.mjs video --task_id <id> [--download]              # Query/download

Submit (common):
  --prompt          Video description (Omni: @image_1 @element_1 @video_1)
  --duration        Seconds; model-dependent (3.0/turbo: 3-15, o1: 3-10, 2.6/2.5: 5|10). Default: official 5
  --model           kling-3.0 / kling-3.0-turbo / kling-2.6 / kling-2.5-turbo / kling-3.0-omni / kling-o1
  --resolution      720p / 1080p / 4k (4k: kling-3.0 and kling-3.0-omni only). Official default: 720p
  --aspect_ratio    16:9 / 9:16 / 1:1 (T2V; Omni when no first_frame and not base video edit).
                    Feature video without first_frame defaults 16:9. Do not pass with first_frame or base edit.
                    With --image, routes to Omni
  --audio           native / off / original (model-dependent; official default: off).
                    original requires --video (keep source audio; feature video cannot use original)
  --output_dir      Output dir (default: ./output)
  --no-wait         Submit only, do not wait
  --wait            Wait for completion (default)

Image-to-video / Omni:
  --image           Image path or URL (comma-separated for Omni refer images)
  --image_types     Optional type list aligned with --image: first_frame / last_frame / refer_image / empty
                    Do not combine last_frame with --image_tail
  --image_tail      Last-frame image (maps to contents type last_frame). Do not combine with --image_types last_frame
  --element_ids     Subject IDs, comma-separated. I2V kling-3.0: contents type=element (max 3). Else Omni.
  --video           Omni reference video: public http(s) URL only
  --video_refer_type feature / base (default: base) → contents feature_video / base_video

Multi-shot:
  --multi_shot      true / false. Request field only on kling-3.0 / kling-3.0-omni (official default true).
                    Base video edit: if omitted, CLI sends false (server default true would fail).
                    Turbo: write 镜头 n, m, words; in --prompt; do not pass --multi_shot.

Query/download:
  --task_id         Task ID
  --download        Download if task succeeded

Watermark:
  --watermark       Generate with watermark (options.watermark_info.enabled=true)

Env:
  credentials file  ~/.config/kling/.credentials (api_key)
  KLING_API_KEY     Session-only Bearer (optional override)
  KLING_MEDIA_ROOTS Comma-separated extra dirs for local media / --output_dir (default: cwd only)
  KLING_ALLOW_ABSOLUTE_PATHS=1  Allow any local path (e.g. WSL downloads outside project)`);
}

function chooseRoute(args) {
  const m = normalizeModelKey(args.model);
  if (m && OMNI_MODELS[m]) return 'omni';
  if (m && !BASIC_MODELS[m] && !OMNI_MODELS[m]) {
    throw new Error(
      `Unknown --model / 未知模型: ${m}\n`
      + 'Allowed / 允许: kling-3.0, kling-3.0-turbo, kling-2.6, kling-2.5-turbo, kling-3.0-omni, kling-o1',
    );
  }
  if (args.video) return 'omni';
  if (args.image) {
    const images = args.image.split(',').map(s => s.trim()).filter(Boolean);
    if (args.aspect_ratio) return 'omni';
    if (images.length > 1) return 'omni';
    if (args.element_ids) {
      const model = m || 'kling-3.0';
      if (BASIC_MODELS[model]?.i2vElements) return 'i2v';
      if (BASIC_MODELS[model]) {
        throw new Error(
          `Unsupported --element_ids for ${model} / 官网图生视频仅 kling-3.0 的 contents 含 element；turbo/2.6/2.5 请去掉 --element_ids，或改用 kling-3.0 / kling-3.0-omni / kling-o1`,
        );
      }
    }
    return 'i2v';
  }
  if (args.element_ids) return 'omni';
  return 't2v';
}

function resolveModel(route, args) {
  const m = normalizeModelKey(args.model);
  if (route === 'omni') {
    if (!m) return 'kling-3.0-omni';
    if (!OMNI_MODELS[m]) {
      throw new Error(
        `Invalid --model for Omni / Omni 不支持该模型: ${m}\n`
        + 'Allowed / 允许: kling-3.0-omni, kling-o1',
      );
    }
    return m;
  }
  if (!m) return 'kling-3.0';
  if (!BASIC_MODELS[m]) {
    throw new Error(
      `Invalid --model for text/image-to-video / 文生/图生不支持该模型: ${m}\n`
      + 'Allowed / 允许: kling-3.0, kling-3.0-turbo, kling-2.6, kling-2.5-turbo',
    );
  }
  return m;
}

function modelSpec(route, model) {
  return route === 'omni' ? OMNI_MODELS[model] : BASIC_MODELS[model];
}

function apiPathOf(route, model) {
  const spec = modelSpec(route, model);
  if (route === 'omni') return spec.path;
  return route === 't2v' ? spec.t2v : spec.i2v;
}

function buildSettings({ spec, duration, resolution, aspectRatio, audio, multiShot, includeAspect }) {
  const settings = {};
  if (duration != null) settings.duration = duration;
  if (resolution) settings.resolution = resolution;
  if (includeAspect && aspectRatio) settings.aspect_ratio = aspectRatio;
  if (audio && spec.audio) settings.audio = audio;
  if (spec.multiShot && multiShot !== undefined) settings.multi_shot = multiShot;
  return settings;
}

function buildOptions(args) {
  if (!args.watermark) return undefined;
  return { watermark_info: { enabled: true } };
}

function validateSettings(route, model, spec, args, ctx) {
  const duration = parseDuration(args.duration);
  if (!spec.durations.includes(duration)) {
    throw new Error(
      `Invalid --duration for ${model} / 该模型时长须为: ${spec.durations.join(', ')}`,
    );
  }

  const resolution = parseResolution(args.resolution);
  if (resolution && !spec.resolutions.includes(resolution)) {
    throw new Error(
      `Invalid --resolution for ${model} / 该模型清晰度须为: ${spec.resolutions.join(', ')}`,
    );
  }

  const audio = parseAudio(args.audio);
  if (audio) {
    if (!spec.audio) {
      throw new Error(`Unsupported --audio for ${model} / 该模型接口无 audio 字段`);
    }
    if (!spec.audio.includes(audio)) {
      throw new Error(
        `Invalid --audio for ${model} / 该模型 audio 须为: ${spec.audio.join(', ')}`,
      );
    }
  }

  let multiShot = parseBoolFlag(args.multi_shot, '--multi_shot');
  if (multiShot !== undefined && !spec.multiShot) {
    throw new Error(
      `Unsupported --multi_shot for ${model} / 该模型请求体无 settings.multi_shot。`
      + (model === 'kling-3.0-turbo'
        ? ' 官网 Turbo 多镜头写在 --prompt：镜头 n, m, words;'
        : ''),
    );
  }
  if (spec.multiShot && multiShot === undefined && isBaseVideoEdit(args)) {
    multiShot = false;
  }

  if (spec.audioRequires1080p && audio === 'native' && (resolution || '720p') !== '1080p') {
    throw new Error(
      'Invalid --audio native / 官网：生成有声视频时仅支持 1080p。请设置 --resolution 1080p',
    );
  }

  if (ctx.hasLastFrame && !spec.lastFrame) {
    throw new Error(`Unsupported last_frame for ${model} / 该模型不支持尾帧`);
  }
  if (ctx.hasLastFrame && spec.lastFrameRequires1080p && (resolution || '720p') !== '1080p') {
    throw new Error('Invalid last_frame / 官网：该模型尾帧仅支持 1080p');
  }
  if (ctx.hasLastFrame && spec.lastFrameRequires1080pSilent) {
    if ((resolution || '720p') !== '1080p') {
      throw new Error('Invalid last_frame / 官网：kling-2.6 尾帧仅支持 1080p 且无声');
    }
    if (audio && audio !== 'off') {
      throw new Error('Invalid last_frame / 官网：kling-2.6 尾帧仅支持无声视频（--audio off）');
    }
  }

  if (model === 'kling-o1' && ctx.hasFirstFrame && !ctx.hasReferImage && !args.video) {
    if (duration !== 5 && duration !== 10) {
      throw new Error(
        'Invalid --duration for kling-o1 first_frame / 官网：仅首帧且无 refer_image/参考视频时时长仅 5 或 10 秒',
      );
    }
  }

  return { duration, resolution, audio, multiShot };
}

function validateOmniVideoListRules(args) {
  if (!args.video) {
    if (args.video_refer_type) {
      throw new Error(
        'Invalid --video_refer_type without --video / 仅在传入 --video 时才能设置 --video_refer_type。',
      );
    }
    return { referType: '' };
  }

  const rawVideo = String(args.video).trim();
  if (!rawVideo) {
    throw new Error('Invalid --video / --video 不能为空，须为非空公网 http(s) URL。');
  }
  if (rawVideo.includes(',')) {
    throw new Error('Invalid --video / 当前仅支持 1 段参考视频，请只传一个 URL。');
  }

  const referType = normalizeReferType(args.video_refer_type);
  if (referType !== 'feature' && referType !== 'base') {
    throw new Error(
      `Invalid --video_refer_type / 无效 refer_type: ${referType}. Allowed / 允许: feature, base`,
    );
  }
  return { referType };
}

function validateOmniImageListRules(args, imageInputs, imageTypes, hasTailArg) {
  const maxImages = args.video ? 4 : 7;
  const totalImages = imageInputs.length + (hasTailArg ? 1 : 0);
  if (totalImages > maxImages) {
    throw new Error(
      `Too many images for omni-video / Omni 图片数量超限: max ${maxImages} (current ${totalImages})`,
    );
  }

  const hasFirstFrame = imageTypes.includes('first_frame');
  const hasLastFrame = imageTypes.includes('last_frame') || hasTailArg;
  const hasReferImage = imageTypes.some((t) => (t || 'refer_image') === 'refer_image');

  if (hasLastFrame && !hasFirstFrame) {
    throw new Error(
      'Invalid image list: last_frame needs first_frame / 不支持仅尾帧，配置 last_frame 时必须同时有 first_frame。',
    );
  }

  const model = normalizeModelKey(args.model) || 'kling-3.0-omni';
  if (model === 'kling-o1' && hasLastFrame && totalImages > 2) {
    throw new Error(
      'Invalid image list for kling-o1 / kling-o1 在图片数超过 2 时不支持 last_frame。',
    );
  }

  const hasFrame = hasFirstFrame || hasLastFrame;
  if (hasFrame && args.video && normalizeReferType(args.video_refer_type) === 'base') {
    throw new Error(
      'Invalid combo: frame images with video edit / 首帧或尾帧不能与视频编辑（--video_refer_type base）同时使用。',
    );
  }
  return { totalImages, hasFirstFrame, hasLastFrame, hasReferImage };
}

function validateOmniElementListRules(args, elementIds, imageState) {
  if (!elementIds.length) return;
  const model = normalizeModelKey(args.model) || 'kling-3.0-omni';
  const hasFirstAndLast = imageState.hasFirstFrame && imageState.hasLastFrame;

  if ((imageState.hasFirstFrame || imageState.hasLastFrame) && elementIds.length > 3) {
    throw new Error(
      `Too many subjects with frame generation / 首帧或尾帧生视频时主体最多 3 个: current ${elementIds.length}`,
    );
  }

  if (hasFirstAndLast && model === 'kling-o1') {
    throw new Error(
      'Invalid element_list for kling-o1 / kling-o1 在首尾帧生视频场景不支持主体。',
    );
  }

  const totalRefs = imageState.totalImages + elementIds.length;
  const maxRefs = args.video ? 4 : 7;
  if (totalRefs > maxRefs) {
    throw new Error(
      `Too many refs for omni-video / Omni 参考图与主体总数超限: max ${maxRefs} (current ${totalRefs})`,
    );
  }
}

function validateOmniAudioVideoRules(model, spec, audio, args, multiShot, imageState) {
  if (audio === 'original' && !args.video) {
    throw new Error(
      'Invalid --audio original without --video / 官网：original 为保留参考视频原声，须同时提供 --video',
    );
  }
  const referType = args.video ? normalizeReferType(args.video_refer_type) : '';
  if (!args.video) return;

  if (referType === 'feature') {
    if (audio && audio !== 'off') {
      throw new Error(
        'Invalid --audio with feature video / 官网：特征参考视频时 audio 只能为 off',
      );
    }
    if (multiShot === false) {
      throw new Error(
        'Invalid --multi_shot false with feature video / 官网：特征参考视频生成多镜头时 multi_shot 只能为 true',
      );
    }
    if (model === 'kling-o1' && imageState.hasLastFrame) {
      throw new Error(
        'Invalid last_frame with feature video / 官网：kling-o1 特征参考视频仅支持首帧，不支持尾帧',
      );
    }
  }
  if (referType === 'base') {
    if (audio === 'native') {
      throw new Error(
        'Invalid --audio native with base video / 官网：待编辑视频 audio 不能为 native',
      );
    }
    if (multiShot === true) {
      throw new Error(
        'Invalid --multi_shot with base video / 官网：待编辑视频不支持多镜头',
      );
    }
    if (imageState.hasFirstFrame || imageState.hasLastFrame) {
      throw new Error(
        'Invalid frames with base video / 官网：待编辑视频不支持定义首帧或尾帧',
      );
    }
  }
  if (!spec.audio?.includes('original') && audio === 'original') {
    throw new Error(`Invalid --audio original for this model / 该模型不支持 original`);
  }
}

async function queryExistingTask(taskId, token, outputDir, download) {
  const data = await queryTask(API_TASKS, taskId, token);
  const status = taskStatusOf(data) || 'unknown';
  console.log(`Task ID / 任务 ID: ${taskId}`);
  console.log(`Status / 状态: ${status}`);
  const msg = taskMessageOf(data);
  if (msg) console.log(`Message / 消息: ${msg}`);
  const url = resultUrlOf(data);
  if (url) {
    console.log(`Video URL / 视频链接: ${url}`);
    const wm = Array.isArray(data?.outputs)
      ? data.outputs.find((item) => item?.type === 'video' && item?.watermark_url)?.watermark_url
      : data?.task_result?.videos?.[0]?.watermark_url;
    if (wm) console.log(`Watermark URL / 水印视频: ${wm}`);
    if (download && isTaskSucceeded(status)) {
      const { mkdir } = await import('node:fs/promises');
      const { join } = await import('node:path');
      await mkdir(outputDir, { recursive: true });
      await downloadFile(url, join(outputDir, `${taskId}.mp4`));
    }
  }
}

export async function main() {
  const args = parseArgs(process.argv);
  if (args.help) { printHelp(); return; }
  validateModelAliasInput(args.model);
  rejectRemovedVideoFlags(args);

  const token = await getTokenOrExit();
  const outputDir = resolveAllowedOutputDir(args.output_dir || './output');

  if (args.task_id && !args.prompt && !args.image && args.multi_shot === undefined) {
    try {
      await queryExistingTask(args.task_id, token, outputDir, args.download);
    } catch (e) {
      console.error(`Error / 错误: ${e.message}`);
      process.exit(1);
    }
    return;
  }

  const imageInputs = parseImageInputs(args.image);
  const imageTypes = parseImageTypes(args.image_types, imageInputs.length);
  if (args.image_tail && imageTypes.includes('last_frame')) {
    throw new Error(
      'Invalid combo: --image_tail with --image_types last_frame / 尾帧只用 --image_tail 或 --image_types last_frame，不要同时传',
    );
  }
  if (args.image_tail && imageInputs.length > 0 && !imageTypes[0]) {
    imageTypes[0] = 'first_frame';
  }
  const elementIds = parseElementIds(args.element_ids);
  const videoState = validateOmniVideoListRules(args);
  const hasImage = imageInputs.length > 0;
  if (!args.prompt && !hasImage && args.multi_shot === undefined) {
    console.error('Error / 错误: --prompt, --image, or --multi_shot required');
    console.error('Use --help / 使用 --help 查看帮助');
    process.exit(1);
  }

  if (args.image_tail && !hasImage) {
    console.error('Error / 错误: --image_tail requires --image (first frame) / 首尾帧需要首帧 --image');
    process.exit(1);
  }

  if (hasImage) {
    const firstInput = imageInputs[0];
    const isUrl = firstInput.startsWith('http://') || firstInput.startsWith('https://');
    if (!isUrl && !existsSync(resolve(firstInput))) {
      console.error(`Error / 错误: image not found / 图片不存在: ${firstInput}`);
      process.exit(1);
    }
  }

  try {
    const route = chooseRoute(args);
    const model = resolveModel(route, args);
    const spec = modelSpec(route, model);
    const apiPath = apiPathOf(route, model);
    const queryHint = `node kling.mjs video --task_id`;

    let imageState = {
      totalImages: imageInputs.length + (args.image_tail ? 1 : 0),
      hasFirstFrame: imageTypes.includes('first_frame') || (route === 'i2v' && hasImage),
      hasLastFrame: imageTypes.includes('last_frame') || Boolean(args.image_tail),
      hasReferImage: imageTypes.some((t) => t === 'refer_image'),
    };
    if (route === 'omni' && (imageInputs.length > 0 || args.image_tail)) {
      imageState = validateOmniImageListRules(args, imageInputs, imageTypes, Boolean(args.image_tail));
    }
    if (route === 'omni') validateOmniElementListRules(args, elementIds, imageState);

    const { duration, resolution, audio, multiShot } = validateSettings(route, model, spec, args, imageState);
    if (route === 'omni') validateOmniAudioVideoRules(model, spec, audio, args, multiShot, imageState);

    const prompt = String(args.prompt || '').trim();
    if (route === 't2v' && !prompt) {
      throw new Error('text-to-video requires --prompt / 文生视频须提供 --prompt');
    }
    if (route === 'omni' && !prompt) {
      throw new Error('Omni requires non-empty --prompt / Omni 须提供非空 --prompt');
    }

    const includeAspect = route === 't2v' || (route === 'omni' && shouldSendOmniAspectRatio(args, imageState));
    if (route === 'omni' && args.aspect_ratio && !includeAspect) {
      throw new Error(
        'Invalid --aspect_ratio / 有首帧或 base 视频编辑时不要传 --aspect_ratio（画面比例由素材决定）',
      );
    }
    const aspectRatio = args.aspect_ratio || (includeAspect ? '16:9' : '');
    const settings = buildSettings({
      spec,
      duration,
      resolution,
      aspectRatio,
      audio,
      multiShot,
      includeAspect,
    });
    const options = buildOptions(args);

    let payload;
    if (route === 't2v') {
      payload = { prompt, settings };
    } else if (route === 'i2v') {
      const contents = [];
      if (prompt) contents.push({ type: 'prompt', text: prompt });
      contents.push({ type: 'first_frame', url: await readMediaAsValue(imageInputs[0]) });
      if (args.image_tail) {
        contents.push({ type: 'last_frame', url: await readMediaAsValue(args.image_tail) });
      }
      if (elementIds.length) {
        if (!spec.i2vElements) {
          throw new Error(
            `Unsupported --element_ids for ${model} / 官网图生视频仅 kling-3.0 的 contents 含 element`,
          );
        }
        if (elementIds.length > 3) {
          throw new Error(
            `Too many subjects for image-to-video / 官网：图生视频最多 3 个主体: current ${elementIds.length}`,
          );
        }
        for (let i = 0; i < elementIds.length; i++) {
          contents.push({
            type: 'element',
            element_id: String(elementIds[i]),
            id: `element_${i + 1}`,
          });
        }
      }
      payload = { contents, settings };
    } else {
      const contents = [];
      if (prompt) contents.push({ type: 'prompt', text: prompt });
      for (let i = 0; i < imageInputs.length; i++) {
        const type = imageTypes[i] || 'refer_image';
        contents.push({
          type,
          url: await readMediaAsValue(imageInputs[i]),
          id: `image_${i + 1}`,
        });
      }
      if (args.image_tail) {
        contents.push({
          type: 'last_frame',
          url: await readMediaAsValue(args.image_tail),
          id: `image_${imageInputs.length + 1}`,
        });
      }
      for (let i = 0; i < elementIds.length; i++) {
        contents.push({
          type: 'element',
          element_id: String(elementIds[i]),
          id: `element_${i + 1}`,
        });
      }
      if (args.video) {
        const videoType = videoState.referType === 'feature' ? 'feature_video' : 'base_video';
        contents.push({
          type: videoType,
          url: readOmniVideoRefUrl(args.video),
          id: 'video_1',
        });
      }
      payload = { contents, settings };
    }
    if (options) payload.options = options;

    const result = await submitTask(apiPath, payload, token);
    console.log(`\nTask ID / 任务 ID: ${result.taskId}`);
    console.log(`Query / 查询: ${queryHint} ${result.taskId} [--download]`);
    if (args.wait !== false) {
      console.log();
      const outPath = await pollAndDownload(API_TASKS, result.taskId, outputDir, { token });
      console.log(`\n✓ Done / 完成: ${outPath}`);
    }
  } catch (e) {
    console.error(`Error / 错误: ${e.message}`);
    process.exit(1);
  }
}

const __filename = fileURLToPath(import.meta.url);
if (process.argv[1] && resolve(__filename) === resolve(process.argv[1])) {
  main().catch((e) => {
    console.error(`Error / 错误: ${e?.message || e}`);
    process.exit(1);
  });
}
