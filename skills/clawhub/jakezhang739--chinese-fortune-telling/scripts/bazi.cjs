#!/usr/bin/env node
/**
 * 八字排盘脚本 —— 移植自 suansuan 项目 apps/server/src/bazi/（一次性快照）。
 *
 * 用法：
 *   node bazi.cjs --date "1990-01-15 12:00" [--gender male|female] [--lon 104.07] [--tz 8]
 *
 *   --date    公历生日，"YYYY-MM-DD HH:mm"（默认按东八区/北京时间解释）
 *             也接受带时区的 ISO 串（如 1990-01-15T12:00:00+08:00）
 *   --gender  大运用（男顺女逆），缺省 male
 *   --lon     出生地经度（东经为正，如成都 104.07）。提供则做真太阳时校正
 *   --tz      输入时间所属时区（默认 8，即北京时间）
 *
 * 输出：完整命盘 JSON（四柱/五行分布/日主强弱/神煞/胎元命宫/大运/调候/称骨/五维评分）。
 * 解读规范见 skill 的 references/bazi-interpretation.md 与 persona-and-style.md。
 */
'use strict';
const path = require('path');
const { Lunar } = require('./lib/lunar.js');

const DATA = (f) => path.join(__dirname, '..', 'data', f);
const chengguWeights = require(DATA('chenggu-weights.json'));
const shenshaRules = require(DATA('shensha-rules.json'));

// ─── 常量（对应 suansuan bazi/constants.ts）───

const GAN_WUXING = {
  甲: '木', 乙: '木', 丙: '火', 丁: '火', 戊: '土',
  己: '土', 庚: '金', 辛: '金', 壬: '水', 癸: '水',
};

const ZHI_HIDDEN = {
  子: { 主气: '水', 藏干: ['癸'] },
  丑: { 主气: '土', 藏干: ['己', '癸', '辛'] },
  寅: { 主气: '木', 藏干: ['甲', '丙', '戊'] },
  卯: { 主气: '木', 藏干: ['乙'] },
  辰: { 主气: '土', 藏干: ['戊', '乙', '癸'] },
  巳: { 主气: '火', 藏干: ['丙', '庚', '戊'] },
  午: { 主气: '火', 藏干: ['丁', '己'] },
  未: { 主气: '土', 藏干: ['己', '丁', '乙'] },
  申: { 主气: '金', 藏干: ['庚', '壬', '戊'] },
  酉: { 主气: '金', 藏干: ['辛'] },
  戌: { 主气: '土', 藏干: ['戊', '辛', '丁'] },
  亥: { 主气: '水', 藏干: ['壬', '甲'] },
};

const WUXING_RELATION = {
  相生: { 木: '火', 火: '土', 土: '金', 金: '水', 水: '木' },
  被生: { 火: '木', 土: '火', 金: '土', 水: '金', 木: '水' },
  相克: { 木: '土', 土: '水', 水: '火', 火: '金', 金: '木' },
  被克: { 土: '木', 水: '土', 火: '水', 金: '火', 木: '金' },
};

const WUXING_DIRECTION = {
  木: { 正位: '东方', 八卦: '震' },
  火: { 正位: '南方', 八卦: '离' },
  金: { 正位: '西方', 八卦: '兑' },
  水: { 正位: '北方', 八卦: '坎' },
  土: { 正位: '中央', 八卦: ['坤', '艮'] },
};

const SEASON_MAP = {
  春: { 旺: ['木'], 相: ['火'], 休: ['水'], 囚: ['金'], 死: ['土'] },
  夏: { 旺: ['火'], 相: ['土'], 休: ['木'], 囚: ['水'], 死: ['金'] },
  秋: { 旺: ['金'], 相: ['水'], 休: ['土'], 囚: ['火'], 死: ['木'] },
  冬: { 旺: ['水'], 相: ['木'], 休: ['金'], 囚: ['土'], 死: ['火'] },
  季春: { 旺: ['土'], 相: ['金'], 休: ['火'], 囚: ['木'], 死: ['水'] },
  季夏: { 旺: ['土'], 相: ['金'], 休: ['火'], 囚: ['木'], 死: ['水'] },
  季秋: { 旺: ['土'], 相: ['金'], 休: ['火'], 囚: ['木'], 死: ['水'] },
  季冬: { 旺: ['土'], 相: ['金'], 休: ['火'], 囚: ['木'], 死: ['水'] },
};

