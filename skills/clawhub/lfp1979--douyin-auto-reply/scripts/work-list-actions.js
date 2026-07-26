/**
 * Douyin Creator Center - "Choose Work" popover actions
 *
 * Target page: https://creator.douyin.com/creator-micro/interactive/comment
 *
 * DOM structure (verified 2026-06-07):
 *   div[role="dialog"]                                  <- popover
 *     h1: "作品列表 共N个视频"
 *     ul.douyin-creator-interactive-list-items         <- list (stable class)
 *       > div[class^="container-"] [class*="active-"]   <- each item (CSS-module hash)
 *           img[class*="cover-"]                        <- thumbnail
 *           div[class*="content-"]
 *               div[class*="title-"]                    <- title (may be EMPTY)
 *               div[class*="desc-"]
 *                   div[class*="time-"]                 <- "发布于YYYY-MM-DD HH:mm"
 *           div[class*="right-"]                        <- right side
 *               span[class*="dux-icon"]                 <- comment icon
 *               div                                     <- comment count (number only)
 *
 *  Pitfalls:
 *   - Title can be empty (user uploaded without title) -- treat "" as a real value
 *   - Class names use CSS-module hash (e.g. "title-LUOP3b"), use attribute prefix match
 *   - Clicking an item CLOSES the dialog and switches the active work
 *   - "active-XXXXX" class on the item = currently selected work
 *
 * Usage:
 *   const WL = require('./work-list-actions');
 *   await WL.openWorkDialog(page);
 *   const works = await WL.listAllWorks(page);
 *   // works -> [{ index, title, date, count, hasTitle, isActive }, ...]
 *
 *   for (const w of works) {
 *     await WL.clickWorkByIndex(page, w.index);
 *     // dialog auto-closed, do your work here
 *   }
 *
 *   // Or by name (partial, case-insensitive):
 *   await WL.clickWorkByName(page, '野兔子');
 *
 *   // Or with options:
 *   await WL.clickWorkByName(page, '丝绸之路', { exact: false, index: 0 });
 */

'use strict';

const SELECTORS = Object.freeze({
  // Popover root -- scoped to the dialog so we never accidentally hit page-level elements
  dialog: 'div[role="dialog"]',

  // List (the only place this global class appears)
  list: 'ul.douyin-creator-interactive-list-items',
  // Each list item is a direct <div> child of the <ul>
  listItem: 'ul.douyin-creator-interactive-list-items > div',

  // Inside an item -- CSS-module hash, use attribute prefix match
  title: '[class*="title-"]',
  date: '[class*="time-"]',
  // "active-" prefix on the item class marks the currently selected work
  activeItem: 'ul.douyin-creator-interactive-list-items > div[class*="active-"]',

  // Trigger button on the main page
  triggerBtn: 'button:has-text("选择作品")',
});

/** Returns true if the popover is currently open. */
async function isWorkDialogOpen(page) {
  return (await page.locator(SELECTORS.dialog).count()) > 0;
}

/**
 * Open the "Choose Work" popover. No-op if already open.
 * Throws if the trigger button cannot be found (probably not on the right page).
 *
 * ⚠️ 关键：除了等 dialog / <ul> 出现，还会等 listItem 数量稳定
 * （列表项是异步加载的，<ul> 出现后还要等几百毫秒才能完整读出来），
 * 否则 listAllWorks / clickWorkByName 会读到部分加载的列表。
 */
async function openWorkDialog(page) {
  if (await isWorkDialogOpen(page)) return;

  const btn = page.locator(SELECTORS.triggerBtn).first();
  const exists = await btn.count();
  if (exists === 0) {
    throw new Error(
      '[openWorkDialog] Trigger button "选择作品" not found. ' +
      'Are you on https://creator.douyin.com/creator-micro/interactive/comment and logged in?'
    );
  }
  await btn.click();
  await page.locator(SELECTORS.dialog).waitFor({ state: 'visible', timeout: 5000 });
  await page.locator(SELECTORS.list).waitFor({ state: 'visible', timeout: 5000 });
  // 等 listItem 数量稳定（异步加载完成），避免读到部分列表
  await waitForWorkListReady(page);
}

/**
 * Wait until the popover's work list stops growing (item count stable for `stableMs`).
 * Returns the final item count. Times out gracefully at maxWaitMs.
 *
 * 为什么需要：点开「选择作品」后，dialog 和 <ul> 骨架立即出现，但里面的
 * <div> 列表项是异步分批渲染的。如果不等，读到的可能是空 / 部分列表。
 *
 * @param {import('playwright').Page} page
 * @param {object} [opts]
 * @param {number} [opts.stableMs=500]  数量稳定多少毫秒才认为加载完
 * @param {number} [opts.maxWaitMs=5000] 总超时（即使还在变也返回当前 count）
 * @param {number} [opts.pollMs=100]  轮询间隔
 * @returns {Promise<number>} 最终 listItem 数量
 */
