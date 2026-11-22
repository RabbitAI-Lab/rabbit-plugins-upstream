import fs from 'node:fs';
import { diagnose } from './diagnose.mjs';

const success = JSON.parse(fs.readFileSync(new URL('../fixtures/success.json', import.meta.url)));
const report = diagnose(success);
if (report.mode !== 'mock' || report.metrics.sampleCount !== 2 || report.metrics.totalLikes !== 180) process.exit(1);
let failed = false;
try { diagnose(JSON.parse(fs.readFileSync(new URL('../fixtures/failure.json', import.meta.url)))); } catch { failed = true; }
if (!failed) process.exit(1);
console.log('douyin-account-diagnosis self-test passed');
