// index.js — comment_list / reply 两个动作的统一入口。
//
// 用 process_one_video.js 导出的两个函数。
//
// ── 命令行用法 ─────────────────────────────────────────────────────
//
// A. 抓评论列表（不回复）：
//    node index.js --comment-list [--title <视频名> | --index <N>]
//
// B. 批量回复（JSON 文件）：
//    node index.js --reply [--title <视频名> | --index <N>] --replies-file <path/to/replies.json>
//                   [--delay-ms <ms>]
//
// C. 批量回复（内联 JSON）：
//    node index.js --reply [--title <视频名> | --index <N>] --replies '[{"author":"x","content":"y","text":"z"}]'
//                   [--delay-ms <ms>]
//
// D. 单条回复（便捷写法，等价于 1 条 list）：
//    node index.js --reply [--title <视频名> | --index <N>] --author <作者> --content <内容关键词> --text <回复文本>
//
// 注意：reply 动作**直接发送**，没有 dry-run 中间步。审批 JSON 阶段就是最后人工把关。
//
// 回复列表条目格式（每条必须含 author + content + text 三个字段）：
//    { "author":   "亮有一计",        // 作者名（子串匹配）
//      "content":  "免费",            // 评论内容关键词（子串匹配）
//      "text":     "感谢推荐" }       // 要发送的回复文本
//
// reply 通用选项：
//   --delay-ms <ms>    多条回复之间的防爬间隔（默认 5000，首条不等待）
//
// comment-list 选项：
//   （无：抓完直接打印 id 清单）
//
// ── 流程 & 输出 ────────────────────────────────────────────────────
//
// 启动浏览器（持久化 profile 复用 cookies）→ 跳评论管理页 →
// 死等登录（"选择作品"按钮出现，最多 5 分钟）→ 直接跑动作（comment_list /
// reply 内部会用 clickWorkByName 自动选 --title 指定的作品）→ 关浏览器。
//
// 无任何 stdin 暂停，全自动。
//
// 输出（仅此一种）：
//   - stdout：run(args, page) 的完整 JSON 返回值，一行
//             shell 可直接 `node index.js ... | tee result.json`
//
// reply 失败时 process.exitCode = 1，方便 shell 流水线用 && / || 判断。
//
// ── 模块用法 ───────────────────────────────────────────────────────
//
// const { run, parseArgs } = require('./index');
// const args = parseArgs(process.argv);   // 自己准备 page（复用已有 context）
// const result = await run(args, page);   // 直接拿返回对象
//
// ─────────────────────────────────────────────────────────────────────

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const { comment_list, reply } = require('./process_one_video');
const WL = require('./work-list-actions');

const TARGET = 'https://creator.douyin.com/creator-micro/interactive/comment';
// USER_DATA_DIR: 默认 skill 自带 user-data/（首次跑会停在登录页）。
// 也支持环境变量覆盖，便于：① 复用现成登录态 ② 多账号。
//   PowerShell: $env:DOUYIN_USER_DATA_DIR='<已有的 user-data 绝对路径>'
//   bash:       DOUYIN_USER_DATA_DIR='<已有的 user-data 绝对路径>' node index.js ...
const USER_DATA_DIR = process.env.DOUYIN_USER_DATA_DIR
  ? path.resolve(process.env.DOUYIN_USER_DATA_DIR)
  : path.resolve(__dirname, 'user-data');

// ── 参数解析 ────────────────────────────────────────────────────────
function parseArgs(argv) {
  const args = { action: null };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    const next = argv[i + 1];
    switch (a) {
      case '--comment-list':  args.action = 'comment-list'; break;
      case '--reply':         args.action = 'reply'; break;
      case '--title':         args.title = next; i++; break;
      case '--index':         args.index = parseInt(next, 10); i++; break;
      case '--replies':       args.replies = next; i++; break;
      case '--replies-file':  args.repliesFile = next; i++; break;
      case '--author':        args.author = next; i++; break;
      case '--content':       args.content = next; i++; break;
      case '--text':          args.text = next; i++; break;
      case '--delay-ms':      args.delayMs = parseInt(next, 10); i++; break;
      case '-h':
      case '--help':
        printUsage();
        process.exit(0);
        break;
      default:
        console.error('[index] 未知参数:', a);
        printUsage();
        process.exit(2);
    }
  }

  // 必填校验
  if (!args.action) {
    console.error('[index] 必须指定 --comment-list 或 --reply');
    printUsage();
    process.exit(2);
  }
  // --title 可选：省略时选第一个作品（index 0）
  // --index <N>  与 --title 互斥
  if (args.title != null && args.index !== undefined) {
    console.error('[index] --title 与 --index 互斥，只能用其中一个');
    process.exit(2);
  }
  if (args.index !== undefined && (!Number.isInteger(args.index) || args.index < 0)) {
    console.error(`[index] --index 必须是 ≥ 0 的整数，收到: ${args.index}`);
    process.exit(2);
  }

  // 把回复列表来源解析成 list
  if (args.action === 'reply') {
    const sources = [
      args.replies && 'inline --replies',
      args.repliesFile && `--replies-file "${args.repliesFile}"`,
      (args.author || args.content || args.text) && '--author/--content/--text',
    ].filter(Boolean);

    if (sources.length === 0) {
      console.error('[index] --reply 必须配合以下之一提供回复列表：');
      console.error('  --replies "<json>"');
      console.error('  --replies-file <path>');
      console.error('  --author <x> --content <y> --text <z>');
      process.exit(2);
    }
    if (sources.length > 1) {
      console.error(`[index] 回复列表来源互斥，但同时给了：${sources.join(' / ')}`);
      process.exit(2);
    }

    if (args.repliesFile) {
      if (!fs.existsSync(args.repliesFile)) {
        console.error(`[index] --replies-file 文件不存在: ${args.repliesFile}`);
        process.exit(2);
      }
      let parsed;
      try {
        const raw = fs.readFileSync(args.repliesFile, 'utf8');
        parsed = JSON.parse(raw);
      } catch (e) {
        console.error(`[index] --replies-file 解析失败（${args.repliesFile}）：${e.message}`);
        process.exit(2);
      }
      if (!Array.isArray(parsed)) {
        console.error('[index] --replies-file 内容必须是 JSON 数组（每条 {author,content,text}）');
        process.exit(2);
      }
      args.list = parsed;
    } else if (args.replies) {
      let parsed;
      try {
        parsed = JSON.parse(args.replies);
      } catch (e) {
        console.error(`[index] --replies 不是合法 JSON：${e.message}`);
        console.error('[index] 提示：PowerShell 里要用单引号包裹双引号 JSON，例如：');
        console.error('  --replies \'[{"author":"x","content":"y","text":"z"}]\'');
        process.exit(2);
      }
      if (!Array.isArray(parsed)) {
        console.error('[index] --replies 必须是 JSON 数组');
        process.exit(2);
      }
      args.list = parsed;
    } else {
      // --author / --content / --text 单条
      if (!args.author || !args.content || !args.text) {
        console.error('[index] 单条模式必须同时给 --author / --content / --text');
        process.exit(2);
      }
      args.list = [{ author: args.author, content: args.content, text: args.text }];
    }

    // 校验每条字段
    for (let i = 0; i < args.list.length; i++) {
      const item = args.list[i];
      if (!item || typeof item.author !== 'string' ||
          typeof item.content !== 'string' || typeof item.text !== 'string') {
        console.error(`[index] replies[${i}] 字段缺失或类型错误，必须是 { author:string, content:string, text:string }`);
        console.error(`[index] 实际: ${JSON.stringify(item)}`);
        process.exit(2);
      }
    }
  }

  return args;
}

