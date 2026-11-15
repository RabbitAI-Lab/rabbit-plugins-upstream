#!/usr/bin/env node
/**
 * CLI wrapper for broken-link-checker.
 * Uses the real exported API from ../index.js:
 *   checkBrokenLinks(targetDir, options) -> results
 *   formatResults(results) -> string
 */
const path = require('path');
const fs = require('fs');
const { checkBrokenLinks, formatResults } = require('../index.js');

const target = process.argv[2] || process.cwd();
const resolved = path.resolve(target);

if (!fs.existsSync(resolved)) {
  console.error(`Target not found: ${resolved}`);
  process.exit(2);
}

const results = checkBrokenLinks(resolved);
console.log(formatResults(results));

if (results.summary.broken_links > 0) {
  console.log('\nBroken links found! Please fix before committing.');
  process.exit(1);
}

console.log('\nNo broken links found.');
process.exit(0);
