// Read-only live checks for the package (no writes): llms.txt, /v1/games, /mcp tools/list via the bridge,
// /v1/duo/link/claim with a bogus code (404 bad_code), /v1/duo/link/next without a token (401).
import { spawn } from 'node:child_process';
const BASE = process.env.AGENT_ARENA_URL || 'https://fmf-flex-arena.fmf-x402.workers.dev';
const H = { 'User-Agent': 'agent-arena-mcp-check/1.0' };
const ok = (c, m) => { console.log(c ? 'PASS' : 'FAIL', m); if (!c) process.exitCode = 1; };
const llms = await (await fetch(`${BASE}/llms.txt`, { headers: H })).text();
ok(llms.split('\n')[0] === '# Agent Arena', `/llms.txt line 1 = ${JSON.stringify(llms.split('\n')[0])}`);
const games = await (await fetch(`${BASE}/v1/games`, { headers: H })).json();
ok(['heist', 'crosstalk', 'corner'].every((g) => games.duo_arenas.some((d) => d.id === g)), `/v1/games duo_arenas: ${games.duo_arenas.map((d) => d.id).join(', ')}`);
ok(['blotto', 'liars-dice', 'split-or-steal'].every((g) => games.strategy_hall.some((d) => d.id === g)), `/v1/games strategy_hall: ${games.strategy_hall.map((d) => d.id).join(', ')}`);
const claim = await fetch(`${BASE}/v1/duo/link/claim`, { method: 'POST', headers: { ...H, 'content-type': 'application/json' }, body: JSON.stringify({ pair_code: '0000000000000000' }) });
ok(claim.status === 404 && (await claim.json()).error === 'bad_code', `/v1/duo/link/claim bogus code -> ${claim.status} bad_code`);
const next = await fetch(`${BASE}/v1/duo/link/next`, { headers: H });
ok(next.status === 401, `/v1/duo/link/next without token -> ${next.status}`);
// stdio bridge
const p = spawn(process.execPath, [new URL('./index.js', import.meta.url).pathname], { env: { ...process.env, AGENT_ARENA_URL: BASE } });
let buf = ''; const waiters = {};
p.stdout.on('data', (d) => { buf += d; let i; while ((i = buf.indexOf('\n')) >= 0) { const m = JSON.parse(buf.slice(0, i)); buf = buf.slice(i + 1); waiters[m.id]?.(m); } });
const rpc = (id, method, params) => new Promise((r) => { waiters[id] = r; p.stdin.write(JSON.stringify({ jsonrpc: '2.0', id, method, params }) + '\n'); });
const init = await rpc(1, 'initialize', { protocolVersion: '2025-03-26' });
ok(init.result?.serverInfo?.name === 'agent-arena', 'bridge initialize');
const list = await rpc(2, 'tools/list', {});
const names = list.result.tools.map((t) => t.name);
ok(['duo_link_claim', 'duo_next', 'duo_move', 'list_games', 'blotto_enter', 'get_match'].every((n) => names.includes(n)), `bridge tools/list: ${names.length} tools (4 local + ${names.length - 4} remote)`);
const lg = await rpc(3, 'tools/call', { name: 'list_games', arguments: {} });
ok(!lg.result.isError && lg.result.structuredContent.duo_arenas.length === 3, 'bridge list_games');
const board = await rpc(4, 'tools/call', { name: 'get_skill_board', arguments: { game: 'blotto' } });
ok(!board.result.isError, 'bridge forwards remote tool get_skill_board');
const nx = await rpc(5, 'tools/call', { name: 'duo_next', arguments: {} });
ok(nx.result.isError === true, 'bridge duo_next without token is an error (401)');
p.kill();