const BRANCH_SEASON = {
  寅: '春', 卯: '春', 辰: '季春', 巳: '夏', 午: '夏', 未: '季夏',
  申: '秋', 酉: '秋', 戌: '季秋', 亥: '冬', 子: '冬', 丑: '季冬',
};

// ─── 真太阳时（对应 true-solar-time.ts，NOAA 近似公式）───

const REFERENCE_LONGITUDE = 120;

function equationOfTime(date) {
  const dayOfYear = Math.floor(
    (date.getTime() - Date.UTC(date.getUTCFullYear(), 0, 0)) / 86400000,
  );
  const B = (2 * Math.PI * (dayOfYear - 81)) / 365;
  return 9.87 * Math.sin(2 * B) - 7.53 * Math.cos(B) - 1.5 * Math.sin(B);
}

function toTrueSolarDate(localDate, longitude) {
  if (longitude === null || longitude === undefined || Number.isNaN(longitude)) return localDate;
  const longitudeDeltaMin = (longitude - REFERENCE_LONGITUDE) * 4; // 每度 4 分钟
  const eotMin = equationOfTime(localDate);
  return new Date(localDate.getTime() + (longitudeDeltaMin + eotMin) * 60000);
}

// ─── 排四柱（对应 compute.ts）───

function computeEightChar(birthDate, longitude) {
  const solarDate = toTrueSolarDate(birthDate, longitude);
  const lunar = Lunar.fromDate(solarDate);
  const ec = lunar.getEightChar();

  const buildPillar = (gan, zhi, shiShenZhi, shiShenGan, hideGan, naYin, xun, xunKong, diShi) => ({
    Gan: gan,
    Zhi: zhi,
    WuXing: [GAN_WUXING[gan] ?? '土', ZHI_HIDDEN[zhi]?.主气 ?? '土'],
    ShiShenZhi: shiShenZhi,
    ShiShenGan: shiShenGan,
    HideGan: hideGan,
    NaYin: naYin,
    Xun: xun,
    XunKong: xunKong,
    DiShi: diShi,
  });

  const year = buildPillar(
    ec.getYearGan(), ec.getYearZhi(), ec.getYearShiShenZhi(), ec.getYearShiShenGan(),
    ec.getYearHideGan(), ec.getYearNaYin(), lunar.getYearXun(), lunar.getYearXunKong(), ec.getYearDiShi(),
  );
  const month = buildPillar(
    ec.getMonthGan(), ec.getMonthZhi(), ec.getMonthShiShenZhi(), ec.getMonthShiShenGan(),
    ec.getMonthHideGan(), ec.getMonthNaYin(), lunar.getMonthXun(), lunar.getMonthXunKong(), ec.getMonthDiShi(),
  );
  const day = {
    ...buildPillar(
      ec.getDayGan(), ec.getDayZhi(), ec.getDayShiShenZhi(), ec.getDayShiShenGan(),
      ec.getDayHideGan(), ec.getDayNaYin(), lunar.getDayXun(), lunar.getDayXunKong(), ec.getDayDiShi(),
    ),
    Chong: lunar.getDayChong(),
    ChongGan: lunar.getDayChongGan(),
  };
  const time = {
    ...buildPillar(
      ec.getTimeGan(), ec.getTimeZhi(), ec.getTimeShiShenZhi(), ec.getTimeShiShenGan(),
      ec.getTimeHideGan(), ec.getTimeNaYin(), lunar.getTimeXun(), lunar.getTimeXunKong(), ec.getTimeDiShi(),
    ),
    Chong: lunar.getTimeChong(),
    ChongGan: lunar.getTimeChongGan(),
  };
  return { year, month, day, time };
}

function toFlatBazi(ec) {
  return {
    yearGan: ec.year.Gan, yearZhi: ec.year.Zhi,
    monthGan: ec.month.Gan, monthZhi: ec.month.Zhi,
    dayGan: ec.day.Gan, dayZhi: ec.day.Zhi,
    hourGan: ec.time.Gan, hourZhi: ec.time.Zhi,
  };
}

// ─── 五行强度（对应 analyze.ts）───

function getSeasonScore(seasonStatus, element) {
  if (seasonStatus.旺.includes(element)) return 3;
  if (seasonStatus.相.includes(element)) return 2;
  if (seasonStatus.休.includes(element)) return 1;
  return 0;
}

