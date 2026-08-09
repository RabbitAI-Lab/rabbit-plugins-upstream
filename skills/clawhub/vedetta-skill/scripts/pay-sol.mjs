#!/usr/bin/env node
/**
 * Vedetta x402 Solana (SVM) payment client — USDC SPL on Solana mainnet.
 *
 * Usage (after green light + funded lab wallet):
 *   export VEDETTA_X402_SOLANA_PRIVATE_KEY='<base58 secret key>'
 *   node pay-sol.mjs '/sol/v1/feed?limit=1'          # $0.005 cheapest
 *   node pay-sol.mjs '/sol/v1/snapshot?asset=BTC'     # $0.02
 *
 * Install once (prefer ~/.vedetta-client so Base pay.mjs shares node_modules):
 *   mkdir -p ~/.vedetta-client && cd ~/.vedetta-client
 *   npm i @x402/axios @x402/svm @x402/evm @solana/kit axios viem bs58
 *   cp this file next to pay.mjs
 *
 * Do NOT log the private key. Dedicated low-balance wallet only.
 * payTo on live 402 must be 4kEdSopjVayXZ8DpAe6G3fVEFYDj6cny6AjWEEWr3Hdq.
 */
import { wrapAxiosWithPayment, x402Client } from '@x402/axios';
import { ExactSvmScheme } from '@x402/svm/exact/client';
import { toClientSvmSigner } from '@x402/svm';
import { createKeyPairSignerFromBytes } from '@solana/kit';
import axios from 'axios';
import bs58 from 'bs58';

const key = process.env.VEDETTA_X402_SOLANA_PRIVATE_KEY;
if (!key) {
  console.error('VEDETTA_X402_SOLANA_PRIVATE_KEY not set');
  console.error('Use a dedicated low-balance Solana wallet (USDC SPL + small SOL for fees).');
  process.exit(1);
}

function decodeSecret(raw) {
  const s = String(raw).trim();
  if (s.startsWith('[')) {
    const arr = JSON.parse(s);
    if (!Array.isArray(arr)) throw new Error('JSON key must be a byte array');
    return Uint8Array.from(arr);
  }
  const cleaned = s.replace(/^\[|\]$/g, '').replace(/^['"]|['"]$/g, '');
  return bs58.decode(cleaned);
}

const secretBytes = decodeSecret(key);
const svmSigner = await createKeyPairSignerFromBytes(secretBytes);
const client = new x402Client();
client.register('solana:*', new ExactSvmScheme(toClientSvmSigner(svmSigner)));

const api = wrapAxiosWithPayment(
  axios.create({ baseURL: 'https://vedetta.dethboy.com', timeout: 220000 }),
  client
);

const path = process.argv[2] || '/sol/v1/feed?limit=1';
if (!path.startsWith('/sol/')) {
  console.error('Refusing non-Sol path. Use /sol/v1/... (this client is SVM-only).');
  process.exit(2);
}

console.error(
  JSON.stringify(
    {
      phase: 'request',
      path,
      payer_pubkey: svmSigner.address,
      payTo_expected: '4kEdSopjVayXZ8DpAe6G3fVEFYDj6cny6AjWEEWr3Hdq',
      network_wire: 'solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp',
      asset_usdc_mint: 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
      started_at: new Date().toISOString(),
    },
    null,
    2
  )
);

try {
  const r = await api.get(path);
  if (r.status < 200 || r.status >= 300) {
    console.error(
      JSON.stringify(
        {
          error: true,
          status: r.status,
          path,
          payer_pubkey: svmSigner.address,
          message: 'Payment wrapper returned non-2xx (no successful settle)',
          data: r.data,
        },
        null,
        2
      )
    );
    process.exit(1);
  }
  console.log(
    JSON.stringify(
      {
        ok: true,
        http_status: r.status,
        path,
        payer_pubkey: svmSigner.address,
        response_keys: r.data && typeof r.data === 'object' ? Object.keys(r.data) : typeof r.data,
        data: r.data,
      },
      null,
      2
    )
  );
} catch (err) {
  const status = err?.response?.status;
  const data = err?.response?.data;
  const headers = err?.response?.headers || {};
  const pr = headers['payment-required'] || headers['PAYMENT-REQUIRED'];
  console.error(
    JSON.stringify(
      {
        error: true,
        status,
        path,
        payer_pubkey: svmSigner.address,
        message: String(err?.message || err),
        has_payment_required_header: Boolean(pr),
        data,
      },
      null,
      2
    )
  );
  process.exit(1);
}
