// fetch_comments.js — 抓取当前页面显示的抖音视频的评论数据 + 注入 DOM 锚点。
//
// 公开 API：
//   const { fetchComments } = require('./fetch_comments');
//
//   const result = await fetchComments(page, {
//     expandReplies: true,   // 是否自动点开每条评论下的"查看 X 条回复"
//     scrollPages: 1,        // 滚动加载几页（每页约 20 条）
//     onProgress: (s) => console.log(s),
//   });
//
//   console.log(JSON.stringify(result, null, 2));
//
// 返回结构：
//   {
//     fetched_at: "2026-06-18T11:30:00.000Z",
//     video: { title: "...", video_id: null },
//     comments: [
//       {
//         id: "c1",
//         parent_id: null,
//         level: 1,
//         user: { name: "...", avatar: "...", is_author: false },
//         content: "...",
//         time: "06月07日 17:06",
//         like_count: 0,
//         replies: [
//           { id: "c1-r1", parent_id: "c1", level: 2, ..., reply_to: "..." },
//         ]
//       },
//     ],
//     stats: { top_count, reply_count, total }
//   }
//
// ── DOM 锚点注入（与 comments 数组中的 id 严格对齐）─────────────────
// 每次 fetchComments 都会：
//   1) 清掉页面上所有残留的 [data-comment-id]（防切换作品后混淆）
//   2) 给每条顶级评论卡注入 data-comment-id="c1"/"c2"/...
//   3) 给每条二级回复（reply-list wrapper 内的 username 节点）
//      注入 data-comment-id="c1-r1"/"c1-r2"/...
//
// 这样 reply_comment.js 可以用纯 [data-comment-id="c1-r2"] 定位，
// **完全避开 hash className 和 innerText 模糊匹配**。
//
// 切换作品后必须重新调 fetchComments，新一轮的 id 才能用。
//
// ── 稳定性说明 ──────────────────────────────────────────────────────
// 评论卡片的识别完全基于**语义前缀**
// （`comment-content-text-`, `username-`, `time-`, `reply-list-`, `load-more-`）
// 和**结构特征**（"同时包含 username + time + content-text 的最近祖先 div"）。
// 不依赖任何 hash 后缀，hash 改了不会失效。
// ─────────────────────────────────────────────────────────────────────

const sel = require('./selectors');

// ─────────────────────────── 辅助函数 ───────────────────────────

/** 在坐标上点击。坐标点击对 DOM 更新后的 stale element handle 更鲁棒。 */
async function clickAt(page, x, y) {
  await page.mouse.click(Math.round(x), Math.round(y));
}

/** 滚动评论列表到底，直到出现"没有更多评论"标记为止。 */
async function scrollListUntilNoMore(page, { maxPages = 1, onProgress = () => {} } = {}) {
  for (let p = 0; p < maxPages; p++) {
    const state = await page.evaluate(() => {
      // "没有更多评论" 这种文案会出现在 loading-* 元素里
      const loadingDone = Array.from(document.querySelectorAll('[class*="loading-"]'))
        .some(el => /没有更多评论|没有更多|已加载全部/.test(el.innerText || ''));
      if (loadingDone) return { done: true };
      return { done: false };
    });
    if (state.done) { onProgress({ phase: 'scroll', pages: p, status: 'no-more' }); return; }

    onProgress({ phase: 'scroll', pages: p + 1 });
    await page.evaluate(() => {
      // 找评论列表的可滚动容器：从 comment-content-text 元素往上爬，
      // 找到第一个 overflow 是 auto/scroll 且内容明显比容器高的祖先。
      const sample = document.querySelector('[class*="comment-content-text-"]');
      if (!sample) return;
      let container = sample.parentElement;
      while (container && container !== document.body) {
        const cs = getComputedStyle(container);
        const isScrollable = /(auto|scroll)/.test(cs.overflow + cs.overflowY);
        const tall = container.scrollHeight > container.clientHeight + 100;
        if (isScrollable && tall) break;
        container = container.parentElement;
      }
      if (container) container.scrollTo({ top: container.scrollHeight, behavior: 'instant' });
      else window.scrollTo(0, document.body.scrollHeight);
    });
    await page.waitForTimeout(1500);
  }
}

