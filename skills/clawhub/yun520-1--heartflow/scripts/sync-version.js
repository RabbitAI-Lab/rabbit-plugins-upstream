#!/usr/bin/env node
// sync-version.js — 将版本号从 src/core/version.js 同步到其他文件
// 用法: node scripts/sync-version.js
// 在 prepublishOnly 中自动调用
//
// 同步目标：
//   1. 当前副本：package.json, VERSION
//   2. 镜像副本：/root/claude1/heartflow/ (package.json, VERSION, src/core/version.js)

'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const VERSION_FILE = path.join(ROOT, 'src', 'core', 'version.js');
const PACKAGE_FILE = path.join(ROOT, 'package.json');
const VERSION_TXT = path.join(ROOT, 'VERSION');

// 镜像副本路径（本地双副本架构）
const MIRROR_ROOT = '/root/claude1/heartflow';
const MIRROR_VERSION_FILE = path.join(MIRROR_ROOT, 'src', 'core', 'version.js');
const MIRROR_PACKAGE_FILE = path.join(MIRROR_ROOT, 'package.json');
const MIRROR_VERSION_TXT = path.join(MIRROR_ROOT, 'VERSION');

// 从 version.js 读取版本号（唯一真相源）
const versionContent = fs.readFileSync(VERSION_FILE, 'utf-8');
const match = versionContent.match(/const VERSION = '([^']+)'/);
if (!match) {
  console.error('ERROR: Cannot find version in src/core/version.js');
  process.exit(1);
}
const version = match[1];
console.log('Source version:', version);

// 同步 helper
function syncFile(filePath, newContent, label) {
  if (!fs.existsSync(filePath)) {
    fs.writeFileSync(filePath, newContent);
    console.log(`Created ${label} → ${version}`);
    return;
  }
  const existing = fs.readFileSync(filePath, 'utf-8');
  if (existing === newContent) {
    console.log(`${label} already at ${version}`);
  } else {
    fs.writeFileSync(filePath, newContent);
    console.log(`Updated ${label} → ${version}`);
  }
}

// ─── 同步当前副本 ────────────────────────────────────────────────────

// package.json
const pkg = JSON.parse(fs.readFileSync(PACKAGE_FILE, 'utf-8'));
if (pkg.version !== version) {
  pkg.version = version;
  fs.writeFileSync(PACKAGE_FILE, JSON.stringify(pkg, null, 2) + '\n');
  console.log('Updated package.json →', version);
} else {
  console.log('package.json already at', version);
}

// VERSION 纯文本文件
syncFile(VERSION_TXT, version + '\n', 'VERSION');

// ─── 同步镜像副本 ────────────────────────────────────────────────────

if (fs.existsSync(MIRROR_ROOT)) {
  console.log('\n--- Mirror sync: /root/claude1/heartflow ---');

  // version.js
  if (fs.existsSync(MIRROR_VERSION_FILE)) {
    const mirrorVersionContent = fs.readFileSync(MIRROR_VERSION_FILE, 'utf-8');
    const mirrorMatch = mirrorVersionContent.match(/const VERSION = '([^']+)'/);
    if (mirrorMatch && mirrorMatch[1] !== version) {
      const updated = mirrorVersionContent.replace(/const VERSION = '[^']+'/, `const VERSION = '${version}'`);
      fs.writeFileSync(MIRROR_VERSION_FILE, updated);
      console.log('Updated mirror/src/core/version.js →', version);
    } else if (!mirrorMatch) {
      console.log('WARNING: Cannot parse mirror version.js');
    } else {
      console.log('mirror/src/core/version.js already at', version);
    }
  }

  // package.json
  if (fs.existsSync(MIRROR_PACKAGE_FILE)) {
    const mirrorPkg = JSON.parse(fs.readFileSync(MIRROR_PACKAGE_FILE, 'utf-8'));
    if (mirrorPkg.version !== version) {
      mirrorPkg.version = version;
      fs.writeFileSync(MIRROR_PACKAGE_FILE, JSON.stringify(mirrorPkg, null, 2) + '\n');
      console.log('Updated mirror/package.json →', version);
    } else {
      console.log('mirror/package.json already at', version);
    }
  }

  // VERSION
  syncFile(MIRROR_VERSION_TXT, version + '\n', 'mirror/VERSION');
} else {
  console.log('\n(Skipping mirror: /root/claude1/heartflow not found)');
}

console.log('\nVersion sync complete:', version);