function analyzeGan(ec, dayElement, scores) {
  ['year', 'month', 'day', 'time'].forEach((pillar) => {
    const elem = ec[pillar].WuXing[0];
    const isDayPillar = pillar === 'day';
    const tenGod = ec[pillar].ShiShenGan;
    const weight = isDayPillar ? 1.5 : 1;
    if (elem === dayElement) {
      if (['比肩', '劫财'].includes(tenGod)) scores.same += weight * 1.2;
      return;
    }
    if (WUXING_RELATION.被生[dayElement] === elem) {
      if (['正印', '偏印'].includes(tenGod)) scores.produce += weight * 1.5;
      else scores.produce += weight * 0.5;
    }
  });
}

function analyzeZhi(ec, dayElement, scores) {
  ['year', 'month', 'day', 'time'].forEach((pillar) => {
    const isDayPillar = pillar === 'day';
    const zhiInfo = ZHI_HIDDEN[ec[pillar].Zhi];
    if (!zhiInfo) return;
    if (zhiInfo.主气 === dayElement) scores.root += isDayPillar ? 2 : 1;
    const weights = [1, 0.5, 0.3]; // 本/中/余气
    ec[pillar].HideGan.forEach((gan, index) => {
      const elem = GAN_WUXING[gan];
      const weight = weights[Math.min(index, 2)];
      if (elem && elem === dayElement) scores.root += weight * (isDayPillar ? 1.5 : 1);
    });
  });
}

function analyzeClash(ec, dayElement, scores) {
  const { Chong: dayChong, ChongGan: dayChongGan } = ec.day;
  const { Chong: timeChong, ChongGan: timeChongGan } = ec.time;
  if (dayChong && ZHI_HIDDEN[dayChong]?.主气 === dayElement) scores.clash -= 0.8;
  if (dayChongGan && GAN_WUXING[dayChongGan] === dayElement) scores.clash -= 0.6;
  if (timeChong && ZHI_HIDDEN[timeChong]?.主气 === dayElement) scores.clash -= 0.5;
  if (timeChongGan && GAN_WUXING[timeChongGan] === dayElement) scores.clash -= 0.4;
}

function getStrengthLevel(score) {
  if (score >= 4.0) return '极强';
  if (score >= 3.0) return '偏强';
  if (score >= 2.0) return '中和';
  if (score >= 1.0) return '偏弱';
  return '过弱';
}

function getChongElement(element) {
  return { 金: '火', 木: '金', 水: '土', 火: '水', 土: '木' }[element];
}

function getBalanceElement(element) {
  return { 金: '土金', 木: '水木', 水: '金水', 火: '木火', 土: '火土' }[element];
}

function getWeakSupportColor(element) {
  return { 金: '白/金', 木: '青/绿', 水: '黑/蓝', 火: '红/紫', 土: '黄/棕' }[element];
}

function generateAdvice(element, score) {
  const level = getStrengthLevel(score);
  const rel = WUXING_RELATION;
  const dir = WUXING_DIRECTION;
  const map = {
    极强: `此造${element}势极盛，宜取${rel.相克[element]}气制其锋芒，以${rel.相生[element]}气泄其旺气。尤忌${getChongElement(element)}方冲克，可配${getWeakSupportColor(rel.被克[element])}色衣物调节。`,
    偏强: `此造${element}气偏旺，需${rel.相克[element]}气来约制，辅以${rel.相生[rel.相克[element]]}气流通气势。${['金', '木'].includes(element) ? '慎用利器' : '避免潮湿'}等${getChongElement(element)}相关物象。`,
    中和: `此造${element}气中和，最喜${rel.相生[element]}气缓缓生助，兼得${rel.相克[element]}气适度约制。宜佩戴${getBalanceElement(element)}材质饰品维持平衡。`,
    偏弱: `此造${element}势偏衰，当以${rel.被生[element]}气滋养根基，配合${element}行比劫助力。忌见${rel.被克[element]}气过重，${dir[getChongElement(element)].正位}(${getChongElement(element)}煞)方位不宜久居。`,
    过弱: `此造${element}气衰极，需借${rel.被克[rel.被克[element]]}之势从弱取用，多聚${rel.被生[element]}气之生助。宜用${getWeakSupportColor(element)}色增强气场，远离${getChongElement(element)}相冲之物。`,
  };
  return map[level] ?? '五行平衡，顺其自然即可';
}

