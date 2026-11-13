#!/usr/bin/env node
const { analyze, countTodos, report } = require('../index.js');
const path = require('path');

const dir = process.argv[2] || process.cwd();
const stats = analyze(path.resolve(dir));
console.log(report(stats));

const todos = countTodos(path.resolve(dir));
console.log('');
console.log('TODO/FIXME/HACK/XXX: ' + todos.count + ' found');
if (todos.details.length > 0) {
  for (const d of todos.details.slice(0, 20)) {
    console.log('  ' + d.file + ':' + d.line + ' ' + d.text);
  }
  if (todos.details.length > 20) console.log('  ... and ' + (todos.details.length - 20) + ' more');
}
