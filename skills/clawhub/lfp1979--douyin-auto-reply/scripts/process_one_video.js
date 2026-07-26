// process_one_video.js — 在指定视频下做"抓评论列表"和"批量回复"两个动作。
//
// 假设调用方已经把 page 准备好：已经登录、已经在创作者中心评论管理页。
// 这里不负责登录、跳页、关浏览器 —— 那是测试脚本和业务编排的职责。

const { fetchComments } = require('./fetch_comments');
const { replyToComment } = require('./reply_comment');
const WL = require('./work-list-actions');

/**
 * 选中指定 title 或 index 的视频，并抓取其评论列表。
 *
 * 三选一：
 *   - 传 title   → clickWorkByName(page, title)（子串匹配）
 *   - 传 index   → clickWorkByIndex(page, index)（按位置）
 *   - 都不传     → clickWorkByIndex(page, 0)（选第一个作品）
 *
 * @param {import('playwright').Page} page
 * @param {string} [title]  视频作品名称（精确或模糊匹配）
 * @param {number} [index]  视频作品 0-based 序号
 * @returns {Promise<{video, stats, comments}>}  fetchComments 的完整返回
 */
async function comment_list(page, title, index) {
  // 1. 选作品：index 优先 → 然后 title → 都没有就选第一个
  if (typeof index === 'number') {
    await WL.clickWorkByIndex(page, index);
  } else if (title != null) {
    await WL.clickWorkByName(page, title);
  } else {
    await WL.clickWorkByIndex(page, 0);
  }

  // 2. 抓评论（注入 data-comment-id 锚点）
  const result = await fetchComments(page, {
    expandReplies: true,
    scrollPages: 1,
  });

  return result;
}

/**
 * 选中指定 title 或 index 的视频，根据"作者名包含 + 内容包含"循环回复。
 * 0 匹配 / >1 匹配都会记到 replies[] 里但**不中断**循环。
 *
 * 三选一：传 title / 传 index / 都不传（选第一个作品）。同 comment_list。
 *
 * @param {import('playwright').Page} page
 * @param {string} [title]  视频作品名称。省略时若 index 也省略则选第一个作品。
 * @param {number} [index]  视频作品 0-based 序号
 * @param {Array<{author: string, content: string, text: string}>} list
 *        - author : 作者名（子串匹配 user.name）
 *        - content: 内容关键词（子串匹配 content）
 *        - text   : 回复文本
 * @param {object} [opts]
 * @param {number}  [opts.delayMs=5000]  多个回复之间的防爬间隔（ms），首条不等待
 * @returns {Promise<{ok: true, replies: Array}>}
 *          每条 replies[i]: { ok, target_id?, reply_text?, reason?, detail?, screenshot? }
 */
async function reply(page, title, list, opts = {}) {
  const { index, delayMs = 5000 } = opts;

  // 1. 选作品：index 优先 → 然后 title → 都没有就选第一个
  if (typeof index === 'number') {
    await WL.clickWorkByIndex(page, index);
  } else if (title != null) {
    await WL.clickWorkByName(page, title);
  } else {
    await WL.clickWorkByIndex(page, 0);
  }

  // 2. 抓评论（拿 id 锚点）
  const result = await fetchComments(page, {
    expandReplies: true,
    scrollPages: 1,
  });

  const replies = [];

  for (let i = 0; i < list.length; i++) {
    const { author, content, text } = list[i];

    // 3. 找目标：作者+内容匹配（顶级 + 二级一起扫）
    const candidates = [];
    for (const c of result.comments) {
      if ((c.user?.name || '').includes(author) &&
          (c.content || '').includes(content)) {
        candidates.push({ ...c, level: 1 });
      }
      for (const r of c.replies) {
        if ((r.user?.name || '').includes(author) &&
            (r.content || '').includes(content)) {
          candidates.push({ ...r, parent_id: c.id, level: 2 });
        }
      }
    }

    if (candidates.length === 0) {
      replies.push({
        ok: false, reason: 'not-found',
        detail: `作者含 "${author}" 且内容含 "${content}" 的评论不存在`,
        author, content,
      });
      continue;
    }
    if (candidates.length > 1) {
      replies.push({
        ok: false, reason: 'ambiguous',
        detail: `匹配到 ${candidates.length} 条，加更精确的关键词或用 --id`,
        candidates: candidates.map(c => ({
          id: c.id, level: c.level, user: c.user?.name,
          content: (c.content || '').slice(0, 40),
        })),
        author, content,
      });
      continue;
    }

    const target = candidates[0];

    // 4. 防爬间隔（首条不等待）
    if (i > 0 && delayMs > 0) {
      console.log(`[reply] (${i + 1}/${list.length}) 等待 ${delayMs}ms 后处理下一条...`);
      await page.waitForTimeout(delayMs);
    } else {
      console.log(`[reply] (${i + 1}/${list.length}) 处理: 作者含 "${author}" + 内容含 "${content}" → [${target.id}]`);
    }

    // 5. 调 replyToComment
    const r = await replyToComment(page, {
      target: { id: target.id, user: target.user, content: target.content },
      text,
    });

    if (r.ok) {
      replies.push({
        ok: true, target_id: target.id, reply_text: text,
      });
    } else {
      replies.push({
        ok: false, reason: r.reason, detail: r.detail, screenshot: r.screenshot,
        author, content,
      });
    }
  }

  return { ok: true, replies };
}

module.exports = { comment_list, reply };