/** 点开所有一级评论下的"查看 X 条回复"按钮，把回复都展开。 */
async function expandAllReplies(page, { onProgress = () => {} } = {}) {
  // 用坐标点击 —— 元素被点击后会被替换成回复项，DOM 引用就失效了。
  // 每轮重新按位置找下一个，比 ElementHandle 更稳。
  //
  // "展开回复"按钮正则：兼容 "查看 / 展开 / 显示" 三种动词前缀，
  // 容忍"X 条回复"或"X 回复"两种说法。**显式排除"收起"按钮**。
  const SHOW_REPLY_RE = /(?:查看|展开|显示)\s*\d+\s*(?:条)?\s*回复/;
  let expanded = 0;
  let lastY = -1;
  let repeatY = 0;
  while (expanded < 500) {
    const target = await page.evaluate((reSrc) => {
      const showRe = new RegExp(reSrc);
      const btns = Array.from(document.querySelectorAll('[class*="load-more-"]'))
        .filter(el => showRe.test(el.innerText || ''))                 // ★ 是"展开回复"按钮
        .filter(el => !/^\s*收起\s*$/.test(el.innerText || ''))         // 排除"收起"
        .filter(el => el.closest('[class*="reply-list-"]'))            // ★ 必须位于 reply-list 内
        .filter(el => {
          const r = el.getBoundingClientRect();
          return r.width > 0 && r.height > 0;
        });
      // 按 Y 排序，从上到下展开
      btns.sort((a, b) => a.getBoundingClientRect().y - b.getBoundingClientRect().y);
      if (!btns.length) return null;
      const btn = btns[0];
      btn.scrollIntoView({ block: 'center', behavior: 'instant' });
      const r = btn.getBoundingClientRect();
      return { x: r.x + r.width / 2, y: r.y + r.height / 2, total: btns.length };
    }, SHOW_REPLY_RE.source);
    if (!target) { onProgress({ phase: 'expand-reply', status: 'no-more-buttons', expanded }); break; }
    if (target.y === lastY) {
      repeatY++;
      if (repeatY >= 3) { onProgress({ phase: 'expand-reply', status: 'stuck-same-y', y: target.y }); break; }
    } else { repeatY = 0; lastY = target.y; }
    await clickAt(page, target.x, target.y);
    expanded++;
    onProgress({ phase: 'expand-reply', expanded, remaining: target.total });
    await page.waitForTimeout(800);
  }
  return expanded;
}

// ─────────────────────────── 解析（一次性往返） ───────────────────────────

/**
 * 在一次 page.evaluate() 调用里把整个评论树解析完成。
 * 返回原始行：[{ index, top: { user, time, content, like_count, avatar, is_author },
 *                 replies: [ { user, time, content, like_count, reply_to, is_author } ] }]
 *
 * 识别策略 —— 纯结构 + 语义前缀，不依赖 hash className：
 *   • comment-content-text-* / username-* / time-* 是源码里稳定的"前缀"
 *   • reply-list-* 标记回复容器
 *   • 顶级评论 = "comment-content-text 的最近祖先，
 *                同时含 username + time + content-text，且不在 reply-list 内"
 *   • 在 reply-list wrapper 内，每个回复各贡献一个 username / time /
 *     comment-content-text / 操作行，按文档顺序 zip
 */