function printUsage() {
  console.log('');
  console.log('用法:');
  console.log('  node index.js --comment-list [--title "<视频名>" | --index <N>]');
  console.log('  node index.js --reply [--title "<视频名>" | --index <N>] --replies-file <path> [--delay-ms N]');
  console.log('  node index.js --reply [--title "<视频名>" | --index <N>] --replies \'<json>\' [--delay-ms N]');
  console.log('  node index.js --reply [--title "<视频名>" | --index <N>] --author <x> --content <y> --text <z>');
  console.log('');
  console.log('回复条目: { author:string, content:string, text:string }');
  console.log('         author / content 是子串匹配；text 是要发送的内容');
  console.log('');
  console.log('动作选项:');
  console.log('  --comment-list              抓评论列表（不回复）');
  console.log('  --reply                     批量回复（必须配合下面之一）。直接发送，无 dry-run 中间步。');
  console.log('  --title "<视频名>"           按标题匹配（子串）。与 --index 互斥。');
  console.log('  --index <N>                 按 0-based 序号选作品。与 --title 互斥。');
  console.log('  --title / --index 都省略     选第一个作品（index 0）');
  console.log('  --replies \'<json>\'          内联 JSON 数组');
  console.log('  --replies-file <path>        JSON 文件路径');
  console.log('  --author --content --text    单条便捷写法');
  console.log('  --delay-ms <ms>              多条回复之间的间隔（默认 5000）');
  console.log('');
}

// ── 主动作：run(args, page) ─────────────────────────────────────────
/**
 * 跑一次 comment_list 或 reply，返回 JSON 结果。
 *
 * 不负责浏览器生命周期（启动/关）——那是调用方（CLI 或其他模块）的职责。
 * 不写文件——返回值就是 JSON。
 *
 * @param {object} args  parseArgs() 的返回值
 * @param {import('playwright').Page} page
 * @returns {Promise<object>}
 *   - action='comment-list' → comment_list(page, title) 的返回：{ video, stats, comments }
 *   - action='reply'        → reply(page, title, list, opts) 的返回：{ ok, replies: [...] }
 *   title 可省略（此时选第一个作品，index 0）；reply 失败时同时设置 process.exitCode = 1（让 shell 流水线能感知）。
 */
async function run(args, page) {
  if (!args || !args.action) {
    throw new Error('[run] args.action 缺失，先调 parseArgs');
  }

  if (args.action === 'comment-list') {
    return await comment_list(page, args.title, args.index);
  }

  if (args.action === 'reply') {
    const replyOpts = {
      index: args.index,
      delayMs: args.delayMs !== undefined ? args.delayMs : 5000,
    };
    const replyResult = await reply(page, args.title, args.list, replyOpts);
    if (replyResult.replies.some(r => !r.ok)) {
      process.exitCode = 1;
    }
    return replyResult;
  }

  throw new Error(`[run] unknown action: ${args.action}`);
}

module.exports = {
  run,
  parseArgs,
};

// ── CLI 入口 ────────────────────────────────────────────────────────
// 只有直接 `node index.js ...` 才跑这段；`require('./index.js')` 时跳过。
if (require.main === module) {
  (async () => {
    const args = parseArgs(process.argv);

    const context = await chromium.launchPersistentContext(USER_DATA_DIR, { headless: false });
    const page = context.pages()[0] || (await context.newPage());
    await page.goto(TARGET, { waitUntil: 'domcontentloaded' });
    await WL.waitForLogin(page);

    try {
      const result = await run(args, page);
      // stdout 唯一输出：run() 的 JSON 返回值
      console.log(JSON.stringify(result));
    } finally {
      await context.close().catch(() => {});
    }
  })().catch(e => {
    console.error('[index] ERROR:', e);
    process.exit(1);
  });
}