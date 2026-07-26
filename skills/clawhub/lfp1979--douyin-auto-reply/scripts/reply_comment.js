// reply_comment.js — 指定一条评论自动回复（写入能力）。
//
// 公开 API：
//   const { replyToComment } = require('./reply_comment');
//
//   const { comments } = await fetchComments(page, { ... });
//   const target = comments.find(c => /* 你的筛选 */);
//
//   const result = await replyToComment(page, {
//     target: { id: target.id, user: target.user, content: target.content },
//     text: '谢谢支持，欢迎常来 🎉',
//     onProgress: (s) => console.log(s),
//   });
//
// 返回结构：
//   { ok: true,  target_id, reply_text }
//   | { ok: false, reason, detail, screenshot }
//
//   reason 取值：
//     - 'card-not-found'      [data-comment-id] 不存在（要先 fetchComments）
//     - 'reply-btn-not-found' 操作行 / "回复"按钮 缺失
//     - 'toolbar-not-found'   点击"回复"后输入框工具栏未出现
//     - 'input-not-found'     工具栏内没找到 contenteditable 输入框
//     - 'send-still-disabled' 输入文字后"发送"按钮仍 disabled
//     - 'send-no-effect'      点击"发送"后 6 秒内 toolbar 没消失
//
// ── 选择器策略（zero-hash，全部基于实测 DOM）─────────────────────
//   • 目标卡片：[data-comment-id="${id}"]
//   • 操作行：div 内文本 /^\d+\s+回复\s+删除\s+举报$/
//   • "回复"按钮：操作行内 innerText.trim() === '回复' 的元素
//   • 输入框：[contenteditable="true"][placeholder^="回复"]
//   • 发送按钮：BUTTON 文字='发送'（在同一 toolbar 内）
//   • 取消按钮：BUTTON 文字='取消'（在同一 toolbar 内，失败兜底用）
//
// 完全避开 hash className（className 是 styled-components 生成的，
// 每次构建 hash 都会变；不参与匹配就不踩这个雷）。
// ─────────────────────────────────────────────────────────────────────

const path = require('path');

// ── 坐标点击 ───────────────────────────────────────────────────────
//
// 项目惯例：DOM 更新后 ElementHandle 会失效，坐标点击更鲁棒。
async function clickAt(page, x, y) {
  await page.mouse.click(Math.round(x), Math.round(y));
}

// ── 失败时截图（写到工作目录）────────────────────────────────────────
async function snap(page, tag) {
  try {
    const file = path.join(__dirname, `reply_err_${tag}_${Date.now()}.png`);
    await page.screenshot({ path: file, fullPage: true });
    return file;
  } catch { return null; }
}

// ── 共用 evaluate 片段：把"通过 [data-comment-id] 找 card"统一在一处 ──
//
// 在 page.evaluate 里：
//   - 顶级评论：返回 card 节点本身
//   - 二级回复：返回 reply-list wrapper（包所有二级回复的 container）
//
// 这样后续所有"在 card 里找操作行 / 回复按钮 / toolbar"的代码都不用
// 再区分顶级/二级。
function makeResolveCardJS() {
  return `
    function resolveCard(id) {
      // 用属性选择器定位 [data-comment-id]，零 className 依赖
      const el = document.querySelector('[data-comment-id="' + id + '"]');
      if (!el) return null;
      const replyList = el.closest('[class*="reply-list-"]');
      if (replyList) {
        // 二级回复：从 reply-list 里找"真正的 wrapper"（非 load-more / 收起）
        const wrappers = Array.from(replyList.children).filter(function(c) {
          var t = (c.innerText || '').trim();
          return !/查看\\s*\\d+\\s*条回复/.test(t) && t !== '收起';
        });
        return wrappers[0] || null;
      }
      // 顶级评论：card 节点本身
      return el;
    }
  `;
}

// ── 关闭当前打开的所有回复输入框（兜底清理）──────────────────────────
async function closeAllOpenReplyToolbars(page) {
  await page.evaluate(() => {
    Array.from(document.querySelectorAll('button'))
      .filter(b => (b.innerText || '').trim() === '取消' && b.offsetParent !== null)
      .forEach(b => b.click());
  });
}

// ─────────────────────────── 公开 API ───────────────────────────

/**
 * 对一条评论自动回复。
 *
 * @param {import('playwright').Page} page  Playwright 页面对象
 * @param {{
 *   target: { id: string, user?: { name?: string }, content?: string },
 *   text: string,
 *   onProgress?: (s: object) => void,
 *   screenshotOnError?: boolean,    // 失败时是否截图（默认 true）
 *   cancelOnError?: boolean,       // 失败时是否主动点"取消"清理 toolbar（默认 true）
 * }} opts
 *
 * @returns {Promise<{ok: true, target_id, reply_text} | {ok: false, reason, detail, screenshot?}>}
 */
