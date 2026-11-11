#!/usr/bin/env node
/**
 * 六爻起卦 + 纳甲排盘脚本 —— 移植自 suansuan 项目 apps/web/src/lib/{bagua,liuyao-pai}.ts（一次性快照）。
 *
 * 用法：
 *   代用户摇卦（三枚硬币 × 6 爻）：
 *     node liuyao.cjs --cast [--question "所问之事"] [--date "2026-09-16 14:00"]
 *   用户自己摇过 / 报卦名：
 *     node liuyao.cjs --original 111011 --changed 111111 [--date ...]
 *     node liuyao.cjs --name 天风姤 [--changed-name 乾为天] [--date ...]
 *
 *   --date  起卦时间（默认当前时刻），格式同 bazi.cjs，默认按北京时间解释。
 *           起卦日的日干支决定六神起法与旬空。
 *
 * 卦 key 约定（与 data/bagua-hexagrams.json 一致）：
 *   6 位二进制 = 上卦三爻(四爻、五爻、上爻) + 下卦三爻(初爻、二爻、三爻)，
 *   每组内第一位是该卦的初位爻（自下而上），1=阳(实)、0=阴(断)。
 *
 * 输出：摇卦结果 + 本卦/变卦完整卦辞爻辞 + 纳甲排盘 JSON。
 * 解读规范见 references/liuyao-interpretation.md。
 */
'use strict';
const path = require('path');
const { Lunar } = require('./lib/lunar.js');

const DATA = (f) => path.join(__dirname, '..', 'data', f);
const hexagramData = require(DATA('bagua-hexagrams.json'));
const palaceData = require(DATA('bagua-gong.json'));

// ─── 基础常量（对应 liuyao-pai.ts）───

const TRIGRAM_BY_BITS = {
  '111': '乾', '110': '兑', '101': '离', '100': '震',
  '011': '巽', '010': '坎', '001': '艮', '000': '坤',
};

/** 每卦由初爻至三爻的纳甲；外卦同样由四爻至上爻。 */
const NAJIA = {
  乾: { inner: ['甲子', '甲寅', '甲辰'], outer: ['壬午', '壬申', '壬戌'] },
  坤: { inner: ['乙未', '乙巳', '乙卯'], outer: ['癸丑', '癸亥', '癸酉'] },
  震: { inner: ['庚子', '庚寅', '庚辰'], outer: ['庚午', '庚申', '庚戌'] },
  巽: { inner: ['辛丑', '辛亥', '辛酉'], outer: ['辛未', '辛巳', '辛卯'] },
  坎: { inner: ['戊寅', '戊辰', '戊午'], outer: ['戊申', '戊戌', '戊子'] },
  离: { inner: ['己卯', '己丑', '己亥'], outer: ['己酉', '己未', '己巳'] },
  艮: { inner: ['丙辰', '丙午', '丙申'], outer: ['丙戌', '丙子', '丙寅'] },
  兑: { inner: ['丁巳', '丁卯', '丁丑'], outer: ['丁亥', '丁酉', '丁未'] },
};

const BRANCH_ELEMENT = {
  子: '水', 亥: '水', 寅: '木', 卯: '木',
  巳: '火', 午: '火', 申: '金', 酉: '金',
  辰: '土', 戌: '土', 丑: '土', 未: '土',
};
const GENERATES = { 木: '火', 火: '土', 土: '金', 金: '水', 水: '木' };
const CONTROLS = { 木: '土', 土: '水', 水: '火', 火: '金', 金: '木' };
const SPIRITS = ['青龙', '朱雀', '勾陈', '螣蛇', '白虎', '玄武'];
const SPIRIT_START = { 甲: 0, 乙: 0, 丙: 1, 丁: 1, 戊: 2, 己: 3, 庚: 4, 辛: 4, 壬: 5, 癸: 5 };
const STAGES = ['本宫', '一世', '二世', '三世', '四世', '五世', '游魂', '归魂'];
const SHI_POSITIONS = [6, 1, 2, 3, 4, 5, 4, 3];
const JIAZI = Array.from({ length: 60 }, (_, index) =>
  '甲乙丙丁戊己庚辛壬癸'[index % 10] + '子丑寅卯辰巳午未申酉戌亥'[index % 12]);
const XUN_KONG = ['戌亥', '申酉', '午未', '辰巳', '寅卯', '子丑'];

/** 化进神对照（变爻地支在十二支序中前进且五行不变），反之为退神 */
const ADVANCE = { 寅: '卯', 巳: '午', 申: '酉', 亥: '子', 丑: '辰', 辰: '未', 未: '戌', 戌: '丑' };

function relativeOf(palace, line) {
  if (line === palace) return '兄弟';
  if (GENERATES[line] === palace) return '父母';
  if (GENERATES[palace] === line) return '子孙';
  if (CONTROLS[palace] === line) return '妻财';
  return '官鬼';
}