async function parseAllInPage(page) {
  return await page.evaluate(() => {
    // ── 清掉所有残留的 data-comment-id（防切换作品后旧 id 干扰）──
    document.querySelectorAll('[data-comment-id]').forEach(el => el.removeAttribute('data-comment-id'));

    function findTopLevelCards() {
      const texts = Array.from(document.querySelectorAll('[class*="comment-content-text-"]'));
      const seen = new Set();
      const out = [];
      for (const textEl of texts) {
        // 往上找最近的、同时含 username + time + content-text 的祖先
        let card = textEl;
        while (card && card !== document.body) {
          const hasUser = !!card.querySelector('[class*="username-"]');
          const hasTime = !!card.querySelector('[class*="time-"]');
          const hasContent = !!card.querySelector('[class*="comment-content-text-"]');
          if (hasUser && hasTime && hasContent) break;
          card = card.parentElement;
        }
        if (!card || card === document.body) continue;
        // 跳过 reply-list 内部的（即二级回复自身）
        if (card.closest('[class*="reply-list-"]')) continue;
        if (seen.has(card)) continue;
        seen.add(card);
        out.push(card);
      }
      return out;
    }

    /**
     * 把用户名元素里的"作者"徽章拆出来。
     * 抖音的"作者"徽章是 username 元素内部的子节点，innerText 可能
     * 是 "飞龙\n作者"，但 DOM 上是嵌套结构 —— 我们把徽章从 DOM 里
     * 移除后再读 innerText 就只剩用户名了。
     */
    function splitBadge(usernameEl) {
      let isAuthor = false;
      const badge = Array.from(usernameEl.querySelectorAll('*'))
        .find(n => (n.innerText || '').trim() === '作者' && n.children.length === 0);
      if (badge) { isAuthor = true; badge.remove(); }
      const name = (usernameEl.innerText || '').trim() || null;
      return { name, isAuthor };
    }

    /** 解析单个一级评论卡片。返回的 _replyListEl 是 DOM 引用，外部处理完会删。 */
    function parseOneCard(card) {
      const $ = (s) => card.querySelector(s);
      const $$ = (s) => Array.from(card.querySelectorAll(s));

      const usernameEl = $('[class*="username-"]');
      const { name: user, isAuthor } = usernameEl
        ? splitBadge(usernameEl)
        : { name: null, isAuthor: false };

      const time = ($('[class*="time-"]')?.innerText || '').trim() || null;
      const content = ($('[class*="comment-content-text-"]')?.innerText || '').trim() || null;

      // 操作行 "0 回复 删除 举报" 里的开头的数字就是点赞数
      let like_count = 0;
      const actionRow = $$('div').find(d => {
        const t = (d.innerText || '').trim();
        return /^\d+\s+回复\s+删除\s+举报$/.test(t);
      });
      if (actionRow) {
        const m = actionRow.innerText.match(/^(\d+)/);
        if (m) like_count = parseInt(m[1], 10);
      }

      // 头像：取 avatar img 的 src
      const img = card.querySelector('[class*="douyin-creator-interactive-avatar"] img');
      const avatar = (img && img.src) || null;

      // 回复列表容器（即使没展开也在 DOM 里，只是没内容）
      const replyList = $('[class*="reply-list-"]');

      return { user, time, content, like_count, avatar, is_author: isAuthor, _replyListEl: replyList };
    }

    /**
     * 解析回复列表 wrapper（展开后，里面装着所有二级回复）。
     *
     * DOM 结构：
     *   <div class="reply-list-QwXCb_">
     *     <div class="container-sXKyMs">     ← wrapper（所有回复都在这）
     *       <span checkbox-1> <span avatar-1>
     *       <div content-1>
     *         <div>
     *           <username-1> <time-1> <content-text-1> <operations-1>
     *         </div>
     *       </div>
     *       <span checkbox-2> ...             ← 回复 2
     *       ...
     *     </div>
     *     <div load-more>收起</div>            ← 也可能是"查看 X 条回复"（未展开时）
     *   </div>
     */
    function parseReplyList(replyList) {
      if (!replyList) return [];
      // 排除 "查看 X 条回复" / "收起" 这种按钮 child
      const wrappers = Array.from(replyList.children).filter(c => {
        const t = (c.innerText || '').trim();
        if (/查看\s*\d+\s*条回复/.test(t)) return false;
        if (t === '收起' || /^收起\s*$/.test(t)) return false;
        return true;
      });
      if (!wrappers.length) return [];
      const wrapper = wrappers[0];

      // 每条回复各贡献一个 username / time / content-text / 操作行
      const usernames = Array.from(wrapper.querySelectorAll('[class*="username-"]'));
      const times = Array.from(wrapper.querySelectorAll('[class*="time-"]'));
      const contents = Array.from(wrapper.querySelectorAll('[class*="comment-content-text-"]'));
      const actionRows = Array.from(wrapper.querySelectorAll('div')).filter(d => {
        const t = (d.innerText || '').trim();
        return /^\d+\s+回复\s+删除\s+举报$/.test(t);
      });
      const n = Math.min(usernames.length, times.length, contents.length, actionRows.length);
      const out = [];
      for (let i = 0; i < n; i++) {
        const { name: user, isAuthor } = splitBadge(usernames[i]);
        // 内容里可能带 "回复 XX: " 前缀，把它剥出来作为 reply_to
        let content = (contents[i].innerText || '').trim();
        let reply_to = null;
        const m = content.match(/^回复\s*([^:：]+)\s*[:：]\s*(.*)$/s);
        if (m) { reply_to = m[1].trim(); content = m[2].trim(); }
        let like_count = 0;
        const am = actionRows[i].innerText.match(/^(\d+)/);
        if (am) like_count = parseInt(am[1], 10);
        out.push({
          user, time: (times[i].innerText || '').trim() || null,
          content, like_count, reply_to, is_author: isAuthor,
        });
      }
      return out;
    }

    return findTopLevelCards().map((card, i) => {
      const top = parseOneCard(card);
      const replyList = top._replyListEl;
      delete top._replyListEl;
      const replies = parseReplyList(replyList);

      // ── 注入 data-comment-id 锚点 ──
      // 顶级评论：id 打 card 节点本身
      const cId = `c${i + 1}`;
      card.setAttribute('data-comment-id', cId);
      // 二级回复：扁平结构，id 打 wrapper 内每个"内层操作行"
      // ─────────────────────────────────────────────────────
      // 重要：抖音 DOM 里每条二级回复有 2 层嵌套的"0 回复 删除 举报" div：
      //   • 外层：className 空
      //   • 内层：className 含 operations-* 前缀（语义词，hash 后缀被 *= 截断）
      // 如果按 usernames 数组顺序注入，会和 reply_comment 的 actionRows[targetIdx]
      // 错位（elementFromPoint 命中内层而不是外层）。
      // 解决：直接按 "operations- 前缀" 过滤，命中每条 reply 真正的内层操作行。
      // reply_comment 拿到 id 节点后，在它内部找"回复"按钮即可，零 zipped array 索引假设。
      if (replyList) {
        const wrappers = Array.from(replyList.children).filter(c => {
          const t = (c.innerText || '').trim();
          return !/查看\s*\d+\s*条回复/.test(t) && t !== '收起';
        });
        const w = wrappers[0];
        if (w) {
          const innerActionRows = Array.from(w.querySelectorAll('[class*="operations-"]'))
            .filter(d => /^\d+\s+回复\s+删除\s+举报$/.test((d.innerText || '').trim().replace(/\s+/g, ' ')));
          innerActionRows.forEach((row, j) =>
            row.setAttribute('data-comment-id', `${cId}-r${j + 1}`)
          );
        }
      }

      return { index: i, top, replies };
    });
  });
}