function analyzeStrength(ec) {
  const dayElement = ec.day.WuXing[0];
  const scores = { season: 0, same: 0, produce: 0, root: 0, sound: 0, clash: 0 };
  const birthSeason = BRANCH_SEASON[ec.month.Zhi] ?? '未知季节';
  const seasonStatus = SEASON_MAP[birthSeason];
  if (seasonStatus) scores.season = getSeasonScore(seasonStatus, dayElement);
  analyzeGan(ec, dayElement, scores);
  analyzeZhi(ec, dayElement, scores);
  analyzeClash(ec, dayElement, scores);
  const total =
    scores.season * 0.4 +
    (scores.same + scores.produce) * 0.25 +
    (scores.root + scores.sound) * 0.25 +
    scores.clash * 0.1;
  return {
    dayElement,
    strength: getStrengthLevel(total),
    advice: generateAdvice(dayElement, total),
    debug: { scores, total },
  };
}

function analyzeWuxingDistribution(ec) {
  const counts = { 金: 0, 木: 0, 水: 0, 火: 0, 土: 0 };
  ['year', 'month', 'day', 'time'].forEach((p) => {
    counts[ec[p].WuXing[0]]++;
    counts[ec[p].WuXing[1]]++;
  });
  Object.keys(counts).forEach((k) => {
    counts[k] = Math.round((counts[k] / 8) * 100);
  });
  return counts;
}

// ─── 神煞（对应 shensha.ts，规则在 data/shensha-rules.json）───

function findShensha(bazi, data = shenshaRules) {
  const TIAN_GAN = new Set(['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']);
  const DI_ZHI = new Set(['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']);
  const result = [];
  for (const shenshaName of Object.keys(data)) {
    const shenshaInfo = data[shenshaName];
    const { check, rule } = shenshaInfo;
    let matched = false;

    if (shenshaName === '阴阳煞') {
      const yinyangMap = {
        甲: '阳', 乙: '阴', 丙: '阳', 丁: '阴', 戊: '阳',
        己: '阴', 庚: '阳', 辛: '阴', 壬: '阳', 癸: '阴',
      };
      const gans = [bazi.yearGan, bazi.monthGan, bazi.dayGan, bazi.hourGan];
      const allYang = gans.every((g) => yinyangMap[g] === '阳');
      const allYin = gans.every((g) => yinyangMap[g] === '阴');
      if (allYang || allYin) result.push({ key: shenshaName, ...shenshaInfo });
      continue;
    }

    for (const [condition, requiredValues] of Object.entries(rule)) {
      const conditionElements = Array.from(condition);
      for (const part of check) {
        const partValue = bazi[part];
        if (!partValue) continue;
        if (conditionElements.includes(partValue)) {
          let targetPart;
          if (TIAN_GAN.has(requiredValues[0])) targetPart = 'dayGan';
          else if (DI_ZHI.has(requiredValues[0])) targetPart = part.replace('Gan', 'Zhi');
          else continue;
          const targetValue = bazi[targetPart];
          if (targetValue && requiredValues.includes(targetValue)) {
            matched = true;
            break;
          }
        }
      }
      if (matched) break;
    }
    if (matched) result.push({ key: shenshaName, ...shenshaInfo });
  }
  return result;
}

// ─── 胎元/命宫/身宫 + 大运（基于 lunar-javascript EightChar API）───

function computeSpecialPillars(birthDate) {
  const ec = Lunar.fromDate(birthDate).getEightChar();
  return {
    taiYuan: ec.getTaiYuan(),
    taiYuanNaYin: ec.getTaiYuanNaYin(),
    mingGong: ec.getMingGong(),
    mingGongNaYin: ec.getMingGongNaYin(),
    shenGong: ec.getShenGong(),
    shenGongNaYin: ec.getShenGongNaYin(),
    taiXi: ec.getTaiXi(),
    taiXiNaYin: ec.getTaiXiNaYin(),
  };
}

function computeYun(birthDate, gender = 'male') {
  const ec = Lunar.fromDate(birthDate).getEightChar();
  const g = gender === 'female' ? 0 : 1;
  const yun = ec.getYun(g);
  return {
    gender: g,
    startYear: yun.getStartYear(),
    startMonth: yun.getStartMonth(),
    startDay: yun.getStartDay(),
    daYun: yun.getDaYun().map((dy) => ({
      ganZhi: dy.getGanZhi(),
      startAge: dy.getStartAge(),
      endAge: dy.getEndAge(),
      startYear: dy.getStartYear(),
      endYear: dy.getEndYear(),
      index: dy.getIndex(),
    })),
  };
}

