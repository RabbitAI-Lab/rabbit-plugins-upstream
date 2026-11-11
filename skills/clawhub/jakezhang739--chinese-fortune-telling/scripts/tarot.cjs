#!/usr/bin/env node
/**
 * 塔罗抽牌脚本 —— 移植自 suansuan 项目 apps/web/src/lib/tarot.ts（一次性快照）。
 *
 * 用法：
 *   代用户抽牌（不重复，每张 50% 逆位）：
 *     node tarot.cjs --draw [--spread "过去,现在,未来"] [--n 3]
 *   用户自己抽好了，查牌义：
 *     node tarot.cjs --cards "宝剑十,月亮,星星" [--reversed "0,1,0"]
 *
 *   --spread   牌阵位置名，逗号分隔（个数决定抽几张，默认 过去,现在,未来）
 *   --cards    逗号分隔的牌名（须与 data/tarot-cards.json 的 name 一致）
 *   --reversed 逗号分隔的 0/1，1=逆位（默认全部正位）
 *
 * 输出：[{ position, reversed, card: 完整牌义 }] JSON。
 * 解读规范见 references/tarot-interpretation.md。
 */
'use strict';
const path = require('path');

const tarotData = require(path.join(__dirname, '..', 'data', 'tarot-cards.json'));

function parseArgs(argv) {
  const args = {};
  for (let i = 0; i < argv.length; i++) {
    const key = argv[i].replace(/^--/, '');
    const next = argv[i + 1];
    if (next !== undefined && !next.startsWith('--')) {
      args[key] = next;
      i++;
    } else {
      args[key] = true; // 布尔标志（如 --draw）
    }
  }
  return args;
}

function drawCards(names) {
  const positions = [];
  const pool = [...tarotData];
  for (let i = 0; i < names.length; i++) {
    const idx = Math.floor(Math.random() * pool.length);
    const card = pool.splice(idx, 1)[0];
    card.reversed = Math.random() > 0.5;
    positions.push({ position: names[i], ...card });
  }
  return positions;
}

function lookupCards(names, reversedFlags) {
  return names.map((name, i) => {
    const card = tarotData.find((c) => c.name === name);
    if (!card) {
      const hint = tarotData
        .filter((c) => c.name.includes(name.slice(0, 1)))
        .slice(0, 5)
        .map((c) => c.name)
        .join('、');
      throw new Error(`未找到牌名「${name}」（相近的牌：${hint || '请核对 78 张牌全名，如 宝剑十/愚者/命运之轮'}）`);
    }
    return {
      position: `第${i + 1}张`,
      reversed: reversedFlags[i] === 1,
      ...card,
    };
  });
}

function main() {
  const args = parseArgs(process.argv.slice(2));

  let result;
  if (args.draw) {
    const positions = (args.spread ?? '过去,现在,未来').split(',').map((s) => s.trim()).filter(Boolean);
    result = drawCards(positions);
  } else if (args.cards) {
    const names = args.cards.split(',').map((s) => s.trim()).filter(Boolean);
    const flags = (args.reversed ?? '').split(',').map((s) => parseInt(s, 10) || 0);
    result = lookupCards(names, flags);
  } else {
    console.error('用法: node tarot.cjs --draw [--spread "过去,现在,未来"]  或  --cards "宝剑十,月亮,星星" [--reversed "0,1,0"]');
    process.exit(1);
  }

  console.log(JSON.stringify(result, null, 2));
}

main();
