#!/usr/bin/env node
/**
 * Kling AI image generation — text-to-image, image-to-image, 4K, series, subject
 * Node.js 18+, zero external deps
 */
import { submitTask, queryTask, pollTask, downloadFile } from './shared/task.mjs';
import { resolve, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseArgs, getTokenOrExit, readMediaAsValue, resolveAllowedOutputDir } from './shared/args.mjs';

const API_GEN = '/v1/images/generations';
const API_OMNI = '/v1/images/omni-image';

function normalizeModelName(v) {
  return String(v || '').trim();
}

function normalizeAliasKey(v) {
  return String(v || '').trim().toLowerCase().replace(/[\s_]+/g, '-');
}

function getImageModelAliasTarget(v) {
  const key = normalizeAliasKey(v);
  const aliasMap = new Map([
    ['omni3', 'kling-v3-omni'],
    ['omni-3', 'kling-v3-omni'],
    ['omni-v3', 'kling-v3-omni'],
    ['v3-omni', 'kling-v3-omni'],
    ['o3', 'kling-v3-omni'],
    ['O3', 'kling-v3-omni'],
    ['kling-image-o3', 'kling-v3-omni'],
    ['kling-o3', 'kling-v3-omni'],
    ['omni1', 'kling-image-o1'],
    ['omni-1', 'kling-image-o1'],
    ['o1', 'kling-image-o1'],
    ['kling-o1', 'kling-image-o1'],
  ]);
  return aliasMap.get(key) || '';
}

function validateModelAliasInput(rawModel) {
  if (!rawModel) return;
  const model = normalizeModelName(rawModel).toLowerCase();
  const target = getImageModelAliasTarget(rawModel);
  if (!target || model === target) return;
  throw new Error(
    `Invalid --model alias / --model 使用了别名: ${rawModel}\n`
    + `Use canonical name / 请改用标准名: ${target}\n`
    + 'Alias mapping / 别名映射: omni3 | omni v3 | o3 -> kling-v3-omni; image o1/omni1 -> kling-image-o1',
  );
}

function validateModelForRoute(apiPath, args) {
  validateModelAliasInput(args.model);
  const model = normalizeModelName(args.model).toLowerCase();
  if (!model) return;

  // We only validate what we can be sure about from public enums.
  // - omni-image: only kling-v3-omni / kling-image-o1
  // - generations: must not use omni-only models
  if (apiPath === API_OMNI) {
    const allowed = new Set(['kling-v3-omni', 'kling-image-o1']);
    if (!allowed.has(model)) {
      throw new Error(
        `Invalid --model for omni-image / omni-image 不支持该模型: ${model}\n`
        + `Allowed / 允许: kling-v3-omni, kling-image-o1`,
      );
    }
  } else {
    const allowed = new Set(['kling-v3', 'kling-v2-1']);
    if (!allowed.has(model)) {
      throw new Error(
        `Invalid --model for generations / generations 不支持该模型: ${model}\n`
        + `Allowed / 允许: kling-v3, kling-v2-1`,
      );
    }
  }
}