function findPalace(key) {
  for (const palace of palaceData) {
    const stage = palace.hexagrams.indexOf(key);
    if (stage >= 0) return { ...palace, stage };
  }
  throw new Error(`未知六爻卦象 key: ${key}`);
}

function getXunKong(dayGanZhi) {
  const index = JIAZI.indexOf(dayGanZhi);
  return index < 0 ? '' : XUN_KONG[Math.floor(index / 10)];
}

function lookupHexagram(key) {
  const entry = hexagramData.find((h) => h.key === key);
  if (!entry) throw new Error(`未知卦 key: ${key}`);
  return { key, ...entry.value };
}

function lookupByName(name) {
  const entry = hexagramData.find((h) => h.value.name === name);
  if (!entry) throw new Error(`未找到卦名: ${name}（可用如 乾为天/天风姤/火天大有 等 64 卦全名）`);
  return { key: entry.key, ...entry.value };
}

/**
 * 由本卦/变卦 key 与起卦日干支生成完整纳甲排盘。
 *
 * 爻序说明：key = 上卦组(四,五,上) + 下卦组(初,二,三)，
 * 故自初爻至上爻的阴阳 = key[3..5] + key[0..2]。
 * （suansuan 源码此处用整串 reverse，对含兑/震/巽/艮的非对称卦会把组内爻序颠倒，本脚本已修正。）
 */
function buildLiuyaoPai(originalKey, changedKey, dayGanZhi) {
  if (!/^[01]{6}$/.test(originalKey) || !/^[01]{6}$/.test(changedKey)) {
    throw new Error('六爻 key 必须是 6 位二进制字符串');
  }
  const palace = findPalace(originalKey);
  const upper = TRIGRAM_BY_BITS[originalKey.slice(0, 3)];
  const lower = TRIGRAM_BY_BITS[originalKey.slice(3)];
  const ganZhi = [...NAJIA[lower].inner, ...NAJIA[upper].outer];
  // 初爻到上爻的阴阳位：下卦组在前、上卦组在后
  const bitsBottomUp = [...originalKey.slice(3), ...originalKey.slice(0, 3)];
  const changedBottomUp = [...changedKey.slice(3), ...changedKey.slice(0, 3)];
  const shiPosition = SHI_POSITIONS[palace.stage];
  const yingPosition = ((shiPosition + 2) % 6) + 1;
  const xunKong = getXunKong(dayGanZhi);
  const spiritStart = SPIRIT_START[dayGanZhi[0]] ?? 0;

  const lines = ganZhi.map((value, index) => {
    const position = index + 1;
    const branch = value[1];
    const element = BRANCH_ELEMENT[branch];
    return {
      position,
      solid: bitsBottomUp[index] === '1',
      changing: bitsBottomUp[index] !== changedBottomUp[index],
      ganZhi: value,
      element,
      relative: relativeOf(palace.element, element),
      spirit: SPIRITS[(spiritStart + index) % 6],
      shiYing: position === shiPosition ? '世' : position === yingPosition ? '应' : null,
      xunKong: xunKong.includes(branch),
    };
  });

  return {
    palace: palace.palace,
    palaceElement: palace.element,
    palaceStage: STAGES[palace.stage],
    upperTrigram: upper,
    lowerTrigram: lower,
    dayGanZhi,
    xunKong,
    lines,
  };
}

/**
 * 动爻化出信息：变卦纳甲中同位爻的干支/五行/六亲（六亲仍以本卦宫五行论），
 * 及变爻对动爻的作用（回头生/回头克/化进神/化退神/比和/泄气等）。
 */
function buildChangedLines(originalKey, changedKey, paipan) {
  const lower2 = TRIGRAM_BY_BITS[changedKey.slice(3)];
  const upper2 = TRIGRAM_BY_BITS[changedKey.slice(0, 3)];
  if (!lower2 || !upper2) throw new Error(`未知变卦 key: ${changedKey}`);
  const ganZhi2 = [...NAJIA[lower2].inner, ...NAJIA[upper2].outer];
  const palaceEle = paipan.palaceElement;

  return paipan.lines
    .filter((l) => l.changing)
    .map((l) => {
      const changedGanZhi = ganZhi2[l.position - 1];
      const origBranch = l.ganZhi[1];
      const changedBranch = changedGanZhi[1];
      const origEle = BRANCH_ELEMENT[origBranch];
      const changedEle = BRANCH_ELEMENT[changedBranch];

      let relation;
      if (ADVANCE[origBranch] === changedBranch && origEle === changedEle) relation = '化进神';
      else if (ADVANCE[changedBranch] === origBranch && origEle === changedEle) relation = '化退神';
      else if (changedEle === origEle) relation = '比和';
      else if (GENERATES[changedEle] === origEle) relation = '回头生';
      else if (CONTROLS[changedEle] === origEle) relation = '回头克';
      else if (GENERATES[origEle] === changedEle) relation = '动爻生变爻(泄气)';
      else relation = '动爻克变爻';

      return {
        position: l.position,
        originalGanZhi: l.ganZhi,
        originalElement: origEle,
        originalRelative: l.relative,
        changedGanZhi,
        changedElement: changedEle,
        changedRelative: relativeOf(palaceEle, changedEle),
        relation,
        changedXunKong: paipan.xunKong.includes(changedBranch),
      };
    });
}

