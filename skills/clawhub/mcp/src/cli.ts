#!/usr/bin/env node
import { redactSecretsFromToolOutput } from '@cryptoslip/sdk';
import { startCryptoSlipStdioServer } from './server.js';

startCryptoSlipStdioServer().catch((err: unknown) => {
  const msg = err instanceof Error ? err.message : String(err);
  process.stderr.write(
    `[@cryptoslip/mcp] Fatal startup error: ${redactSecretsFromToolOutput(msg)}\n`,
  );
  process.exitCode = 1;
});