async function waitForWorkListReady(page, opts = {}) {
  const { stableMs = 500, maxWaitMs = 5000, pollMs = 100 } = opts;
  const start = Date.now();
  let lastCount = -1;
  let lastChangeAt = Date.now();

  while (Date.now() - start < maxWaitMs) {
    const count = await page.locator(SELECTORS.listItem).count();
    const now = Date.now();
    if (count !== lastCount) {
      lastCount = count;
      lastChangeAt = now;
    } else if (count > 0 && now - lastChangeAt >= stableMs) {
      return count;
    }
    await page.waitForTimeout(pollMs);
  }
  return lastCount;
}

/**
 * Close the popover (Escape key, then wait for it to detach).
 * Safe to call even if not open.
 */
async function closeWorkDialog(page) {
  if (!(await isWorkDialogOpen(page))) return;
  await page.keyboard.press('Escape').catch(() => {});
  await page
    .locator(SELECTORS.dialog)
    .waitFor({ state: 'detached', timeout: 3000 })
    .catch(() => {});
}

/**
 * Read the metadata of every work in the popover. Opens the dialog if needed.
 *
 * @returns {Promise<Array<{
 *   index: number,      // 0-based, stable for this popover session
 *   title: string,      // may be ""
 *   date: string,       // "发布于YYYY-MM-DD HH:mm"
 *   count: number,      // comment count
 *   hasTitle: boolean,  // convenience: title.length > 0
 *   isActive: boolean,  // true if this is the currently selected work
 * }>>}
 */
async function listAllWorks(page) {
  await openWorkDialog(page);
  return await page.$$eval(SELECTORS.listItem, (items) => {
    return items.map((it, i) => {
      // Title: first descendant with class starting with "title-"
      const titleEl = it.querySelector('[class*="title-"]');
      const dateEl = it.querySelector('[class*="time-"]');
      // Comment count: last plain div child of the right-side block
      const right = it.querySelector('[class*="right-"]');
      const countEl = right ? right.querySelector('div:not([class])') : null;
      const countText = (countEl ? countEl.textContent : '0').trim();

      const title = (titleEl ? titleEl.textContent : '').trim();
      const date = (dateEl ? dateEl.textContent : '').trim();
      const count = Number(countText) || 0;
      const isActive = Array.from(it.classList).some((c) => c.indexOf('active-') === 0);

      return { index: i, title, date, count, hasTitle: title.length > 0, isActive };
    });
  });
}

/**
 * Return the number of works shown in the popover. Opens the dialog if needed.
 */
async function getWorkCount(page) {
  await openWorkDialog(page);
  return await page.locator(SELECTORS.listItem).count();
}

/**
 * Click the work at the given 0-based index. Opens the dialog if needed.
 * The dialog will close automatically after a successful click.
 *
 * @returns {Promise<{index:number, title:string, date:string}>}
 */
async function clickWorkByIndex(page, index) {
  if (!Number.isInteger(index) || index < 0) {
    throw new Error(`[clickWorkByIndex] index must be a non-negative integer, got ${index}`);
  }
  await openWorkDialog(page);

  const total = await page.locator(SELECTORS.listItem).count();
  if (index >= total) {
    throw new Error(
      `[clickWorkByIndex] out of range: index=${index}, but the popover has only ${total} works`
    );
  }

  const item = page.locator(SELECTORS.listItem).nth(index);
  await item.click({ timeout: 5000 });
  // The dialog auto-closes after a click. Wait for it to detach.
  // ⚠️ 只用 hasText 过滤，排除新手引导弹窗（如"共创中心"模块引导），
  // 因为页面可能同时存在多个 role="dialog"，Playwright strict mode 会报错。
  // ⚠️ 超时 8s 而非默认 5s：douyin 首次打开 dialog 时响应较慢，
  //    5s 偶发 11× visible 超时，8s 更稳。
  await page
    .locator(SELECTORS.dialog).filter({ hasText: '作品列表' })
    .waitFor({ state: 'detached', timeout: 8000 });

  // We can't return the exact post-click title from here without re-opening the dialog,
  // so return what we knew before the click.
  return { index, title: '', date: '' };
}

/**
 * Click a work by name. By default performs case-insensitive partial matching.
 *
 * @param {Page} page
 * @param {string} name - work title (or part of it)
 * @param {Object} [opts]
 * @param {boolean} [opts.exact=false] - require full title match (still case-insensitive)
 * @param {number} [opts.index=0] - when multiple matches, pick the Nth one (0-based)
 * @param {boolean} [opts.fallbackToIterate=false] - if popover is currently closed and
 *   matches may have changed since the last listAllWorks, re-list before matching
 *
 * @returns {Promise<{index:number, title:string, date:string, count:number}>} the matched work
 * @throws Error if 0 matches (with a helpful list of available titles in the message),
 *         or if `index` is out of range for the match list.
 */