// ─── 三枚硬币摇卦（对应 bagua.ts tossCoin：老阳/少阴/少阳/老阴）───

function tossCoin() {
  const coins = [0, 0, 0].map(() => (Math.random() < 0.5 ? 0 : 1));
  const sum = coins[0] + coins[1] + coins[2];
  // upper=本卦位, lower=变卦位
  let upper, lower;
  if (sum === 0) { upper = '0'; lower = '1'; }       // 全阴 = 老阴（变）
  else if (sum === 3) { upper = '1'; lower = '0'; }  // 全阳 = 老阳（变）
  else if (sum === 1) { upper = '1'; lower = '1'; }  // 两阴一阳 = 少阳
  else { upper = '0'; lower = '0'; }                 // 两阳一阴 = 少阴
  return { upper, lower, coins };
}

/** 摇六次，yaos[0]=初爻 … yaos[5]=上爻；key 按 [上卦组][下卦组] 组装 */
function tossSixTimes() {
  const yaos = [];
  let originalLower = '', originalUpper = '', changedLower = '', changedUpper = '';
  for (let i = 0; i < 6; i++) {
    const r = tossCoin();
    yaos.push({ ...r, changing: r.upper !== r.lower });
    if (i < 3) { originalLower += r.upper; changedLower += r.lower; }
    else { originalUpper += r.upper; changedUpper += r.lower; }
  }
  return {
    original: originalUpper + originalLower,
    changed: changedUpper + changedLower,
    yaos,
  };
}

// ─── CLI ───

function parseArgs(argv) {
  const args = {};
  for (let i = 0; i < argv.length; i++) {
    const key = argv[i].replace(/^--/, '');
    const next = argv[i + 1];
    if (next !== undefined && !next.startsWith('--')) {
      args[key] = next;
      i++;
    } else {
      args[key] = true; // 布尔标志（如 --cast）
    }
  }
  return args;
}

function parseDate(str, tz) {
  const m = str.match(/^(\d{4})-(\d{1,2})-(\d{1,2})(?:[T ](\d{1,2}):(\d{1,2}))?$/);
  if (m) {
    const [, y, mo, d, h = 12, mi = 0] = m;
    return new Date(Date.UTC(+y, +mo - 1, +d, +h - tz, +mi));
  }
  const d = new Date(str);
  if (Number.isNaN(d.getTime())) throw new Error(`无法解析日期: ${str}`);
  return d;
}

function dayGanZhiOf(date) {
  const ec = Lunar.fromDate(date).getEightChar();
  return ec.getDayGan() + ec.getDayZhi();
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  const tz = args.tz !== undefined ? parseFloat(args.tz) : 8;
  const castDate = args.date ? parseDate(args.date, tz) : new Date();
  const dayGanZhi = dayGanZhiOf(castDate);

  let originalKey, changedKey, cast = null;
  if (args.cast) {
    cast = tossSixTimes();
    originalKey = cast.original;
    changedKey = cast.changed;
  } else if (args.original) {
    originalKey = args.original;
    changedKey = args.changed ?? args.original; // 无变爻则本卦=变卦
  } else if (args.name) {
    originalKey = lookupByName(args.name).key;
    changedKey = args.changedName ? lookupByName(args.changedName).key : originalKey;
  } else {
    console.error('用法: node liuyao.cjs --cast [--question "..."] [--date ...]  或  --original 111011 --changed 111111  或  --name 天风姤 [--changed-name 乾为天]');
    process.exit(1);
  }

  const original = lookupHexagram(originalKey);
  const changed = lookupHexagram(changedKey);
  const paipan = buildLiuyaoPai(originalKey, changedKey, dayGanZhi);
  const changedLines = buildChangedLines(originalKey, changedKey, paipan);
  const changingLines = paipan.lines.filter((l) => l.changing);
  // 变爻爻辞（数据 yao 数组按 初→上 排列）
  const changingYaoTexts = changingLines.map((l) => original.yao?.[l.position - 1] ?? null);

  console.log(JSON.stringify({
    question: args.question ?? null,
    castDate: castDate.toISOString(),
    dayGanZhi,
    cast, // null 表示非代摇（用户提供 key/卦名）
    originalHexagram: {
      name: original.name,
      key: original.key,
      gua_ci: original.gua_ci ?? '',
      xiang_ci: original.xiang_ci ?? '',
      tuan_ci: original.tuan_ci ?? '',
      modern_description: original.modern_description ?? '',
    },
    changedHexagram: {
      name: changed.name,
      key: changed.key,
      gua_ci: changed.gua_ci ?? '',
      xiang_ci: changed.xiang_ci ?? '',
      modern_description: changed.modern_description ?? '',
    },
    changingYaoTexts,
    changedLines,
    paipan,
  }, null, 2));
}

main();
