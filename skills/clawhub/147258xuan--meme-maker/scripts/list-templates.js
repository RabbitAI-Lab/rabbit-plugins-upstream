#!/usr/bin/env node
const { getTemplates } = require('../index');
const templates = getTemplates();
console.log('=== Available Meme Templates ===\n');
templates.forEach((t, i) => console.log(`  ${i + 1}. ${t.name} (id: ${t.id})`));
console.log(`\nTotal: ${templates.length} templates`);
