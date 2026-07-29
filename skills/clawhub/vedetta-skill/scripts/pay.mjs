#!/usr/bin/env node
/**
 * Vedetta x402 payment client — USDC on Base.
 * Usage:
 *   export VEDETTA_X402_PRIVATE_KEY='0x...'
 *   node pay.mjs '/v1/feed?limit=1'
 *   node pay.mjs '/v1/consensus?asset=BTC'
 *
 * Requires (once, in this directory or ~/.vedetta-client):
 *   npm i @x402/axios @x402/evm axios viem
 */
import { wrapAxiosWithPayment, x402Client } from '@x402/axios';
import { ExactEvmScheme } from '@x402/evm/exact/client';
import { toClientEvmSigner } from '@x402/evm';
import axios from 'axios';
import { createPublicClient, http } from 'viem';
import { base } from 'viem/chains';
import { privateKeyToAccount } from 'viem/accounts';

const key = process.env.VEDETTA_X402_PRIVATE_KEY;
if (!key) {
  console.error('VEDETTA_X402_PRIVATE_KEY not set');
  console.error('Use a dedicated low-balance Base USDC wallet. Never commit the key.');
  process.exit(1);
}

const account = privateKeyToAccount(key.startsWith('0x') ? key : `0x${key}`);
const publicClient = createPublicClient({ chain: base, transport: http() });
const client = new x402Client();
client.register('eip155:*', new ExactEvmScheme(toClientEvmSigner(account, publicClient)));

const api = wrapAxiosWithPayment(
  axios.create({ baseURL: 'https://vedetta.dethboy.com', timeout: 220000 }),
  client
);

const path = process.argv[2] || '/v1/snapshot?asset=BTC';
try {
  const r = await api.get(path);
  console.log(JSON.stringify(r.data, null, 2));
} catch (err) {
  const status = err?.response?.status;
  const data = err?.response?.data;
  if (status) {
    console.error(JSON.stringify({ error: true, status, data }, null, 2));
  } else {
    console.error(String(err?.message || err));
  }
  process.exit(1);
}