async function replyToComment(page, {
  target,
  text,
  onProgress = () => {},
  screenshotOnError = true,
  cancelOnError = true,
}) {
  const fail = async (reason, detail) => {
    if (cancelOnError) await closeAllOpenReplyToolbars(page);
    const screenshot = screenshotOnError ? await snap(page, reason) : null;
    return { ok: false, reason, detail, screenshot };
  };

  // 1. 找目标卡片（自建 id 锚点，零 className 锚定）
  const resolveSrc = makeResolveCardJS();
  const cardFound = await page.evaluate(
    ({ id, src }) => {
      // eslint-disable-next-line no-new-func
      const resolve = new Function(src + '; return resolveCard(' + JSON.stringify(id) + ');');
      const card = resolve();
      if (!card) return { found: false };
      card.scrollIntoView({ block: 'center', behavior: 'instant' });
      // 等滚动稳定（下一 tick）
      return { found: true };
    },
    { id: target.id, src: resolveSrc }
  );

  if (!cardFound.found) {
    return await fail(
      'card-not-found',
      `No element with [data-comment-id="${target.id}"]. ` +
      `Make sure fetchComments() was called for the current video.`
    );
  }
  onProgress({ phase: 'card-found', id: target.id });
  await page.waitForTimeout(200); // 让 scrollIntoView 稳定

  // 2. 找"回复"按钮
  // ─────────────────────────────────────────────────────
  // fetch_comments.js 注入 id 时打在内层操作行（className 含 operations-* 前缀的 div）。
  // 因此这里直接 `[data-comment-id="${id}"]` 拿节点就是该 reply 的内层操作行，
  // 在它内部找"回复"按钮。零 zipped array 索引假设。
  const btnFound = await page.evaluate(
    ({ id, src }) => {
      // eslint-disable-next-line no-new-func
      const resolve = new Function(src + '; return resolveCard(' + JSON.stringify(id) + ');');
      const card = resolve();
      if (!card) return { found: false, reason: 'card-gone' };

      // 直接拿 id 节点（顶级评论 = card 自身；二级评论 = card 内部的 wrapper）
      // ⚠️ 顶级评论的 data-comment-id 锚点打在 card 自己身上，
      //    card.querySelector('[data-comment-id="cN"]') 在自身内查不到，必须 fallback 到 card。
      let actionRow = card.querySelector(`[data-comment-id="${id}"]`);
      if (!actionRow) {
        if (card.getAttribute('data-comment-id') === id) {
          actionRow = card;  // 顶级评论：card 本身就是 action row
        } else {
          return { found: false, reason: 'no-id-in-card' };
        }
      }

      // 在操作行内找"回复"按钮（text 严格匹配 + 子节点 ≤ 2，过滤噪声）
      const btn = Array.from(actionRow.querySelectorAll('*'))
        .find(el => {
          const t = (el.innerText || '').trim();
          return t === '回复' && el.children.length <= 2;
        });
      if (!btn) return { found: false, reason: 'no-reply-btn-in-action-row' };

      btn.scrollIntoView({ block: 'center', behavior: 'instant' });
      const r = btn.getBoundingClientRect();
      return { found: true, x: r.x + r.width / 2, y: r.y + r.height / 2 };
    },
    { id: target.id, src: resolveSrc }
  );

  if (!btnFound.found) {
    return await fail(
      'reply-btn-not-found',
      `Could not find "回复" button in action row of [data-comment-id="${target.id}"]. ` +
      `Reason: ${btnFound.reason || 'unknown'}`
    );
  }
  onProgress({ phase: 'reply-btn-found' });

  // 3. 点击"回复"按钮
  await clickAt(page, btnFound.x, btnFound.y);

  // 4. 等 toolbar 出现（找含 input + 发送按钮 的最小祖先）
  let toolbarReady = null;
  for (let attempt = 0; attempt < 30; attempt++) {
    toolbarReady = await page.evaluate(
      ({ id, src }) => {
        // eslint-disable-next-line no-new-func
        const resolve = new Function(src + '; return resolveCard(' + JSON.stringify(id) + ');');
        const card = resolve();
        if (!card) return { ready: false };
        const ces = Array.from(card.querySelectorAll('[contenteditable="true"]'));
        for (const ce of ces) {
          // sanity check: placeholder 必须以 "回复" 开头（排除顶部"主动发评论"那个）
          const ph = (ce.getAttribute('placeholder') || ce.getAttribute('aria-placeholder') || '');
          if (!/^回复\s/.test(ph)) continue;
          // walk-up 找含"发送"按钮的最小祖先
          let toolbar = ce.parentElement;
          while (toolbar && toolbar !== document.body) {
            const sendBtn = Array.from(toolbar.querySelectorAll('button'))
              .find(b => (b.innerText || '').trim() === '发送');
            if (sendBtn) return { ready: true, placeholder: ph };
            toolbar = toolbar.parentElement;
          }
        }
        return { ready: false };
      },
      { id: target.id, src: resolveSrc }
    );
    if (toolbarReady.ready) break;
    await page.waitForTimeout(200);
  }

  if (!toolbarReady || !toolbarReady.ready) {
    return await fail(
      'toolbar-not-found',
      `No reply toolbar appeared within 6s after clicking "回复". ` +
      `Expected contenteditable with placeholder starting with "回复 " inside the target card.`
    );
  }
  onProgress({ phase: 'toolbar-found', placeholder: toolbarReady.placeholder });

  // 5. 输入文本（纯 evaluate：focus + innerHTML + InputEvent，绕过键盘事件依赖）
  const inputResult = await page.evaluate(
    ({ id, src, text }) => {
      // eslint-disable-next-line no-new-func
      const resolve = new Function(src + '; return resolveCard(' + JSON.stringify(id) + ');');
      const card = resolve();
      if (!card) return { ok: false, reason: 'card-gone' };
      const ce = Array.from(card.querySelectorAll('[contenteditable="true"]'))
        .find(el => /^回复\s/.test((el.getAttribute('placeholder') || el.getAttribute('aria-placeholder') || '')));
      if (!ce) return { ok: false, reason: 'no-input' };
      ce.focus();
      // ★ 用 innerHTML 而不是 innerText，保留 emoji / 多行结构
      ce.innerHTML = text;
      // ★ 派发 InputEvent 触发 React 状态更新（已实测：disabled 翻转为 false）
      ce.dispatchEvent(new InputEvent('input', {
        bubbles: true,
        inputType: 'insertText',
        data: text,
      }));
      return { ok: true, len: ce.innerText.length };
    },
    { id: target.id, src: resolveSrc, text }
  );

  if (!inputResult.ok) {
    return await fail('input-not-found', `Reason: ${inputResult.reason || 'unknown'}`);
  }
  onProgress({ phase: 'text-typed', len: inputResult.len });

  // 6. 等"发送"按钮 enabled
  await page.waitForTimeout(300);
  const sendBtn = await page.evaluate(
    ({ id, src }) => {
      // eslint-disable-next-line no-new-func
      const resolve = new Function(src + '; return resolveCard(' + JSON.stringify(id) + ');');
      const card = resolve();
      if (!card) return { found: false };
      // 在 toolbar 内（和输入框同一个工具栏）找"发送"按钮
      const ce = Array.from(card.querySelectorAll('[contenteditable="true"]'))
        .find(el => /^回复\s/.test((el.getAttribute('placeholder') || el.getAttribute('aria-placeholder') || '')));
      if (!ce) return { found: false };
      let toolbar = ce.parentElement;
      while (toolbar && toolbar !== document.body) {
        const btn = Array.from(toolbar.querySelectorAll('button'))
          .find(b => (b.innerText || '').trim() === '发送');
        if (btn) {
          const r = btn.getBoundingClientRect();
          return {
            found: true,
            disabled: btn.disabled,
            x: r.x + r.width / 2,
            y: r.y + r.height / 2,
          };
        }
        toolbar = toolbar.parentElement;
      }
      return { found: false };
    },
    { id: target.id, src: resolveSrc }
  );

  if (!sendBtn.found) {
    return await fail('toolbar-not-found', '"发送" button disappeared after typing');
  }
  if (sendBtn.disabled) {
    return await fail('send-still-disabled',
      '"发送" button still disabled after typing. ' +
      'Input may not have triggered React state update.');
  }
  onProgress({ phase: 'send-btn-enabled' });

  // 7. 点击"发送"
  await clickAt(page, sendBtn.x, sendBtn.y);

  // 8. 等 toolbar 消失（成功标志）
  let disappeared = false;
  for (let attempt = 0; attempt < 30; attempt++) {
    const stillOpen = await page.evaluate(
      ({ id, src }) => {
        // eslint-disable-next-line no-new-func
        const resolve = new Function(src + '; return resolveCard(' + JSON.stringify(id) + ');');
        const card = resolve();
        if (!card) return false;
        return !!Array.from(card.querySelectorAll('[contenteditable="true"]'))
          .find(el => /^回复\s/.test((el.getAttribute('placeholder') || el.getAttribute('aria-placeholder') || '')));
      },
      { id: target.id, src: resolveSrc }
    );
    if (!stillOpen) { disappeared = true; break; }
    await page.waitForTimeout(200);
  }

  if (!disappeared) {
    return await fail('send-no-effect',
      '"发送" clicked but reply toolbar still visible after 6s. ' +
      'Check network / 抖音 server response.');
  }
  onProgress({ phase: 'reply-sent' });

  return { ok: true, target_id: target.id, reply_text: text };
}

module.exports = { replyToComment };
