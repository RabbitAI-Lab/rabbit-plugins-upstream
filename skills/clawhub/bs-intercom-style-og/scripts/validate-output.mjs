#!/usr/bin/env node

import { lstatSync, readFileSync, readdirSync } from 'node:fs';
import { extname, resolve } from 'node:path';
import { inspectRasterBytes } from './raster.mjs';

const TEXT_EXTENSIONS = new Set([
  '.css',
  '.html',
  '.js',
  '.json',
  '.jsx',
  '.md',
  '.mjs',
  '.svg',
  '.text',
  '.ts',
  '.tsx',
  '.txt',
]);
const MULTI_VALUE_OPTIONS = new Map([
  ['--image', 'images'],
  ['--prompt-file', 'promptFiles'],
  ['--text-root', 'textRoots'],
]);
const SINGLE_VALUE_OPTIONS = new Set(['--require-format', '--min-width']);
const BOOLEAN_OPTIONS = new Set(['--require-16-9']);

const EXTENDED_PICTOGRAPHIC = /\p{Extended_Pictographic}/u;
const TEXT_NOTICE_CODE_POINTS = new Set([0x00a9, 0x00ae, 0x2122]);

function isExplicitIconRange(codePoint) {
  return (
    codePoint === 0x20e3 ||
    (codePoint >= 0x2190 && codePoint <= 0x21ff) ||
    (codePoint >= 0x2300 && codePoint <= 0x23ff) ||
    (codePoint >= 0x2500 && codePoint <= 0x27bf) ||
    (codePoint >= 0x2b00 && codePoint <= 0x2bff) ||
    (codePoint >= 0x1f000 && codePoint <= 0x1ffff)
  );
}

function findProhibitedIconGlyph(text) {
  const characters = Array.from(text);
  for (let index = 0; index < characters.length; index += 1) {
    const character = characters[index];
    const codePoint = character.codePointAt(0);
    const emojiStyledNotice =
      TEXT_NOTICE_CODE_POINTS.has(codePoint) &&
      characters[index + 1]?.codePointAt(0) === 0xfe0f;
    if (
      isExplicitIconRange(codePoint) ||
      emojiStyledNotice ||
      (EXTENDED_PICTOGRAPHIC.test(character) &&
        !TEXT_NOTICE_CODE_POINTS.has(codePoint))
    ) {
      return character;
    }
  }
  return null;
}

function usage() {
  return `Usage:
  node scripts/validate-output.mjs \\
    --image /absolute/path/artwork.webp \\
    [--image /absolute/path/another.webp] \\
    [--prompt-file /absolute/path/prompt.txt] \\
    [--text-root /absolute/path/generated-text] \\
    [--require-format webp] [--require-16-9] [--min-width 1024]

The text scan rejects emoji, dingbats, Unicode arrows, geometric icon glyphs,
and pictographic symbols used as icons. Bitmap content still requires visual
inspection.
`;
}

function parseArgs(argv) {
  const options = { images: [], promptFiles: [], textRoots: [] };
  const seenSingletons = new Set();
  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];
    if (token === '--help' || token === '-h') {
      if (options.help) throw new Error('Help flag was provided more than once.');
      options.help = true;
      continue;
    }
    if (BOOLEAN_OPTIONS.has(token)) {
      if (seenSingletons.has(token)) throw new Error(`Duplicate option: ${token}`);
      seenSingletons.add(token);
      options.require16x9 = true;
      continue;
    }
    if (!MULTI_VALUE_OPTIONS.has(token) && !SINGLE_VALUE_OPTIONS.has(token)) {
      throw new Error(`Unknown option: ${token}`);
    }
    const value = argv[index + 1];
    if (!value || value.startsWith('--')) {
      throw new Error(`Missing value for ${token}.`);
    }
    const multiKey = MULTI_VALUE_OPTIONS.get(token);
    if (multiKey) {
      options[multiKey].push(value);
    } else {
      if (seenSingletons.has(token)) throw new Error(`Duplicate option: ${token}`);
      seenSingletons.add(token);
      options[token.slice(2)] = value;
    }
    index += 1;
  }
  return options;
}

