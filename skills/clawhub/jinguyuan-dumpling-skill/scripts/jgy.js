#!/usr/bin/env node
'use strict';

/**
 * Unified JGY CLI for the Skill runtime.
 *
 *   node scripts/jgy.js auth-start --phone "+86 138..."
 *   printf '%s' "$CODE" | node scripts/jgy.js auth-complete --login-id pl_xxx --stdin
 *   node scripts/jgy.js auth-status
 *   node scripts/jgy.js logout
 *   node scripts/jgy.js call authenticated-test
 *
 * The verification code is read ONLY from stdin, never from argv (which would leak into shell
 * history / process list / host logs). stdout is structured JSON with secrets redacted.
 */

const { createAuth, AuthError } = require('./lib/jgy-auth');
const { createApiClient } = require('./lib/jgy-api');
const { createLotteryApi } = require('./lib/lottery-api');
const claims = require('./lib/lottery-claims');
const { ok, err, emit } = require('./lib/output');

const SLUG_RE = /^[A-HJ-NP-Z2-9]{6,12}$/;

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (a.startsWith('--')) {
      const key = a.slice(2);
      const next = argv[i + 1];
      if (next === undefined || next.startsWith('--')) { args[key] = true; }
      else { args[key] = next; i += 1; }
    } else {
      args._.push(a);
    }
  }
  return args;
}

function readStdin() {
  return new Promise((resolve) => {
    let data = '';
    if (process.stdin.isTTY) { resolve(''); return; }
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', (c) => { data += c; });
    process.stdin.on('end', () => resolve(data));
    // Guard against a host that never closes stdin: resolve empty after a short wait.
    setTimeout(() => resolve(data), 2000).unref?.();
  });
}

async function main() {
  const argv = process.argv.slice(2);
  const command = argv[0];
  const args = parseArgs(argv.slice(1));
  const auth = createAuth();

  switch (command) {
    case 'auth-start': {
      const res = await auth.authStart(args.phone);
      return emit(ok(res));
    }
    case 'auth-complete': {
      let code = '';
      if (args.stdin) code = (await readStdin()).trim();
      else if (args.code) {
        // Explicitly refuse the insecure path: codes must not travel via argv.
        return emit(err('unsafe_input_channel', '验证码必须通过标准输入传入，不能作为命令行参数。'));
      }
      const res = await auth.authComplete({ loginId: args['login-id'], code });
      return emit(ok(res));
    }
    case 'auth-status':
      return emit(ok(auth.authStatus()));
    case 'logout':
      return emit(ok(await auth.logout()));
    case 'get_lottery': {
      const slug = args.slug || args._[0];
      const result = await getLottery(slug, auth);
      return emit(result);
    }
    case 'list_my_prizes': {
      const result = await listMyPrizes(auth);
      return emit(result);
    }
    case 'call': {
      const capability = args._[0];
      if (capability === 'authenticated-test') {
        const data = await auth.callAuthenticatedTest();
        return emit(ok({ data }));
      }
      if (!capability) return emit(err('invalid_command', '缺少能力名称。'));
      // Public capability (Phase 5 migration surface) — public routes need no login.
      // GET without args; POST with --args '<json>' (queue/query 等结构化查询).
      const api = createApiClient();
      let data;
      if (args.args) {
        let parsed;
        try { parsed = JSON.parse(String(args.args)); }
        catch { return emit(err('invalid_command', '--args 必须是合法 JSON。')); }
        data = await api.postCapability(capability, parsed);
      } else {
        data = await api.getCapability(capability);
      }
      return emit(ok({ data }));
    }
    default:
      return emit(err('invalid_command', '未知命令。可用：auth-start / auth-complete / auth-status / logout / call / get_lottery / list_my_prizes'));
  }
}

// ── 实体卡揭晓与奖品查询 ─────────────────────────────────────────

async function getLottery(slug, auth) {
  if (!slug || !SLUG_RE.test(slug)) {
    return err('invalid_slug', 'slug 格式不合法，需要 6-12 位大写字母+数字（不含 I、O、0、1）。');
  }

  // 1. 获取/生成匿名 claim token
  const claim = claims.getOrCreateClaim(slug);
  const claimToken = claim.claim_token;

  // 2. 检查登录态
  const status = auth.authStatus();
  let bearerToken = null;
  if (status.authenticated) {
    try { bearerToken = await auth.getAccessToken(); } catch { /* 未登录走匿名 */ }
  }

  // 3. 调用揭晓接口
  const lotteryApi = createLotteryApi({ bearer: bearerToken });
  const result = await lotteryApi.revealLottery({ slug, claimToken });

  // 4. 根据结果更新/删除本地 claim
  if (result && result.code === 'NO_PRIZE') {
    claims.removeClaim(slug);
    return ok({ result, claim_removed: true });
  }

  const resData = result && result.data ? result.data : {};
  if (resData.claim_id || resData.claim_state) {
    claims.updateClaim(slug, {
      claim_id: resData.claim_id,
      claim_state: resData.claim_state,
    });
  }

  // 5. 组装返回（含 next_action 提示）
  const nextAction = [];
  if (!status.authenticated) nextAction.push('login');
  return ok({ result, next_action: nextAction.length ? nextAction : undefined });
}

async function listMyPrizes(auth) {
  // 1. 匿名 claim 奖品
  const allClaims = claims.getAllClaims();
  const anonymousPrizes = [];
  for (const [slug, claim] of Object.entries(allClaims)) {
    const lotteryApi = createLotteryApi();
    const prize = await lotteryApi.getAnonymousPrize(claim.claim_token);
    anonymousPrizes.push({ slug, ...prize });
  }

  // 2. 登录态奖品
  let myPrizes = null;
  const status = auth.authStatus();
  if (status.authenticated) {
    try {
      const bearerToken = await auth.getAccessToken();
      const lotteryApi = createLotteryApi({ bearer: bearerToken });
      myPrizes = await lotteryApi.getMyPrizes();
    } catch { /* 登录态失效则跳过 */ }
  }

  return ok({
    anonymous: anonymousPrizes,
    my: myPrizes,
    total: anonymousPrizes.length + (myPrizes && Array.isArray(myPrizes) ? myPrizes.length : 0),
  });
}

function runCli() {
  return main().catch((e) => {
    if (e instanceof AuthError) {
      emit(err(e.code, e.message, e.extra || {}));
      process.exitCode = 1;
      return;
    }
    emit(err('unexpected_error', '执行失败，请稍后重试。'));
    process.exitCode = 1;
  });
}

if (require.main === module) void runCli();

module.exports = { runCli, getLottery, listMyPrizes };
