#!/usr/bin/env node
'use strict';

/**
 * Unified compact-CLI entry (build source for scripts/jgy.cjs).
 *
 * Dispatch rules:
 *   auth-start / auth-complete / auth-status / logout / call  -> jgy.js  (金谷园登录与公开查询)
 *   get_lottery / list_my_prizes                              -> jgy.js  (实体卡揭晓与奖品查询)
 *   queue <command ...>                                       -> queue.js (美团真实排队动作)
 *   auth-poll-worker ...                                      -> queue.js (后台轮询自派生子命令)
 *
 * The background poller re-spawns THIS file (scriptPath = __filename), so the
 * `auth-poll-worker` route must stay at top level, not under the `queue` prefix.
 * Development keeps loose modules; the release bundle fuses them via build.mjs.
 */

async function dispatch() {
  const argv = process.argv.slice(2);
  const cmd = argv[0];

  if (cmd === 'queue' || cmd === 'auth-poll-worker') {
    const { run, exitCodeFor } = require('./queue');
    const queueArgv = cmd === 'queue' ? argv.slice(1) : argv;
    const result = await run(queueArgv, { scriptPath: __filename });
    process.stdout.write(`${JSON.stringify(result)}\n`);
    process.exitCode = exitCodeFor(result);
    return;
  }

  const { runCli } = require('./jgy');
  await runCli();
}

void dispatch();