// ─── 调候简化版（对应 compute-enhanced.ts）───

function getSeason(monthZhi) {
  if (['寅', '卯', '辰'].includes(monthZhi)) return '春';
  if (['巳', '午', '未'].includes(monthZhi)) return '夏';
  if (['申', '酉', '戌'].includes(monthZhi)) return '秋';
  return '冬';
}

const TIAOHU_HINTS = {
  木: {
    春: '春木当令旺极，宜火泄秀、金修剪，忌水再生。',
    夏: '夏木火旺木渴，宜水润泽、湿土培根。',
    秋: '秋木逢金克，宜水化杀生身，忌金再克。',
    冬: '冬水寒木冻，宜火暖局、土实根。',
  },
  火: {
    春: '春木旺生火，火势渐旺，宜土泄火、水济火。',
    夏: '夏火当令极旺，宜水制火、湿土泄火，忌木再生。',
    秋: '秋金旺火退，宜木生火、火助身。',
    冬: '冬水旺火弱，宜木化水生火、火助身暖局。',
  },
  土: {
    春: '春木旺土虚，宜火生土、土助身，忌木再克。',
    夏: '夏火旺土燥，宜水润土、金泄土，忌火再生。',
    秋: '秋金旺土泄，宜火生土、土助身。',
    冬: '冬水旺土寒，宜火暖土、土实根。',
  },
  金: {
    春: '春木旺金弱，宜土生金、金助身，忌火再克。',
    夏: '夏火旺金熔，宜湿土生金、水制火，忌木再生火。',
    秋: '秋金当令旺极，宜火锻炼、水泄秀，忌土再生。',
    冬: '冬水旺金寒，宜土生金、火暖局，忌水再泄。',
  },
  水: {
    春: '春木旺水泄，宜金生水、水助身。',
    夏: '夏火旺水竭，宜金生水、水助身，忌土再克。',
    秋: '秋金旺水旺，宜火暖局、木泄秀，忌金再生。',
    冬: '冬水当令极旺，宜土制水、火暖局，忌金再生。',
  },
};

function computeTiaoHouSimple(dayGan, monthZhi) {
  const dayElement = GAN_WUXING[dayGan] ?? '土';
  const season = getSeason(monthZhi);
  return { level: 'simple', dayElement, monthZhi, hint: TIAOHU_HINTS[dayElement][season] };
}

// ─── 称骨（袁天罡标准版，对应 chenggu.ts，权重表在 data/chenggu-weights.json）───

const CN_NUM = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十'];

function toCn(n) {
  if (n <= 10) return CN_NUM[n];
  if (n < 20) return '十' + (n % 10 === 0 ? '' : CN_NUM[n % 10]);
  const tens = Math.floor(n / 10);
  const ones = n % 10;
  return CN_NUM[tens] + '十' + (ones === 0 ? '' : CN_NUM[ones]);
}

function computeChenggu(lunar) {
  const yearGanZhi = lunar.getYearInGanZhi();
  const month = Math.abs(lunar.getMonth()); // 闰月沿用本月重量
  const day = lunar.getDay();
  const timeZhi = lunar.getEightChar().getTimeZhi();

  const y = chengguWeights.year[yearGanZhi] ?? 0;
  const m = chengguWeights.month[String(month)] ?? 0;
  const d = chengguWeights.day[String(day)] ?? 0;
  const h = chengguWeights.hour[timeZhi] ?? 0;

  const totalQian = y + m + d + h;
  const liang = Math.floor(totalQian / 10);
  const qian = totalQian % 10;
  return {
    totalQian,
    liang,
    qian,
    weightText: `${toCn(liang)}两${qian === 0 ? '' : toCn(qian) + '钱'}`,
    lyric: chengguWeights.lyrics[String(totalQian)] ?? chengguWeights.lyricsFallback,
    breakdown: { year: y, month: m, day: d, hour: h },
  };
}

// ─── 五维评分（对应 analyze.ts analyzeLifeScores）───

