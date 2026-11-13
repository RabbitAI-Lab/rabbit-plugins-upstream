'use strict';
const mod = require('./scripts/screen');
if (require.main === module) {
  const args = require('minimist')(process.argv.slice(2));
  mod.screen(args).catch(e => { console.error('ERROR:', e.message); process.exit(1); });
} else {
  module.exports = mod;
}