async function clickWorkByName(page, name, opts) {
  if (typeof name !== 'string' || name.trim() === '') {
    throw new Error('[clickWorkByName] name must be a non-empty string');
  }
  const exact = !!(opts && opts.exact);
  const pickIndex = opts && Number.isInteger(opts.index) ? opts.index : 0;
  const needle = name.trim().toLowerCase();

  // Always re-list to avoid stale state (cheap: dialog stays open if already open).
  const works = await listAllWorks(page);

  const matches = exact
    ? works.filter((w) => w.title.toLowerCase() === needle)
    : works.filter((w) => w.title.toLowerCase().indexOf(needle) !== -1);

  if (matches.length === 0) {
    const sample = works
      .slice(0, 10)
      .map((w) => `    [${w.index}] ${w.title || '(无标题)'}`)
      .join('\n');
    throw new Error(
      `[clickWorkByName] no match for "${name}" (exact=${exact}). ` +
      `Popover has ${works.length} works. First 10:\n${sample}`
    );
  }
  if (pickIndex >= matches.length) {
    throw new Error(
      `[clickWorkByName] ${matches.length} matches for "${name}", but index=${pickIndex} is out of range.\n` +
      `Matches:\n` +
      matches.map((m) => `    [${m.index}] ${m.title}`).join('\n')
    );
  }

  const target = matches[pickIndex];
  await clickWorkByIndex(page, target.index);
  return target;
}

/**
 * Click each work in order, with `onEach(work, info)` called after each successful click.
 * The dialog will be re-opened automatically between iterations.
 *
 * @param {Page} page
 * @param {(work: {index:number, title:string, date:string, count:number}, info: {i:number, total:number}) => Promise<void>|void} onEach
 * @param {Object} [opts]
 * @param {number} [opts.delayMs=0] - delay between iterations (in ms)
 * @param {number} [opts.startFrom=0] - 0-based index to start from
 * @param {(i:number, err:Error) => boolean} [opts.onError] - return true to continue, false to throw
 *
 * @returns {Promise<Array<{index:number, title:string, date:string, count:number, ok:boolean, error?:Error}>>}
 */
async function iterateAllWorks(page, onEach, opts) {
  if (typeof onEach !== 'function') {
    throw new Error('[iterateAllWorks] onEach must be a function');
  }
  const delayMs = (opts && opts.delayMs) || 0;
  const startFrom = (opts && Number.isInteger(opts.startFrom)) ? opts.startFrom : 0;
  const onError = opts && opts.onError;

  const works = await listAllWorks(page);
  const results = [];

  for (let i = startFrom; i < works.length; i++) {
    const w = works[i];
    let entry = { index: w.index, title: w.title, date: w.date, count: w.count, ok: true };
    try {
      await clickWorkByIndex(page, w.index);
      // Dialog is now closed, the work is selected. Run the user callback.
      await onEach(w, { i, total: works.length });
    } catch (err) {
      entry.ok = false;
      entry.error = err;
      results.push(entry);
      if (onError) {
        const shouldContinue = onError(i, err);
        if (!shouldContinue) throw err;
      } else {
        throw err;
      }
      // Make sure dialog is closed before next iteration.
      await closeWorkDialog(page).catch(() => {});
      continue;
    }
    results.push(entry);
    if (delayMs > 0 && i < works.length - 1) {
      await page.waitForTimeout(delayMs);
    }
  }

  return results;
}
/**
 * 等待用户登录成功（死等，不需要回车）。
 * 登录成功的标志：评论管理页左上角的"选择作品"按钮变为可见。
 *
 * @param {import('playwright').Page} page
 * @param {number} [timeoutMs=300000] 超时时间（默认 5 分钟）
 * @throws 超时仍未登录时抛错（带明确提示）
 */
async function waitForLogin(page, timeoutMs = 5 * 60 * 1000) {
  try {
    await page
      .getByRole('button', { name: '选择作品' })
      .waitFor({ state: 'visible', timeout: timeoutMs });
  } catch (e) {
    // Playwright 超时报错信息里包含 "Timeout" 字样
    if (/Timeout/i.test(e.message)) {
      throw new Error(
        `[waitForLogin] 登录超时（${Math.round(timeoutMs / 1000)}s），` +
        `"选择作品" 按钮仍未出现。请确认：\n` +
        `  1. 已用浏览器手动登录抖音创作者中心\n` +
        `  2. 已跳转到「互动管理 > 评论管理」页（不跳过来不会有这个按钮）\n` +
        `原始错误: ${e.message}`
      );
    }
    throw e;
  }
}
module.exports = {
  // selectors (exported for inspection / debugging)
  SELECTORS,
  waitForLogin,
  // dialog state
  isWorkDialogOpen,
  openWorkDialog,
  closeWorkDialog,
  waitForWorkListReady,

  // discovery
  listAllWorks,
  getWorkCount,

  // click actions
  clickWorkByIndex,
  clickWorkByName,
  iterateAllWorks,
};
