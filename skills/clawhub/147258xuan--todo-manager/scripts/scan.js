#!/usr/bin/env node
'use strict';
const { scanTodos, formatReport, saveTodos, getSummary } = require('../index');
const dir = process.argv[2] || '.';
const todos = scanTodos(dir);
console.log(formatReport(todos));
const summary = getSummary(todos);
if (summary.total > 0) {
  console.log('\nSummary: ' + JSON.stringify(summary));
  const out = saveTodos(todos);
  console.log('Saved to ' + out);
}
