#!/usr/bin/env node
/**
 * folder-icon: 为子文件夹批量生成并应用彩色图标
 *
 * 依赖：
 *   npm install -g @resvg/resvg-js js-yaml
 *
 * 用法（WSL / Linux）：
 *   NODE_PATH=$(npm root -g) node folder-icon.js "/mnt/d/目标目录" [--dry-run] [--force] [--icon-dir "目录名"]
 *
 * 用法（Windows）：
 *   node folder-icon.js "D:\目标目录" [--dry-run] [--force] [--icon-dir "目录名"]
 */

'use strict';

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const https = require('https');
const yaml = require('js-yaml');

// ============================================================
// 全局模块路径（兼容全局安装）
// ============================================================
const NPM_GLOBAL = process.env.NPM_GLOBAL ||
  execSync('npm root -g', { encoding: 'utf8' }).trim();

const { Resvg } = require(path.join(NPM_GLOBAL, '@resvg/resvg-js'));

// ============================================================
// 常量配置
// ============================================================

// 方案C 圆形底衬颜色：统一浅灰，柔和且适配各种深色主题
const BADGE_BG = '#F0F0F4';

// ============================================================
// 已注册图标中哪些有 filled 版本（Tabler icons/filled/ 目录）
// 有 filled → 使用 filled（视觉更重、更清晰）
// 没有 filled → 自动回退到 outline
// ============================================================
const FILLED_ICONS = new Set([
  'account-search-outline.ico',
  'alert-outline.ico',
  'archive-outline.ico',
  'book-outline.ico',
  'bug-outline.ico',
  'cactus.ico',
  'chart-bar-outline.ico',
  'circle-outline.ico',
  'cloud-download-outline.ico',
  'database-outline.ico',
  'download-outline.ico',
  'edit-outline.ico',
  'file-document-outline.ico',
  'file-excel-outline.ico',
  'file-word-outline.ico',
  'folder-outline.ico',
  'gamepad-outline.ico',
  'heart-outline.ico',
  'image-outline.ico',
  'link-outline.ico',
  'lock-outline.ico',
  'mail-outline.ico',
  'music-outline.ico',
  'presentation-outline.ico',
  'school-outline.ico',
  'search-outline.ico',
  'shield-check-outline.ico',
  'star-outline.ico',
  'trash-outline.ico',
  'upload-outline.ico',
  'video-outline.ico',
]);

const ICON_TO_TABLER = {
  "account-search-outline.ico": "user-search",
  "alert-outline.ico": "alert-circle",
  "archive-outline.ico": "archive",
  "book-outline.ico": "book",
  "bug-outline.ico": "bug",
  "cactus.ico": "cactus",
  "chart-bar-outline.ico": "chart-bar",
  "circle-outline.ico": "circle",
  "cloud-download-outline.ico": "cloud-download",
  "cloud-upload-outline.ico": "cloud-upload",
  "code-outline.ico": "code",
  "cpu-outline.ico": "cpu",
  "database-outline.ico": "database",
  "device-laptop-outline.ico": "device-laptop",
  "download-outline.ico": "download",
  "edit-outline.ico": "edit",
  "file-document-outline.ico": "file-description",
  "file-excel-outline.ico": "file-spreadsheet",
  "file-word-outline.ico": "file-text",
  "folder-outline.ico": "folder",
  "gamepad-outline.ico": "device-gamepad",
  "heart-outline.ico": "heart",
  "image-outline.ico": "photo",
  "link-outline.ico": "link",
  "lock-outline.ico": "lock",
  "mail-outline.ico": "mail",
  "music-outline.ico": "music",
  "notebook-outline.ico": "notes",
  "presentation-outline.ico": "presentation",
  "school-outline.ico": "school",
  "search-outline.ico": "search",
  "shield-check-outline.ico": "shield-check",
  "signal-outline.ico": "wifi",
  "star-outline.ico": "star",
  "terminal-outline.ico": "terminal",
  "tool-outline.ico": "tools",
  "trash-outline.ico": "trash",
  "upload-outline.ico": "upload",
  "video-outline.ico": "video",
};

// ============================================================
// 路径转换工具（WSL ↔ Windows）
// 所有 Node.js fs 操作使用 WSL 路径；attrib/curl 等 Windows 命令才转 Windows 路径
// ============================================================

// Windows 路径 → WSL 路径（供 Node.js fs 使用）
function toWsl(windowsPath) {
  if (!windowsPath) return windowsPath;
  if (windowsPath.startsWith('/mnt/')) return windowsPath; // 已是 WSL 路径
  if (!/^[A-Za-z]:[\\\/]/.test(windowsPath)) return windowsPath; // 非 Windows 路径
  return execSync(`wslpath -u "${windowsPath}"`, { encoding: 'utf8' }).trim();
}