function analyzeLifeScores(strength, shensha) {
  const clamp = (n) => Math.max(0, Math.min(100, Math.round(n)));
  const baseByStrength = { 极强: 66, 偏强: 72, 中和: 78, 偏弱: 65, 过弱: 58 };
  const base = baseByStrength[strength.strength];
  const auspicious = shensha.filter((i) => i.type === '吉').length;
  const inauspicious = shensha.filter((i) => i.type === '凶').length;
  const shenshaDelta = Math.max(-12, Math.min(12, auspicious * 2 - inauspicious * 2));
  const has = (re) => shensha.some((i) => re.test(i.key));

  const raw = {
    career: base + shenshaDelta + (has(/文昌|国印|将星|天乙/) ? 7 : 0),
    wealth: base - 2 + shenshaDelta + (has(/禄|金舆|福星/) ? 7 : 0),
    marriage: base - 1 + Math.round(shenshaDelta / 2) + (has(/桃花|红鸾|天喜/) ? 8 : 0),
    health: base + 4 - inauspicious * 2 + (strength.strength === '中和' ? 6 : 0),
    personality: base + 2 + auspicious + (has(/华盖|文昌/) ? 5 : 0),
  };

  const dimensions = [
    { key: 'career', label: '事业', score: clamp(raw.career), comment: '看行动力、贵人助力与事业承压能力。' },
    { key: 'wealth', label: '财运', score: clamp(raw.wealth), comment: '看资源整合、守成能力与财星承载。' },
    { key: 'marriage', label: '姻缘', score: clamp(raw.marriage), comment: '看关系互动、情感表达与缘分助力。' },
    { key: 'health', label: '健康', score: clamp(raw.health), comment: '看五行平衡与日主的恢复能力。' },
    { key: 'personality', label: '性情', score: clamp(raw.personality), comment: '看心性稳定、学习力与自我调节。' },
  ];
  const average = Math.round(dimensions.reduce((s, i) => s + i.score, 0) / dimensions.length);
  return {
    dimensions,
    average,
    summary:
      average >= 75
        ? '整体格局较为均衡，宜顺势发挥长处，同时以持续行动巩固优势。'
        : average >= 65
          ? '整体有进有守，关键在于补足短板、把握节奏，不宜急于求成。'
          : '先天结构起伏较明显，更宜重视长期积累、生活规律与现实支持。',
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
      args[key] = true;
    }
  }
  return args;
}

/** 把 "YYYY-MM-DD HH:mm" 按 tz 时区转成 Date；带时区的 ISO 串直接解析 */
function parseDate(str, tz) {
  const m = str.match(/^(\d{4})-(\d{1,2})-(\d{1,2})[T ](\d{1,2}):(\d{1,2})$/);
  if (m) {
    const [, y, mo, d, h, mi] = m;
    return new Date(Date.UTC(+y, +mo - 1, +d, +h - tz, +mi));
  }
  const d = new Date(str);
  if (Number.isNaN(d.getTime())) throw new Error(`无法解析日期: ${str}`);
  return d;
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.date) {
    console.error('用法: node bazi.cjs --date "1990-01-15 12:00" [--gender male|female] [--lon 104.07] [--tz 8]');
    process.exit(1);
  }
  const tz = args.tz !== undefined ? parseFloat(args.tz) : 8;
  const gender = args.gender === 'female' ? 'female' : 'male';
  const lon = args.lon !== undefined ? parseFloat(args.lon) : null;
  const birthDate = parseDate(args.date, tz);

  const eightChar = computeEightChar(birthDate, lon);
  const flat = toFlatBazi(eightChar);
  const wuxing = analyzeWuxingDistribution(eightChar);
  const strength = analyzeStrength(eightChar);
  const shensha = findShensha(flat);
  const specialPillars = computeSpecialPillars(birthDate);
  const yun = computeYun(birthDate, gender);
  const tiaoHou = computeTiaoHouSimple(eightChar.day.Gan, eightChar.month.Zhi);
  const solarDate = toTrueSolarDate(birthDate, lon);
  const chenggu = computeChenggu(Lunar.fromDate(solarDate));
  const lifeScores = analyzeLifeScores(strength, shensha);

  console.log(JSON.stringify({
    input: { date: args.date, tz, gender, longitude: lon, note: 'date 默认按北京时间(东八区)解释；提供 lon 则已做真太阳时校正' },
    trueSolarTimeUsed: lon !== null,
    eightChar,
    wuxing,
    strength,
    shensha,
    specialPillars,
    yun,
    tiaoHou,
    chenggu,
    lifeScores,
  }, null, 2));
}

main();
