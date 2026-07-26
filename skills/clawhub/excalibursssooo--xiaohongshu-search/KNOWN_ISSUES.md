# Known Issues — xiaohongshu-search

> 隐性 bug、workaround、踩过的坑。**不**丢人,免得新人/未来自己重踩。
> 加新条目请写清楚:复现条件、根因、临时 workaround、是否已修/在哪一版修。

---

## v1.3.x 及更早:`user-search` author 解析 Bug

**复现**:
```bash
xhs-fetch.py user-search "影视飓风官方"
# 输出:user_id = 6a37ddf5000000000d034c01
# 但跑 xhs-harvest.py user 6a37ddf5000000000d034c01 拿到的是 "小红薯6A39354A" 侧栏用户
# 真正想要的 "影视飓风" 是 5c6391880000000012009893
```

**根因**:
search 桶笔记页里 `/user/profile/{uid}` 链接会出现多个:
- author 主页链接(我们要的)   classes: `['avatar-container', 'avatar-click', 'info']`
- 侧栏推荐用户(错的)          classes: `['link-wrapper', 'user side-bar-component', 'popover-trigger']`
- 评论者头像                  href 含 `pc_comment`

旧代码 Stage 3:
```python
.filter(c => {
    if (c.href.includes('pc_comment')) return false;
    if (c.href.includes('side-bar')) return false;   # ❌ href 里没有 'side-bar' 子串!
    if (MY_ID && c.href.includes(MY_ID)) return false;
    return true;
})
user_id = raw[0]['user_id'];   # ❌ 永远取第一个 (可能是侧栏)
```

两个错误叠加:
1. `c.href.includes('side-bar')` 检查的是 href 子串,但侧栏的 href 是干净的 `/user/profile/{uid}`,**没有 'side-bar' 子串** —— 真正的标记在 classes 里
2. 取 `raw[0]` 没考虑 author 特征

外加 `MY_ID` 从 cookie 读 `x-user-id-redlive.xiaohongshu.com`,a1 改版后这个 cookie 不一定下发,导致"排除自己"逻辑静默失效。

**临时 workaround**(v1.3.x):
手动从 candidates 里挑(打印所有 candidates 即可):
```python
# 在 xhs-fetch.py cmd_user_search 末尾加:
print(f"   📋 所有候选 ({len(raw)}):")
for i, c in enumerate(raw, 1):
    print(f"      {i}. user_id={c.get('user_id')}  classes={c.get('classes')}")
```
看 `classes` 包含 `avatar-container` / `avatar-click` 的那个。

**修复**:v1.4.0 — 用 classes 特征过滤 + 打开 user/profile 桶验证 name 匹配 + 失败回退到下一候选。

---

## v1.2.0 起:search 桶 IP 风控 (300012) 后无降级路径

**复现**:
- 短时间内多次跑 `xhs-fetch.py search` / `xhs-harvest.py hot`
- 触发 300012(`IP at risk. Switch to a secure network and retry.`)
- 之后 `user-search` / `user-resolve` 都失败(它们依赖 search 桶拿候选)

**根因**:
- search 桶 captcha 衰减 5-10 min,user 桶 30+ min
- user-search / user-resolve 必须用 search 桶拿 note_id → 笔记页 → author 链接,完全没法绕开
- 300012 触发时,**所有依赖 search 桶的 CLI 都不可用**

**临时 workaround**:
- 等 5-30 min,或换 IP (4G 热点 / 重启路由)
- **手动 fallback**:浏览器登录 xhs → 搜该用户 → 进主页 → URL 末尾 32 位 hex = user_id → `xhs-harvest.py user <uid> --limit 20`

**修复**:v1.4.0 — 新增 `xhs-fetch.py user-resolve` 走"search listing → 逐个验证 candidate user_id → 返回验证通过的",但仍依赖 search 桶,所以本质没变,只是用户拿到的 user_id 不会错。彻底解决需要**实现 search 桶 fallback**,但 xhs 没有"不用 search 桶拿 user_id"的 API,所以**这是一个结构性限制**。

---

## v1.0.0 起:xsec_token 短期失效导致 note 404

**复现**:
```bash
xhs-fetch.py search "影视飓风官方" --limit 5
# 拿到 note_id=69d3683b000000001d token=ABuZEHtacd4V5-9AvIFtwHMU

xhs-fetch.py note 69d3683b000000001d --via-search --token "ABuZEHtacd4V5-9AvIFtwHMU"
# ❌ 该笔记无法浏览 (300031)  或  ✓ 小红书 - 你访问的页面不见了  (404)
```

**根因**:
xsec_token 是 short-lived,search listing 渲染完几秒就过期。xsec_source 也有匹配要求(search 桶的 token 配 `pc_note`,user 桶的配 `pc_user`,错配 300017)。

**临时 workaround**:
- `xhs-harvest.py user <uid> --limit N` —— token 来自用户主页 DOM,**比 search listing 稳定很多**
- 单独抓笔记时,先 `xhs-fetch.py user <uid>` 拿主页,再用主页里 `link_with_token` 配 `xsec_source=pc_user` 走 `--via-user-profile`

**修复**:暂无。已加 README 提示。

---

## 笔记页 DOM 的 likes/collects 不准

**复现**:
某爆款笔记 user.json 里 likes=100000,但笔记页 DOM 显示 1092。

**根因**:
- 笔记页 DOM 拿到的是"**当前会话/最近时间窗**"的点赞(可能 cache,可能截断)
- 主页 note-item 里 like-wrapper 是"**累计**"(更接近真实)
- 极爆款(>10w)经常被截断显示

**临时 workaround**:
以 user.json 的 likes 字段为准。报告里也用 user.json。

**修复**:暂无,这是 xhs 前端数据流的特性。

---

## cookie 风控指纹缺失导致"前 N 个请求正常,后面突然 300012"

**复现**:
- check 通过
- 跑 2-3 个 CLI 突然 300012
- 同一份 cookie 之前能稳定跑 100+

**根因**:
风控指纹 cookie(`webId` / `gid` / `acw_tc` / `websectiga` / `sec_poison_id` / `loadts` / `ets`)缺失或过期。前 1-2 个请求风控还没检测到,后面触发。

**临时 workaround**:
- 浏览器重新登录 xhs → F12 → Application → Cookies → 重新 copy(document.cookie)
- 确认 F12 Network 面板里能看到上述所有 cookie 都有值(不是 None)

**修复**:v1.4.0 — `xhs-keepalive.py check` 会主动扫描风控指纹 cookie,缺则 warn。
```bash
python3 $SKILL/xhs-keepalive.py check
#  ⚠️  风控指纹 cookie 缺: ['webId', 'websectiga']
```

---

## a1 改版后 `x-user-id-redlive.xiaohongshu.com` cookie 不下发

**复现**:
浏览器复制的 cookie 里**没有** `x-user-id-redlive.xiaohongshu.com` 字段。

**根因**:
xhs a1 cookie 改版后,这个 cookie 改名/移除/不再下发了。Stage 3 的"排除自己"逻辑依赖读这个 cookie,读不到 = MY_ID = '' = 排除自己逻辑静默失效。

**临时 workaround**:
- 之前用 cookie 里的 a1 字段直接作 fallback key(`a1` 跟 `x-user-id-redlive.xiaohongshu.com` 不一定对应)
- 或者完全不排除自己(接受"可能拿到自己 user_id"的极小概率)

**修复**:v1.4.0 — 完全不依赖 MY_ID 排除自己,改用 classes 特征(`popover-trigger` / `side-bar-*`)覆盖 99% 场景。
