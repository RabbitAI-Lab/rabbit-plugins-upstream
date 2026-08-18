#!/usr/bin/env node
import { readFileSync } from 'node:fs';

const file = process.argv[2];
if (!file) {
  console.error('Usage: node scripts/validate-beautiful-deck.mjs <index.html>');
  process.exit(2);
}

const html = readFileSync(file, 'utf8');
const errors = [];
const warnings = [];

// Extract slide divs with depth-aware parsing (Beautiful/Cyberpunk use <div class="slide">)
function extractSlides() {
  const slides = [];
  const openRe = /<div\b[^>]*class="[^"]*\bslide\b[^"]*"[^>]*>/gi;
  let match;
  while ((match = openRe.exec(html)) !== null) {
    const start = match.index;
    const tagEnd = html.indexOf('>', start);
    if (tagEnd === -1) continue;
    let depth = 1;
    let i = tagEnd + 1;
    while (i < html.length && depth > 0) {
      const nextOpen = html.indexOf('<div', i);
      const nextClose = html.indexOf('</div>', i);
      if (nextClose === -1) break;
      if (nextOpen !== -1 && nextOpen < nextClose) {
        depth++;
        i = nextOpen + 4;
      } else {
        depth--;
        if (depth === 0) {
          slides.push({ idx: slides.length + 1, html: html.slice(start, nextClose + 6), tag: match[0] });
          i = nextClose + 6;
          openRe.lastIndex = i;
        } else {
          i = nextClose + 6;
        }
      }
    }
  }
  return slides;
}

const slides = extractSlides();

if (!slides.length) {
  errors.push('No <div class="slide"> pages found. Are you validating the correct Beautiful/Cyberpunk template?');
}

const ids = [];
const themes = [];
slides.forEach((slide) => {
  const clsMatch = slide.tag.match(/\bclass="([^"]*)"/);
  const classes = clsMatch ? clsMatch[1].split(/\s+/) : [];
  const idMatch = slide.tag.match(/\bid="([^"]*)"/);
  const id = idMatch ? idMatch[1] : null;

  // ID
  if (!id) {
    errors.push(`Slide ${slide.idx}: missing id. Use id="s{N}".`);
  } else if (!/^s\d+$/.test(id)) {
    errors.push(`Slide ${slide.idx}: id "${id}" does not match s{N} pattern.`);
  } else {
    ids.push(parseInt(id.slice(1), 10));
  }

  // Theme class
  const hasLight = classes.includes('light');
  const hasDark = classes.includes('dark');
  const isHero = classes.includes('hero');
  if (!hasLight && !hasDark) {
    errors.push(`Slide ${slide.idx}: missing theme class. Every slide must include either "light" or "dark".`);
  }
  if (isHero && !hasLight && !hasDark) {
    errors.push(`Slide ${slide.idx}: hero slide must also include "light" or "dark".`);
  }
  themes.push(hasDark ? 'dark' : 'light');

  // Animation density (cover/closing slides are allowed to be lighter)
  const animCount = (slide.html.match(/\banim(?:-left|-right|-scale|-float)?\b/g) || []).length;
  if (animCount < 3 && !classes.includes('hero')) {
    warnings.push(`Slide ${slide.idx}: only ${animCount} animated elements. Consider adding .anim to kicker, title, lead, and cards.`);
  }
});

// Sequential IDs
if (ids.length) {
  ids.sort((a, b) => a - b);
  for (let i = 0; i < ids.length; i++) {
    if (ids[i] !== i + 1) {
      errors.push(`Slide IDs are not sequential: expected s${i + 1}, found s${ids[i]}.`);
      break;
    }
  }
}

// Theme rhythm: no more than 3 consecutive same theme
let run = 1;
for (let i = 1; i < themes.length; i++) {
  if (themes[i] === themes[i - 1]) {
    run++;
    if (run > 3) {
      errors.push(`Theme rhythm: more than 3 consecutive ${themes[i]} slides starting around slide ${i - 1}.`);
      break;
    }
  } else {
    run = 1;
  }
}

// Whole-deck checks (ignore comments)
const stripped = html.replace(/<!--[\s\S]*?-->/g, '');

// Images
const imgTags = [...stripped.matchAll(/<img\b[^>]*>/gi)];
imgTags.forEach((m) => {
  const tag = m[0];
  if (/src="https?:\/\//i.test(tag)) {
    warnings.push('Found external image URL. Prefer local images/ folder and relative paths.');
  }
});

// Data-chart JSON
const chartMatches = [...stripped.matchAll(/data-chart="([^"]*)"/gi)];
chartMatches.forEach((m, idx) => {
  try {
    JSON.parse(m[1]);
  } catch (e) {
    errors.push(`Smart chart #${idx + 1} has invalid JSON: ${e.message}`);
  }
});

// Count-up data-value
const countUpTags = [...stripped.matchAll(/<[^>]*class="[^"]*\bcount-up\b[^"]*"[^>]*>/gi)];
countUpTags.forEach((m, idx) => {
  if (!/\bdata-value="/.test(m[0])) {
    errors.push(`Count-up element #${idx + 1} is missing data-value.`);
  }
});

// Inline bad practices
if (/height\s*:\s*100vh/i.test(stripped)) {
  errors.push('Avoid height:100vh on slide elements; use the template stage sizing.');
}
if (/box-shadow\s*:/i.test(stripped) && /frame-img/i.test(stripped)) {
  warnings.push('Images should not use inline shadows. The template handles card shadows.');
}
if (/border-radius\s*:\s*\d+px/i.test(stripped) && /frame-img/i.test(stripped)) {
  warnings.push('Images should not use inline border-radius. Use the template frame classes.');
}

// Emoji detection
const emojiRe = /[\u{1F300}-\u{1F6FF}\u{1F900}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;
if (emojiRe.test(stripped)) {
  warnings.push('Detected emoji characters. Prefer Lucide icons for icons.');
}

// Print results
if (errors.length) {
  console.error(`\n❌ ${errors.length} error(s) found in ${file}:\n`);
  errors.forEach((e) => console.error('  • ' + e));
}
if (warnings.length) {
  console.warn(`\n⚠️ ${warnings.length} warning(s) in ${file}:\n`);
  warnings.forEach((w) => console.warn('  • ' + w));
}
if (!errors.length && !warnings.length) {
  console.log(`\n✅ Beautiful/Cyberpunk deck validation passed for ${file}.`);
  process.exit(0);
}
process.exit(errors.length ? 1 : 0);
