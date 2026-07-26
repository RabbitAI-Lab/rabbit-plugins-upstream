// selectors.js — 抖音创作者中心评论管理页面的所有选择器，集中管理。
//
// ╔═══════════════════════════════════════════════════════════════════╗
// ║ 稳定性报告（已通过 audit.js / audit2.js 现场验证）               ║
// ╠═══════════════════════════════════════════════════════════════════╣
// ║                                                                   ║
// ║  所有选择器都是 class-prefix 子串匹配。                          ║
// ║  "前缀"（prefix）是抖音前端开发在源码里写死的语义词；           ║
// ║  "后缀"（HASH）由 styled-components 自动生成，每次构建都会变。   ║
// ║                                                                   ║
// ║  页面没有 data-* / aria-label / role="comment" / name= 属性      ║
// ║  （已通过 probe_selectors.js 验证）。所以"语义前缀"是           ║
// ║  目前能找到的最稳定锚点。                                       ║
// ║                                                                   ║
// ║  全局计数（截至 audit 验证时）：                                 ║
// ║    [class*="comment-content-text-"]  -> 9   (3 顶级 + 6 回复)   ║
// ║    [class*="username-"]              -> 9                          ║
// ║    [class*="time-"]                  -> 9                          ║
// ║    [class*="reply-list-"]            -> 2   (只有 2 条评论有)    ║
// ║    [class*="load-more-"]             -> 2   (当前全是"收起")     ║
// ║    [class*="loading-"]               -> 1                          ║
// ║                                                                   ║
// ║  失效模式：                                                     ║
// ║    - 抖音改了源码里的语义词（如 username → nickname），全坏。    ║
// ║      截至目前还没发生过。                                        ║
// ║    - 抖音改了 DOM 结构（如 username 移出 comment card），         ║
// ║      walk-up 算法失效，parseAllInPage 返回 0 条顶级评论。        ║
// ║    - 抖音更新后，先跑 example.js 验证一遍。                     ║
// ║                                                                   ║
// ╚═══════════════════════════════════════════════════════════════════╝

module.exports = {
  // ── 评论单元的"语义锚点"（className 前缀） ──
  COMMENT_TEXT:  '[class*="comment-content-text-"]',  // 评论/回复的文本节点
  USERNAME:      '[class*="username-"]',               // 用户名（内部可能含"作者"徽章）
  TIME:          '[class*="time-"]',                   // 发布时间
  REPLY_LIST:    '[class*="reply-list-"]',             // 一级评论下的二级回复容器
  LOAD_MORE:     '[class*="load-more-"]',              // "查看 X 条回复" / "收起" 按钮
  LOADING:       '[class*="loading-"]',                // "没有更多评论" 标记（需用文本过滤）

  // ── 头像包裹元素（双段 className，"avatar-XXX" 是后段） ──
  AVATAR_WRAP:   '[class*="douyin-creator-interactive-avatar"]',
};
