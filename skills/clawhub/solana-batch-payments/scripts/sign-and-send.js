#!/usr/bin/env node
// Sign and submit unsigned batch transactions from the Spraay Solana Gateway.
//
// Usage:
//   node sign-and-send.js <response.json> <keypair.json> [rpc-url]
//
//   response.json — the JSON response from /solana/batch-send-sol or
//                   /solana/batch-send-token (contains transactions[])
//   keypair.json  — standard Solana keypair file (e.g. ~/.config/solana/id.json)
//                   Must match the `sender` used in the build request.
//   rpc-url       — optional, defaults to mainnet-beta public RPC
//
// The private key is used LOCALLY only. Nothing is sent to the gateway.

import { readFileSync } from 'node:fs';
import {
  Connection,
  Keypair,
  Transaction,
} from '@solana/web3.js';

const [, , responsePath, keypairPath, rpcUrl] = process.argv;

if (!responsePath || !keypairPath) {
  console.error('Usage: node sign-and-send.js <response.json> <keypair.json> [rpc-url]');
  process.exit(1);
}

const res = JSON.parse(readFileSync(responsePath, 'utf8'));
const secret = Uint8Array.from(JSON.parse(readFileSync(keypairPath, 'utf8')));
const keypair = Keypair.fromSecretKey(secret);

if (res.sender && keypair.publicKey.toBase58() !== res.sender) {
  console.error(`Keypair ${keypair.publicKey.toBase58()} does not match sender ${res.sender}`);
  process.exit(1);
}

const connection = new Connection(
  rpcUrl || 'https://api.mainnet-beta.solana.com',
  'confirmed',
);

console.log(`Signing ${res.transactionCount} transaction(s) as ${keypair.publicKey.toBase58()}`);

for (const [i, b64] of res.transactions.entries()) {
  const tx = Transaction.from(Buffer.from(b64, 'base64'));
  tx.sign(keypair);

  try {
    const sig = await connection.sendRawTransaction(tx.serialize());
    await connection.confirmTransaction(
      {
        signature: sig,
        blockhash: res.blockhash,
        lastValidBlockHeight: res.lastValidBlockHeight,
      },
      'confirmed',
    );
    console.log(`  [${i + 1}/${res.transactionCount}] confirmed: ${sig}`);
  } catch (err) {
    console.error(`  [${i + 1}/${res.transactionCount}] FAILED: ${err.message}`);
    console.error('  If the blockhash expired, rebuild the batch and retry.');
    process.exit(1);
  }
}

console.log('Done. Verify with GET /solana/status/<signature> ($0.001/call).');