// WSL 路径 → Windows 路径（供 attrib / curl 等命令使用）
function toWin(wslPath) {
  if (!wslPath) return wslPath;
  if (!wslPath.startsWith('/mnt/')) return wslPath;
  try {
    return execSync(`wslpath -w "${wslPath}"`, { encoding: 'utf8' }).trim();
  } catch {
    return wslPath;
  }
}

// ============================================================
// SVG 获取（GitHub Raw CDN + curl）
// type: 'filled' 或 'outline'（Tabler 有 1000 个 filled 图标，优先使用）
// ============================================================
async function fetchSvg(tablerName, type = 'outline') {
  const url = `https://raw.githubusercontent.com/tabler/tabler-icons/master/icons/${type}/${tablerName}.svg`;
  try {
    const data = execSync(
      `curl -sfL "${url}"`,
      { encoding: 'utf8', timeout: 15000 }
    );
    if (!data.includes('<svg')) throw new Error(`Invalid SVG for "${tablerName}"`);
    return data;
  } catch (e) {
    throw new Error(`下载 SVG "${tablerName}" 失败: ${e.message}`);
  }
}

// ============================================================
// SVG 着色（替换 currentColor / stroke / fill 为目标色）
// ============================================================
function svgColorize(svgText, rgb) {
  const [r, g, b] = rgb;
  const hex = `#${r.toString(16).padStart(2, '0')}${g.toString(16).padStart(2, '0')}${b.toString(16).padStart(2, '0')}`;

  return svgText
    .replace(/currentColor/g, hex)
    .replace(/(stroke|fill)="([^"]*)"/g, (_, attr, val) => {
      const lower = val.toLowerCase().trim();
      if (lower === 'none' || lower === 'transparent') return `${attr}="none"`;
      if ((val.startsWith('#') && val.length !== 4) || val.startsWith('rgb') || val.startsWith('hsl')) {
        return `${attr}="${val}"`; // 保留已格式化的颜色
      }
      return `${attr}="${hex}"`;
    });
}

// ============================================================
// SVG → PNG（resvg-js，支持透明）
// ============================================================
function renderSvgToPng(svgText, width, height) {
  const resvg = new Resvg(svgText, {
    fitTo: { mode: 'width', value: width },
  });
  return resvg.render().asPng();
}

// ============================================================
// SVG 加圆形徽章底衬（方案C）
// 在原始 SVG 前面插入一个 <circle> 背景层，图标叠加在上方
// 底衬颜色统一为浅灰（#F0F0F4），柔和且适配各种深色主题
// viewBox 扩大到 30x30，圆形 r=14（半径约为 viewBox 的 46.7%）
// 图标内容居中显示，圆形边缘略超出图标内容形成底衬效果
// ============================================================
function wrapWithBadge(svgText, bgColor) {
  const badgeCircle = `<circle cx="12" cy="12" r="10.5" fill="${bgColor}"/>`;
  return svgText.replace(/^(<svg[^>]*>)/m, `$1\n${badgeCircle}\n`);
}

// ============================================================
// 多尺寸 PNG → ICO 文件（PNG-in-ICO）
// ============================================================
function buildIco(pngBuffers, outputPath) {
  const sizes = [16, 32, 48, 256];
  const pngData = sizes.map((size, i) => ({
    size,
    data: pngBuffers[i] || pngBuffers[pngBuffers.length - 1],
  }));

  const headerSize = 6;
  const dirEntrySize = 16;
  let offset = headerSize + pngData.length * dirEntrySize;

  const dirEntries = pngData.map(({ size, data }) => {
    const w = size >= 256 ? 0 : size;
    const h = size >= 256 ? 0 : size;
    const entry = Buffer.alloc(16);
    entry.writeUInt8(w, 0);
    entry.writeUInt8(h, 1);
    entry.writeUInt8(0, 2);         // color count
    entry.writeUInt8(0, 3);         // reserved
    entry.writeUInt16LE(1, 4);      // color planes
    entry.writeUInt16LE(32, 6);     // bits per pixel
    entry.writeUInt32LE(data.length, 8);
    entry.writeUInt32LE(offset, 12);
    offset += data.length;
    return entry;
  });

  const ico = Buffer.concat([
    Buffer.from([0, 0, 1, 0, pngData.length & 0xff, (pngData.length >> 8) & 0xff]),
    ...dirEntries,
    ...pngData.map((p) => p.data),
  ]);

  fs.writeFileSync(outputPath, ico);
}