// ─────────────────────────── 公开 API ───────────────────────────

/**
 * 抓取当前页面上显示的视频的评论。
 *
 * @param {import('playwright').Page} page  Playwright 页面对象
 * @param {{
 *   expandReplies?: boolean,        // 是否自动展开所有二级回复（默认 true）
 *   scrollPages?: number,            // 滚动加载几页（默认 1）
 *   onProgress?: (s: object) => void, // 进度回调
 * }} [opts]
 */
async function fetchComments(page, {
  expandReplies = true,
  scrollPages = 1,
  onProgress = () => {},
} = {}) {
  // 等至少一个评论文本节点挂载到 DOM（不要求可见，避免首条评论被
  // sticky header 遮挡 / 动画未完成时误判；后面 fetchComments 是要抓所有
  // 评论数据的，不依赖首条 visible）
  await page.waitForSelector(sel.COMMENT_TEXT, { state: 'attached', timeout: 10000 });

  // 滚动加载更多
  await scrollListUntilNoMore(page, { maxPages: scrollPages, onProgress });
  await page.waitForTimeout(800);

  // 展开所有二级回复
  if (expandReplies) {
    await expandAllReplies(page, { onProgress });
    await page.waitForTimeout(800);
  }

  // 一次性解析全部评论
  const raw = await parseAllInPage(page);
  onProgress({ phase: 'parse-all', top_count: raw.length });

  // 整形成对外文档承诺的 schema
  const comments = raw.map(({ index, top, replies }) => ({
    id: `c${index + 1}`,
    parent_id: null,
    level: 1,
    user: { name: top.user, avatar: top.avatar, is_author: top.is_author },
    content: top.content,
    time: top.time,
    like_count: top.like_count,
    replies: replies.map((r, ri) => ({
      id: `c${index + 1}-r${ri + 1}`,
      parent_id: `c${index + 1}`,
      level: 2,
      user: { name: r.user, is_author: r.is_author },
      content: r.content,
      time: r.time,
      like_count: r.like_count,
      reply_to: r.reply_to,
    })),
  }));

  const reply_count = comments.reduce((acc, c) => acc + c.replies.length, 0);

  // 视频标题：在同时含"选择作品"和"发布于"的最小元素里抽中间那段
  const videoTitle = await page.evaluate(() => {
    const all = Array.from(document.querySelectorAll('div, section, header'));
    const candidates = all.filter(el => {
      const t = (el.innerText || '').replace(/\s+/g, ' ');
      return /选择作品/.test(t) && /发布于/.test(t) && t.length < 1500;
    });
    if (!candidates.length) return null;
    candidates.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    const t = (candidates[0].innerText || '').replace(/\s+/g, ' ');
    const m = t.match(/选择作品\s*(.+?)\s*发布于/);
    return m ? m[1].trim() : null;
  });

  return {
    fetched_at: new Date().toISOString(),
    video: { title: videoTitle, video_id: null },
    comments,
    stats: { top_count: comments.length, reply_count, total: comments.length + reply_count },
  };
}

module.exports = { fetchComments };