function parseImageInputs(rawImageArg) {
  if (!rawImageArg) return [];
  const parts = String(rawImageArg).split(',').map(s => s.trim());
  if (parts.some(p => !p)) {
    throw new Error(
      'Invalid --image list / --image 列表中存在空值；请移除空项并确保每个 image 非空。',
    );
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

function validateOmniRefCount(imageInputs, elementIds) {
  const totalRefs = imageInputs.length + elementIds.length;
  if (totalRefs > 10) {
    throw new Error(
      `Too many refs for omni-image / omni-image 参考图与主体总数超限: max 10 (current ${totalRefs})`,
    );
  }
}

function printHelp() {
  console.log(`Kling AI image generation

Usage:
  node kling.mjs image --prompt <text> [options]           # Text/image-to-image
  node kling.mjs image --prompt "..." [--resolution 4k]     # 4K / series → Omni (kling-v3-omni)
  node kling.mjs image --model kling-image-o1 --prompt "..."  # official Omni default (t2i / i2i)
  node kling.mjs image --task_id <id> [--download]         # Query/download

Submit (common):
  --prompt          Image description (required). Omni: <<<image_1>>> / <<<element_1>>>
  --resolution      1k / 2k / 4k (4k uses Omni)
  --aspect_ratio    Aspect ratio (default: 16:9 basic; Omni t2i 16:9; Omni with --image: auto).
                    auto is invalid without --image
  --n               Number of images 1-9
  --output_dir      Output dir (default: ./output)
  --no-wait         Submit only, do not wait
  --wait            Wait for completion (default)

Basic API:
  --negative_prompt Negative prompt (not with --image)
  --model           kling-v3 (default) / kling-v2-1
  --element_ids     Subject IDs for kling-v3 element_list

Omni (4K/series/multi-image):
  --model           kling-image-o1 (official default) / kling-v3-omni (4k / series)
  --result_type     single / series (default: single)
  --series_amount   Series count 2-9 or auto (when result_type=series; auto = 智能数量)
  --image           Reference image path or URL, comma-separated for multiple
  --element_ids     Subject IDs, comma-separated (kling-v3 generations element_list, or Omni)
  (omni refs)       image count + element count <= 10

Query/download:
  --task_id         Task ID
  --download        Download if task succeeded

Env:
  credentials file  ~/.config/kling/.credentials (api_key)
  KLING_API_KEY     Session-only Bearer (optional override)
  KLING_MEDIA_ROOTS Comma-separated extra dirs for --image / --output_dir (default: cwd only)
  KLING_ALLOW_ABSOLUTE_PATHS=1  Allow any local path (e.g. WSL downloads)`);
}

function useOmniApi(args) {
  const m = normalizeModelName(args.model).toLowerCase();
  if (m === 'kling-v3-omni' || m === 'kling-image-o1') return true;
  if (args.result_type === 'series') return true;
  if ((args.resolution || '').toLowerCase() === '4k') return true;
  if ((args.aspect_ratio || '').toLowerCase() === 'auto') return true;
  if (args.image && args.image.includes(',')) return true;
  return false;
}

function defaultOmniImageModel(args) {
  if ((args.resolution || '').toLowerCase() === '4k') return 'kling-v3-omni';
  if (args.result_type === 'series') return 'kling-v3-omni';
  return 'kling-image-o1';
}

async function queryTaskAnyPath(taskId, token) {
  for (const apiPath of [API_OMNI, API_GEN]) {
    try {
      const data = await queryTask(apiPath, taskId, token);
      if (data && (data.task_status === 'succeed' || data.task_status === 'failed' || data.task_status === 'processing' || data.task_status === 'submitted')) {
        return { apiPath, data };
      }
    } catch (_) { /* try next */ }
  }
  throw new Error(`Task not found / 未找到任务: ${taskId}`);
}

function collectImageUrls(taskResult) {
  const urls = [];
  const append = (list) => {
    if (!Array.isArray(list)) return;
    for (const item of list) {
      if (item?.url) urls.push(item.url);
    }
  };
  append(taskResult?.images);
  append(taskResult?.series_images);
  if (urls.length === 0 && taskResult?.url) urls.push(taskResult.url);
  return urls;
}

async function pollAndDownloadImages(apiPath, taskId, outputDir, opts = {}) {
  const data = await pollTask(apiPath, taskId, opts);
  const urls = collectImageUrls(data?.task_result || {});
  if (urls.length === 0) {
    throw new Error('Task succeeded but missing image urls / 任务成功但未返回图片 URL');
  }
  const outPaths = [];
  for (let i = 0; i < urls.length; i++) {
    const outPath = join(outputDir, urls.length === 1 ? `${taskId}.png` : `${taskId}_${i}.png`);
    await downloadFile(urls[i], outPath);
    outPaths.push(outPath);
  }
  return outPaths;
}

export async function main() {
  const args = parseArgs(process.argv);
  if (args.help) { printHelp(); return; }
  validateModelAliasInput(args.model);

  const token = await getTokenOrExit();
  const outputDir = resolveAllowedOutputDir(args.output_dir || './output');
  const queryHint = `node kling.mjs image --task_id`;

  if (args.task_id && !args.prompt) {
    try {
      const { apiPath, data } = await queryTaskAnyPath(args.task_id, token);
      console.log(`Task ID / 任务 ID: ${args.task_id}`);
      console.log(`Status / 状态: ${data?.task_status || 'unknown'}`);
      const result = data?.task_result || {};
      const imageUrls = collectImageUrls(result);
      imageUrls.forEach((url, i) => {
        console.log(`Image / 图片[${i}]: ${url}`);
      });
      if (args.download && imageUrls.length > 0) {
        const { mkdir } = await import('node:fs/promises');
        await mkdir(outputDir, { recursive: true });
        for (let i = 0; i < imageUrls.length; i++) {
          const outPath = join(outputDir, imageUrls.length === 1 ? `${args.task_id}.png` : `${args.task_id}_${i}.png`);
          await downloadFile(imageUrls[i], outPath);
        }
      }
    } catch (e) {
      console.error(`Error / 错误: ${e.message}`);
      process.exit(1);
    }
    return;
  }

  if (!args.prompt) {
    console.error('Error / 错误: --prompt or --task_id required');
    console.error('Use --help / 使用 --help 查看帮助');
    process.exit(1);
  }

  const apiPath = useOmniApi(args) ? API_OMNI : API_GEN;
  const imageInputs = parseImageInputs(args.image);
  const elementIds = parseElementIds(args.element_ids);

  try {
    validateModelForRoute(apiPath, args);

    if (apiPath === API_GEN) {
      const modelName = (args.model || 'kling-v3').toLowerCase();
      if (args.negative_prompt && imageInputs.length > 0) {
        throw new Error(
          'Unsupported --negative_prompt with --image / 官网：图生图不支持负向提示词',
        );
      }
      if (elementIds.length && modelName === 'kling-v2-1') {
        throw new Error(
          'Unsupported --element_ids for kling-v2-1 / 官网：kling-v2-1 无 element_list，请用 kling-v3 或 Omni',
        );
      }
      if (imageInputs.length + elementIds.length > 10) {
        throw new Error(
          `Too many refs for generations / 参考图与主体总数超限: max 10 (current ${imageInputs.length + elementIds.length})`,
        );
      }
      const payload = {
        model_name: modelName,
        prompt: args.prompt,
        negative_prompt: args.negative_prompt || '',
        n: parseInt(args.n || '1', 10),
        aspect_ratio: args.aspect_ratio || '16:9',
        resolution: args.resolution || '1k',
        callback_url: '',
      };
      if (imageInputs.length > 0) {
        payload.image = await readMediaAsValue(imageInputs[0]);
      }
      if (elementIds.length > 0) {
        payload.element_list = elementIds.map((id) => ({ element_id: id }));
      }
      const result = await submitTask(API_GEN, payload, token);
      console.log(`\nTask ID / 任务 ID: ${result.taskId}`);
      console.log(`Query / 查询: ${queryHint} ${result.taskId} [--download]`);
      if (args.wait !== false) {
        console.log();
        const outPaths = await pollAndDownloadImages(API_GEN, result.taskId, outputDir, { token });
        console.log(`\n✓ Done / 完成: ${outPaths.length} image(s)`);
        outPaths.forEach((p) => console.log(`  - ${p}`));
      }
      return;
    }

    const hasRefImage = imageInputs.length > 0;
    const requestedAspect = (args.aspect_ratio || '').toLowerCase();
    if (requestedAspect === 'auto' && !hasRefImage) {
      throw new Error(
        'Invalid --aspect_ratio auto / 无参考图时不支持 auto，请指定 16:9 等固定比例，或提供 --image',
      );
    }
    const payload = {
      model_name: (args.model || defaultOmniImageModel(args)).toLowerCase(),
      prompt: args.prompt,
      resolution: (args.resolution || '1k').toLowerCase(),
      aspect_ratio: requestedAspect || (hasRefImage ? 'auto' : '16:9'),
      result_type: args.result_type || 'single',
      callback_url: '',
    };
    if ((args.resolution || '').toLowerCase() === '4k' && payload.model_name === 'kling-image-o1') {
      throw new Error(
        'Invalid --resolution 4k for kling-image-o1 / 官网能力地图：Image O1 支持 1k/2k，4k 请用 kling-v3-omni',
      );
    }
    if (payload.result_type === 'series' && payload.model_name === 'kling-image-o1') {
      throw new Error(
        'Invalid --result_type series for kling-image-o1 / 官网能力地图：Image O1 不支持组图，请用 kling-v3-omni',
      );
    }
    if (payload.result_type === 'series') {
      if (imageInputs.length === 0) {
        throw new Error(
          'Invalid --result_type series without --image / 组图仅支持 i2i，请提供 --image（t2i 不支持 series）。',
        );
      }
      const rawSeries = String(args.series_amount || '4').trim().toLowerCase();
      if (rawSeries === 'auto') {
        payload.series_amount = 'auto';
      } else {
        const n = parseInt(rawSeries, 10);
        if (!Number.isInteger(n) || n < 2 || n > 9) {
          throw new Error('Invalid --series_amount / 须为 2-9 或 auto');
        }
        payload.series_amount = n;
      }
    } else {
      payload.n = parseInt(args.n || '1', 10);
    }
    validateOmniRefCount(imageInputs, elementIds);
    if (imageInputs.length > 0) {
      payload.image_list = [];
      for (const img of imageInputs) {
        payload.image_list.push({ image: await readMediaAsValue(img) });
      }
    }
    if (elementIds.length > 0) {
      payload.element_list = elementIds.map(id => ({ element_id: id }));
    }

    const result = await submitTask(API_OMNI, payload, token);
    console.log(`\nTask ID / 任务 ID: ${result.taskId}`);
    console.log(`Query / 查询: ${queryHint} ${result.taskId} [--download]`);
    if (args.wait !== false) {
      console.log();
      const outPaths = await pollAndDownloadImages(API_OMNI, result.taskId, outputDir, { token });
      console.log(`\n✓ Done / 完成: ${outPaths.length} image(s)`);
      outPaths.forEach((p) => console.log(`  - ${p}`));
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