// ============================================================
// 完整生成单个 .ico
// filled 图标使用 Tabler 的 icons/filled/ 目录，其余用 outline
// ============================================================
async function makeIcon(iconName, rgb, outputDir) {
  if (!ICON_TO_TABLER[iconName]) {
    throw new Error(`未知图标名: ${iconName}，请先在 ICON_TO_TABLER 中注册`);
  }

  const tablerName = ICON_TO_TABLER[iconName];
  const svgType = FILLED_ICONS.has(iconName) ? 'filled' : 'outline';
  const svgText = await fetchSvg(tablerName, svgType);
  const coloredSvg = svgColorize(svgText, rgb);
  const badgedSvg = wrapWithBadge(coloredSvg, BADGE_BG);

  const sizes = [16, 32, 48, 256];
  const pngBuffers = sizes.map((size) => renderSvgToPng(badgedSvg, size, size));

  const outputPath = path.join(outputDir, iconName);
  buildIco(pngBuffers, outputPath);
  return outputPath;
}

// ============================================================
// 写入 desktop.ini（ANSI 编码）
// ============================================================
function writeDesktopIni(folderPathWsl, iconRelPath) {
  const iniContent = `[.ShellClassInfo]\r\nIconResource=${iconRelPath}\r\n`;
  const desktopIni = path.join(folderPathWsl, 'desktop.ini');

  // Node.js 不直接支持 ANSI，用 latin1（Windows 中文系统下等价于 cp936）
  fs.writeFileSync(desktopIni, iniContent, 'latin1');

  const desktopIniWin = toWin(desktopIni);
  const { spawnSync } = require('child_process');
  const result = spawnSync(
    '/mnt/c/Windows/System32/attrib.exe',
    ['+S', '+H', desktopIniWin],
    { windowsHide: true, timeout: 10000 }
  );
  if (result.status !== 0) {
    console.warn(`    ⚠ attrib +S +H 失败 (${result.status}): ${(result.stderr || '').toString().trim()}`);
  }
}

// ============================================================
// 设置文件夹 +S 属性
// ============================================================
function setFolderSystemAttr(folderPathWsl) {
  const folderWin = toWin(folderPathWsl);
  const { spawnSync } = require('child_process');
  const result = spawnSync(
    '/mnt/c/Windows/System32/attrib.exe',
    ['+S', folderWin],
    { windowsHide: true, timeout: 10000 }
  );
  if (result.status !== 0) {
    console.warn(`    ⚠ attrib +S 失败 (${result.status}): ${(result.stderr || '').toString().trim()}`);
  }
}

// ============================================================
// 刷新 Explorer
// ============================================================
function refreshExplorer() {
  const { spawnSync } = require('child_process');
  try {
    spawnSync(
      'powershell.exe',
      ['-Command', 'Rundll32 user32.dll,UpdatePerUserSystemParameters'],
      { windowsHide: true }
    );
  } catch (e) {
    // Ignore
  }
}

// ============================================================
// 加载配置
// ============================================================
function loadConfig(skillDir, cliConfig) {
  const configPaths = [
    cliConfig,
    path.join(skillDir, 'scripts', 'icon_config.yaml'),
    path.join(skillDir, 'scripts', 'icon_config.yml'),
  ].filter(Boolean);

  let cfg = { icon_dir: '.folder-icons', svg_source: 'tabler', explicit_mappings: [] };

  for (const p of configPaths) {
    try {
      if (fs.existsSync(p)) {
        const content = fs.readFileSync(p, 'utf8');
        cfg = yaml.load(content);
        break;
      }
    } catch (e) {
      // try next
    }
  }

  return cfg;
}

