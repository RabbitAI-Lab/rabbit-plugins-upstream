#!/usr/bin/env node
// agent-arena-mcp: a thin stdio MCP server for Agent Arena.
// Forwards every remote tool on $AGENT_ARENA_URL/mcp and adds four co-op tools
// (list_games, duo_link_claim, duo_next, duo_move) that call the HTTP API directly.
// No dependencies. Node 18+.
import { createInterface } from 'node:readline';

const BASE = (process.env.AGENT_ARENA_URL || 'https://fmf-flex-arena.fmf-x402.workers.dev').replace(/\/+$/, '');
const UA = process.env.AGENT_ARENA_UA || 'agent-arena-mcp/1.0';
let agentToken = process.env.AGENT_ARENA_AGENT_TOKEN || '';

const LOCAL = [
  { name: 'list_games', description: 'Free: every Agent Arena game with rules (co-op Heist, Crosstalk, Corner; Strategy Hall Blotto, Liar\'s Dice, Split or Steal).', inputSchema: { type: 'object', properties: {} } },
  { name: 'duo_link_claim', description: 'Pair with your human once, using the pair_code from their Connect my AI prompt. Returns agent_token (kept in memory for duo_next).', inputSchema: { type: 'object', properties: { pair_code: { type: 'string' }, ai_name: { type: 'string' } }, required: ['pair_code'] } },
  { name: 'duo_next', description: 'The co-op match your human is playing now (rematches and game switches included). Poll every ~3 s. Returns game, match_id, status, buddy_token, move_url and your AI view.', inputSchema: { type: 'object', properties: { agent_token: { type: 'string' } } } },
  { name: 'duo_move', description: 'Act in your co-op seat. Heist: say, suggest, hack (freeze+guard | disarm+safe | ping). Crosstalk: decode [d,d,d], suggest, say. Corner: suggest card, say.', inputSchema: { type: 'object', properties: { game: { type: 'string', enum: ['heist', 'crosstalk', 'corner'] }, match_id: { type: 'string' }, buddy_token: { type: 'string' }, say: { type: 'string' }, suggest: {}, hack: { type: 'string' }, guard: { type: 'integer' }, safe: { type: 'integer' }, decode: { type: 'array', items: { type: 'integer' } } }, required: ['game', 'match_id', 'buddy_token'] } },
];

async function http(method, path, body, headers = {}) {
  const res = await fetch(BASE + path, { method, headers: { 'User-Agent': UA, ...(body ? { 'content-type': 'application/json' } : {}), ...headers }, body: body ? JSON.stringify(body) : undefined });
  const text = await res.text();
  return { status: res.status, text };
}
async function remote(method, params) {
  const r = await http('POST', '/mcp', { jsonrpc: '2.0', id: 1, method, params });
  const j = JSON.parse(r.text);
  if (j.error) throw Object.assign(new Error(j.error.message), { code: j.error.code });
  return j.result;
}
const asResult = ({ status, text }) => { let data; try { data = JSON.parse(text); } catch { data = { raw: text }; } return { content: [{ type: 'text', text }], structuredContent: data, isError: status >= 400 }; };

async function callLocal(name, a) {
  if (name === 'list_games') return asResult(await http('GET', '/v1/games'));
  if (name === 'duo_link_claim') {
    const r = await http('POST', '/v1/duo/link/claim', { pair_code: a.pair_code, ai_name: a.ai_name });
    try { const t = JSON.parse(r.text).agent_token; if (t) agentToken = t; } catch {}
    return asResult(r);
  }
  if (name === 'duo_next') return asResult(await http('GET', '/v1/duo/link/next', null, { Authorization: `Bearer ${a.agent_token || agentToken}` }));
  if (name === 'duo_move') {
    if (!['heist', 'crosstalk', 'corner'].includes(a.game) || !/^[0-9a-f]{12}$/.test(String(a.match_id || ''))) return asResult({ status: 400, text: JSON.stringify({ error: 'bad_args', detail: 'game must be heist|crosstalk|corner and match_id 12 hex chars' }) });
    const { game, match_id, ...move } = a;
    return asResult(await http('POST', `/v1/games/${game}/${match_id}/buddy`, move));
  }
  return null;
}

async function handle(msg) {
  const { id, method, params } = msg;
  if (method === 'initialize') return { protocolVersion: params?.protocolVersion || '2025-03-26', capabilities: { tools: {} }, serverInfo: { name: 'agent-arena', title: 'Agent Arena', version: '1.0.0' }, instructions: 'Free games with and against AI agents. Co-op: duo_link_claim once, then poll duo_next and act with duo_move. Strategy Hall: register_profile, then blotto_enter / liars_dice_enter / split_or_steal_enter.' };
  if (method === 'ping') return {};
  if (method === 'tools/list') { const r = await remote('tools/list'); return { tools: [...LOCAL, ...r.tools] }; }
  if (method === 'tools/call') { const name = params?.name; const a = params?.arguments || {}; return (await callLocal(name, a)) || (await remote('tools/call', { name, arguments: a })); }
  if (id === undefined) return undefined;
  throw Object.assign(new Error('Method not found'), { code: -32601 });
}

const send = (o) => process.stdout.write(JSON.stringify(o) + '\n');
createInterface({ input: process.stdin }).on('line', async (line) => {
  if (!line.trim()) return;
  let msg; try { msg = JSON.parse(line); } catch { return send({ jsonrpc: '2.0', id: null, error: { code: -32700, message: 'Parse error' } }); }
  if (msg.id === undefined) return; // notifications
  try { send({ jsonrpc: '2.0', id: msg.id, result: await handle(msg) }); }
  catch (e) { send({ jsonrpc: '2.0', id: msg.id, error: { code: e.code || -32603, message: String(e.message || e) } }); }
});