function assertGlyphPolicy() {
  for (const codePoint of [
    0x20e3,
    0x2192,
    0x25b2,
    0x25bc,
    0x25d0,
    0x25c8,
    0x2713,
    0x2b06,
    0x2b50,
    0x1f1fa,
    0x1f600,
  ]) {
    const character = String.fromCodePoint(codePoint);
    if (!findProhibitedIconGlyph(character)) {
      throw new Error(`Internal glyph policy missed U+${codePoint.toString(16)}.`);
    }
  }
  for (const codePoint of [0x203c, 0x2049, 0x2139, 0x24c2, 0x3030, 0x303d, 0x3297, 0x3299]) {
    if (!findProhibitedIconGlyph(String.fromCodePoint(codePoint))) {
      throw new Error(`Internal emoji policy missed U+${codePoint.toString(16)}.`);
    }
  }
  for (const allowedCodePoint of [0x41, 0x00a9, 0x00ae, 0x2122]) {
    const allowed = String.fromCodePoint(allowedCodePoint);
    if (findProhibitedIconGlyph(allowed)) {
      throw new Error(`Internal glyph policy rejected ordinary U+${allowedCodePoint.toString(16)} text.`);
    }
    if (
      TEXT_NOTICE_CODE_POINTS.has(allowedCodePoint) &&
      !findProhibitedIconGlyph(`${allowed}${String.fromCodePoint(0xfe0f)}`)
    ) {
      throw new Error(`Internal emoji policy allowed styled U+${allowedCodePoint.toString(16)}.`);
    }
  }
}

function glyphDescription(character) {
  return `U+${character.codePointAt(0).toString(16).toUpperCase().padStart(4, '0')}`;
}

function scanText(path) {
  const buffer = readFileSync(path);
  if (buffer.length > 2 * 1024 * 1024) {
    throw new Error(`Text file exceeds the 2 MB scan limit: ${path}`);
  }
  let text;
  try {
    text = new TextDecoder('utf-8', { fatal: true }).decode(buffer);
  } catch {
    throw new Error(`Text file is not valid UTF-8: ${path}`);
  }
  const match = findProhibitedIconGlyph(text);
  if (match) {
    throw new Error(
      `Prohibited icon glyph ${glyphDescription(match)} found in ${path}. Use inline SVG or ordinary words instead.`
    );
  }
  return { path, bytes: buffer.length };
}

function walkText(root, found) {
  const metadata = lstatSync(root);
  if (metadata.isSymbolicLink()) throw new Error(`Symbolic link is not scanned: ${root}`);
  if (metadata.isDirectory()) {
    for (const name of readdirSync(root)) {
      if (name === '.git' || name === 'node_modules') continue;
      walkText(resolve(root, name), found);
    }
    return;
  }
  if (TEXT_EXTENSIONS.has(extname(root).toLowerCase())) found.push(scanText(root));
}

function main() {
  assertGlyphPolicy();
  const options = parseArgs(process.argv.slice(2));
  if (options.help) {
    process.stdout.write(usage());
    return;
  }
  if (
    options.images.length === 0 &&
    options.promptFiles.length === 0 &&
    options.textRoots.length === 0
  ) {
    throw new Error('Pass at least one --image, --prompt-file, or --text-root.');
  }

  const minWidth = Number(options['min-width'] ?? 0);
  if (!Number.isInteger(minWidth) || minWidth < 0) {
    throw new Error('--min-width must be a non-negative integer.');
  }
  const requiredFormat = options['require-format'];
  if (requiredFormat && !['webp', 'png', 'jpeg'].includes(requiredFormat)) {
    throw new Error('--require-format must be webp, png, or jpeg.');
  }

  const images = options.images.map((value) => {
    const path = resolve(value);
    return { path, ...inspectRasterBytes(readFileSync(path)) };
  });
  for (const image of images) {
    if (requiredFormat && image.format !== requiredFormat) {
      throw new Error(`${image.path} is ${image.format}, expected ${requiredFormat}.`);
    }
    if (minWidth && image.width < minWidth) {
      throw new Error(`${image.path} is ${image.width}px wide, below ${minWidth}px.`);
    }
    if (options.require16x9 && image.width * 9 !== image.height * 16) {
      throw new Error(
        `${image.path} is ${image.width}x${image.height}, not an exact 16:9 raster.`
      );
    }
  }

  const textFiles = options.promptFiles.map((value) => scanText(resolve(value)));
  for (const value of options.textRoots) walkText(resolve(value), textFiles);

  process.stdout.write(
    `${JSON.stringify(
      {
        ok: true,
        images,
        textFilesScanned: textFiles.length,
      },
      null,
      2
    )}\n`
  );
}

try {
  main();
} catch (error) {
  process.stderr.write(`${error.message}\n`);
  process.exitCode = 1;
}