// ============================================================
// 主流程
// ============================================================
async function run(targetPathWsl, iconDirArg, configPath, dryRun, force) {
  // 所有 fs 操作使用 WSL 路径
  if (!fs.existsSync(targetPathWsl)) {
    console.error(`[ERROR] 目录不存在: ${targetPathWsl}`);
    return;
  }

  const skillDir = path.resolve(__dirname, '..');
  const cfg = loadConfig(skillDir, configPath);

  // 图标目录：目录名则相对于目标目录，绝对路径直接用
  const iconDirName = iconDirArg || cfg.icon_dir || '.folder-icons';
  const iconOutputDir = path.isAbsolute(iconDirName)
    ? iconDirName                          // 已是绝对路径（WSL 或 Windows）
    : path.join(targetPathWsl, iconDirName);

  // 本地图标目录（icon_source=local 时使用）
  const localIconDir = cfg.icon_local_dir
    ? (path.isAbsolute(cfg.icon_local_dir)
        ? cfg.icon_local_dir
        : toWsl(cfg.icon_local_dir))
    : null;

  const mappings = cfg.explicit_mappings || [];
  if (mappings.length === 0) {
    console.warn('[WARN] 配置文件中没有 explicit_mappings，什么都不做');
    return;
  }

  console.log(`[INFO] 目标目录: ${targetPathWsl}`);
  console.log(`[INFO] 图标目录: ${iconOutputDir}`);
  console.log();

  // 确保图标目录存在
  if (!dryRun && !fs.existsSync(iconOutputDir)) {
    fs.mkdirSync(iconOutputDir, { recursive: true });
    console.log(`[INFO] 图标目录已创建: ${iconOutputDir}`);
  }

  // 建立映射字典
  const mappingDict = {};
  for (const m of mappings) mappingDict[m.folder] = m;

  // 遍历子文件夹
  const subfolders = fs.readdirSync(targetPathWsl, { encoding: 'utf8' })
    .map((name) => ({ name, fullPath: path.join(targetPathWsl, name) }))
    .filter(({ name, fullPath }) => {
      try {
        return fs.statSync(fullPath).isDirectory() && !name.startsWith('.');
      } catch {
        return false;
      }
    })
    .sort((a, b) => a.name.localeCompare(b.name, 'zh-CN'));

  let processed = 0;

  for (const { name: folderName, fullPath: subfolderPath } of subfolders) {
    const m = mappingDict[folderName];
    if (!m) continue;

    const iconName = m.icon;
    const rgb = m.rgb;
    const colorDesc = m.color || '';
    const rgbStr = `[${rgb.join(', ')}]`;

    console.log(`${dryRun ? '[DRY]  ' : ''}[${folderName}] → ${iconName} ${rgbStr} ${colorDesc}`);

    if (dryRun) continue;

    // 1. 生成 .ico
    const iconPath = path.join(iconOutputDir, iconName);
    if (!fs.existsSync(iconPath) || force) {
      let generated = false;

      // 优先从本地图标目录复制（icon_source=local）
      if (localIconDir && fs.existsSync(localIconDir)) {
        const localSrc = path.join(localIconDir, iconName);
        if (fs.existsSync(localSrc)) {
          try {
            fs.copyFileSync(localSrc, iconPath);
            console.log(`    ✓ 复制本地图标: ${iconPath}`);
            generated = true;
          } catch (e) {
            console.warn(`    ⚠ 本地图标复制失败: ${e.message}，尝试从 Tabler 生成`);
          }
        }
      }

      // 本地没有 → 从 Tabler 生成
      if (!generated) {
        try {
          await makeIcon(iconName, rgb, iconOutputDir);
          console.log(`    ✓ 图标生成: ${iconPath}`);
        } catch (e) {
          console.error(`    ✗ 图标生成失败: ${e.message}`);
          continue;
        }
      }
    } else {
      console.log(`    → 已有图标，跳过生成（用 --force 强制重建）`);
    }

    // 2. 计算从子文件夹到图标的相对路径（Windows 反斜杠格式）
    const iconRelPath = path.relative(subfolderPath, iconPath).replace(/\//g, '\\');

    // 3. 写入 desktop.ini
    try {
      writeDesktopIni(subfolderPath, iconRelPath);
      console.log(`    ✓ desktop.ini 写入（IconResource=${iconRelPath}）`);
    } catch (e) {
      console.error(`    ✗ desktop.ini 写入失败: ${e.message}`);
    }

    // 4. 设置文件夹 +S 属性
    try {
      setFolderSystemAttr(subfolderPath);
      console.log(`    ✓ 文件夹 +S 属性已设置`);
    } catch (e) {
      console.error(`    ✗ 文件夹属性设置失败: ${e.message}`);
    }

    console.log();
    processed++;
  }

  console.log(`[DONE] ${processed} 个文件夹图标已应用`);
  if (processed > 0 && !dryRun) {
    console.log('请按 F5 刷新 Explorer 查看效果');
    refreshExplorer();
  }
}

// ============================================================
// CLI 入口
// ============================================================
function parseArgs(argv) {
  const args = { positional: [], flags: {} };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg.startsWith('--')) {
      const key = arg.slice(2);
      args.flags[key] = argv[i + 1] && !argv[i + 1].startsWith('--') ? argv[++i] : true;
    } else if (!arg.startsWith('-')) {
      args.positional.push(arg);
    }
  }
  return args;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));

  const [targetDir] = args.positional;
  if (!targetDir) {
    console.error('用法: node folder-icon.js "D:\\目标目录" [--dry-run] [--force] [--icon-dir "目录名"]');
    process.exit(1);
  }

  // 统一转为 WSL 路径（Node.js fs 全部用 WSL 路径）
  const resolvedTarget = toWsl(targetDir);

  await run(
    resolvedTarget,
    args.flags['icon-dir'],
    args.flags['config'],
    !!args.flags['dry-run'],
    !!args.flags['force']
  );
}

main().catch((e) => {
  console.error('[FATAL]', e.message);
  process.exit(1);
});