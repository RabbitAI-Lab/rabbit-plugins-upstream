#!/usr/bin/env node
/**
 * CLI wrapper for video summarizer.
 * Usage: node scripts/extract-frames.js <videoPath> [threshold] [outputDir]
 */
const vs = require('../index.js');

const videoPath = process.argv[2];
if (!videoPath) {
  console.error('Usage: node scripts/extract-frames.js <videoPath> [threshold] [outputDir]');
  process.exit(1);
}

const opts = {};
if (process.argv[3]) opts.sceneThreshold = parseFloat(process.argv[3]);
if (process.argv[4]) opts.outputDir = process.argv[4];

try {
  const result = vs.summarize(videoPath, opts);
  console.log(JSON.stringify(result, null, 2));
} catch (e) {
  console.error('Error:', e.message);
  process.exit(1);
}
