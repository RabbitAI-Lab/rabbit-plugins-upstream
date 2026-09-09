#!/usr/bin/env node
/** Start pinned hypelens agent-rail MCP from local node_modules (no child_process). */
import { createRequire } from 'node:module';
import { dirname, join } from 'node:path';
import { pathToFileURL } from 'node:url';

const require = createRequire(import.meta.url);
try {
  const pkgJson = require.resolve('@hypelens/hypelens-agent-rail/package.json');
  const pkg = require(pkgJson);
  const binRel = (pkg.bin && (pkg.bin['hypelens-rail-mcp'] || pkg.bin['hypelens-agent-rail'])) || 'bin/hypelens-rail-mcp.js';
  const entry = join(dirname(pkgJson), binRel);
  await import(pathToFileURL(entry).href);
} catch (e) {
  console.error('Missing dependency. Run: npm install (in this scripts/ folder)');
  console.error(String(e && e.message ? e.message : e));
  process.exit(1);
}
