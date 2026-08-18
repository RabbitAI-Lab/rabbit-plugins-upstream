# 支持平台与 URL 规范 (Supported Platforms)

本文档记录了当前 Skill 支持的主流社交/视频平台的搜索与交互规范。

---

## 1. 抖音 (Douyin)
- **平台代码**: `douyin` / `tiktok`
- **首页**: `https://www.douyin.com/`
- **搜索 URL**: `https://www.douyin.com/search/{encoded_name}?type=user`
- **识别特征**:
  - 用户卡片: `div[data-e2e="search-user-item"]`
  - 关注按钮: `button:has-text("关注")`
  - 已关注状态: `已关注`, `互相关注`
- **注意事项**: 高频检索会触发滑块验证，脚本内置 8~15 秒平滑间隔。

---

## 2. 哔哩哔哩 (Bilibili)
- **平台代码**: `bilibili` / `b站`
- **首页**: `https://www.bilibili.com/`
- **搜索 URL**: `https://search.bilibili.com/upuser?keyword={encoded_name}`
- **识别特征**:
  - 用户卡片: `li.user-item`, `div.user-item`
  - 关注按钮: `button:has-text("关注")`, `button:has-text("+ 关注")`
  - 已关注状态: `已关注`, `已互粉`
- **注意事项**: 需注意未登录时点击关注会弹出登录弹窗。

---

## 3. 小红书 (Xiaohongshu)
- **平台代码**: `xiaohongshu` / `red` / `小红书`
- **首页**: `https://www.xiaohongshu.com/`
- **搜索 URL**: `https://www.xiaohongshu.com/search_result?keyword={encoded_name}&type=user`
- **识别特征**:
  - 用户卡片: `div.user-item`, `div[class*="user-card"]`
  - 关注按钮: `button:has-text("关注")`
  - 已关注状态: `已关注`, `互相关注`
- **注意事项**: 小红书网页版对未登录搜索有频率限制，务必保持登录状态。

---

## 4. X / Twitter
- **平台代码**: `x` / `twitter` / `推特`
- **首页**: `https://x.com/`
- **搜索 URL**: `https://x.com/search?q={encoded_name}&f=user`
- **识别特征**:
  - 用户卡片: `div[data-testid="UserCell"]`
  - 关注按钮: `button[data-testid$="-follow"]`, `button:has-text("Follow")`
  - 已关注状态: `Following`, `已关注`
- **注意事项**: 需具备可用网络环境与已登录状态。

---

## 5. YouTube
- **平台代码**: `youtube` / `油管`
- **首页**: `https://www.youtube.com/`
- **搜索 URL**: `https://www.youtube.com/results?search_query={encoded_name}&sp=EgIQAg%253D%253D`
- **识别特征**:
  - 频道卡片: `ytd-channel-renderer`
  - 订阅按钮: `button:has-text("订阅")`, `button:has-text("Subscribe")`
  - 已订阅状态: `已订阅`, `Subscribed`
