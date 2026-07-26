#!/usr/bin/env node
import { detectInternalNetwork } from './lib/internal-env.js';

const result = await detectInternalNetwork();
process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
process.exit(result.allowed ? 0 : 1);
