---
name: xiaohongshu-search
description: 小红书内容抓取(搜索/读笔记/看用户)。统一走 agent-browser(官方 JS 环境 + X-s 签名自动处理)。需注入登录 cookie。
version: 1.4.1
emoji: "📕"
homepage: https://github.com/excalibursssooo/xiaohongshu-search
metadata:
  openclaw:
    requires:
      bins: [python3, agent-browser]
    envVars:
      - {name: XHS_COOKIE_FILE, required: false, description: "覆盖 cookie 路径"}
      - {name: XHS_DATA_DIR,    required: false, description: "覆盖整个 data/ 目录(给 docker/CI 用)"}
    primaryEnv: XHS_COOKIE_FILE
changelog:
  - v1.4.1: 抽 common.py 消重复 (err/ok/author_matches/strip_author_suffix/safe_int); fetch 错误用结构化输出 [ERR] error_code=XXX,msg=YYY; harvest 解析 error_code 走对应分支; harvest --from-name 优先 user-resolve,fallback user-search
  - v1.4.0: P0 修复 user-search author 解析 (classes 特征过滤 + user/profile 桶验证 + 失败回退); 新增 user-resolve (Plan B 降级,逐个验证); 新增 --list-candidates 调试; harvest user 加 author 验证; cookie check 加风控指纹检查; troubleshooting 章节
  - v1.3.1: 修复 frontmatter YAML 引号缺失 (XHS_DATA_DIR description 漏 ",导致 YAML 解析失败)
  - v1.3.0: captcha / IP 风控 一律不重试,直接报错(避免脚本自我加锁)
  - v1.2.0: 🎯 走 via-user-profile 路径完全绕开 search 桶 captcha
  - v1.1.0: 一条命令抓取特定用户视频
  - v1.0.0: 初版
---

# xiaohongshu-search

> **⚠️ cookie 必填**。关键字段:`a1`(长效) + `web_session`(6-12h 短效) + `id_token` + `webId/gid/acw_tc/websectiga/sec_poison_id/loadts/ets`(风控指纹)。

## ⚡ 30 秒上手

```bash
export SKILL=/path/to/xiaohongshu

python3 $SKILL/xhs-keepalive.py check                             # cookie 验证

# 🎯 抓特定用户的视频(⭐ 推荐 — 完全绕开 search captcha)
python3 $SKILL/xhs-harvest.py user <user_id> --limit 15 --comments 15
python3 $SKILL/xhs-harvest.py user 5c6391880000000012009893 --limit 15

# 🆘 不知道 user_id? 用 --from-name (走 search 桶,被 captcha 时会失败)
python3 $SKILL/xhs-harvest.py user --from-name "影视飓风" --limit 15 --comments 15

# 🔍 查 user_id 但拿不准哪个是 author
python3 $SKILL/xhs-fetch.py user-search "影视飓风" --list-candidates  # 看完整候选
python3 $SKILL/xhs-fetch.py user-resolve "影视飓风"                   # 逐个验证 (Plan B)

# 抓一个主题的热门笔记(必须 search 桶,被 captcha 时会失败)
python3 $SKILL/xhs-harvest.py hot "AI" --limit 10 --comments 10

# 已知 note_id 批量抓
python3 $SKILL/xhs-harvest.py ids id1 id2 id3 --tokens "t1,t2,t3"
```

`xhs-harvest.py` 编排工作流,`xhs-fetch.py` 原子操作。落盘: `$SKILL/data/harvests/<topic>-<ts>/REPORT.md`。

#fetch_pydiff

```bash
xhs-harvest.py user <user_id> --limit 15 --comments 15
```

**为什么是推荐路径**:
- ✅ **完全不走 search 桶** → search captcha 触发也不影响
- ✅ 主页 DOM 里 `note-item` 自带 `xsec_token + xsec_source=pc_user` → 30/30 命中
- ✅ 一条命令,内部完成: 主页拿 30 篇 → DOM 拿 token → 逐条走 `/user/profile/{uid}/{nid}?...&xsec_source=pc_user` 抓详情 → 报告

### 内部流程

```
Step 1  xhs-fetch.py user <user_id> --notes 50  →  user.json
        ↓ DOM 解析 note-item 里的 <a href>, 拿 (note_id, xsec_token, xsec_source=pc_user)
Step 2  对每条 note, 走 via-user-profile 抓详情
        URL: /user/profile/{uid}/{nid}?xsec_token=...&xsec_source=pc_user
        ↓ 完全在 user/profile 桶, 不碰 search 桶
Step 3  落盘 + 写 REPORT.md
```

### 落盘结构

```
$SKILL/data/harvests/user-<uid前12位>-<时间戳>/
├── REPORT.md          ← 人类可读报告
├── user.json          ← 主页元数据 + 笔记列表 (带 xsec_token)
└── notes/
    ├── n01-*.json     ← 笔记详情 + 评论
    └── ...
```

### 不知道 user_id? 备选 `--from-name`

```bash
xhs-harvest.py user --from-name "小Lin说" --limit 15
```

**限制**: 内部调 `xhs-fetch.py user-search`,会走 **search 桶**。search 桶 IP captcha 触发时此命令会失败(报"未找到匹配")。

**故障时切换**:
```bash
# 浏览器登录 xhs → 搜索 → 进主页 → URL 末尾 32 位 hex = user_id
# 例: xhs.com/user/profile/5c6391880000000012009893
xhs-harvest.py user 5c6391880000000012009893 --limit 15        # 直接走 user/profile 桶
```

---

## 🛡️ IP-bound captcha 完全解决

xhs captcha **按 URL 路径分桶,各桶独立计数**:

| 桶 | 路径 | 衰减 | 状态 |
|---|---|---|---|
| 桶 1 | `/search_result?keyword=...` (search listing) | 5-10 min | ❌ 频繁锁 |
| 桶 2 | `/search_result/{nid}?xsec_token=...&xsec_source=pc_note` | 5-10 min | ❌ 300017 |
| 桶 3 | `/user/profile/{uid}` (用户主页) | 30+ min | ⚠️ 触发频率低 |
| **桶 4** | **`/user/profile/{uid}/{nid}?xsec_token=...&xsec_source=pc_user`** | **30+ min** | **✅ 推荐路径** |

### 🎯 黄金法则:**永远走桶 4**(via-user-profile)

```bash
xhs-harvest.py user <user_id> --limit 15 --comments 15
```

这条命令**完全不碰 search 桶**,即使 search 桶被锁也照常工作。

### ⛔ 不要走(会被 captcha 拦)

| 命令 | 失败原因 |
|---|---|
| `xhs-fetch.py note <id> --via-search` (用主页 token) | 30017 url invalid — token + xsec_source 不匹配 |
| `xhs-fetch.py search "..."` (search listing) | 桶 1 captcha |
| `xhs-harvest.py user --from-name "..."` (search 桶被锁时) | 找不到匹配的 user_id |
| `xhs-harvest.py hot "..."` (search 桶被锁时) | 拿不到候选 |

### 🚨 重要:captcha / IP 风控 **一律不重试**

**v1.3.0 行为变更**:遇到 captcha 或 300012 IP 风控,脚本**直接报错退出**,不自动 sleep + 重试。

**为什么**: 之前自动重试反而把 captcha 锁得更死(IP 持续被标记)。现在:
- 遇到 captcha → 立即报错,告诉你"等 5-30 min 或换 IP 后重跑"
- **不**消耗额外请求
- **不**让 captcha 加锁
- **不**让用户等 N 分钟看脚本自己重试

用户决定要不要重跑,什么时候重跑,要不要换 IP。

### captcha / IP 风控的解决

| 方式 | 操作 | 效果 |
|---|---|---|
| 4G 热点 | 手机开热点,PC 连 | 立即换 IP,所有桶清空 |
| 重启路由 | 断电重启 | 重新分配 IP(看 ISP) |
| 代理池 | 脚本支持 http_proxy 环境变量 | 批量抓推荐 |
| 等衰减 | 5-30 分钟 | search 桶 5-10 min,user 桶 30+ min |

---

## 🪤 7 个常见坑

| # | 坑 | 怎么避 |
|---|---|---|
| 1 | `user-search "影视飓风"` 抓到 @GOODLUCK | 用官方/唯一名(影视飓风**官方**);Stage 1.5 自动验证 author |
| 2 | 主页 link 没 xsec_token | 不会发生,30/30 都有,parse_user_note_link 拿 |
| 3 | `/explore/{id}` 直接访问 300031 | 必须带 xsec_token 走 via-user-profile 或 via-search |
| 4 | `write_report` KeyError 崩 | 已修,全用 .get() |
| 5 | search 路径的 author 字段带后缀 `"name2天前"` | `strip_author_suffix()` 处理 |
| 6 | search 关键词太泛搜不到目标笔记 | 用全标题或前 15 字;长尾/低曝光笔记可能搜不到 |
| 7 | 笔记页 DOM 的 `likes/collects` 不准 | **累计点赞以 user.json 的 `likes` 字段为准** |
| 8 | `user-search` 拿到侧栏用户的 user_id(classes 含 `side-bar` / `popover-trigger`) | v1.4.0+ 已修(用 classes 特征过滤 author + 验证 user/profile 桶 name)。调试:加 `--list-candidates` |

---

## ⚠️ ab 直接调用的限速铁律

| 场景 | 间隔 |
|---|---|
| `ab_open` → `ab_open`(不同页面) | **必须 sleep ≥ 3s**(脚本默认 4s) |
| `ab_eval` → `ab_open`(页面切换) | sleep ≥ 2s |
| `ab_eval` → `ab_eval`(同一页面) | 不需 sleep |
| 连续多次 `ab_open`(调试) | **必中 300012** |

**黄金法则**:能交给脚本的事,绝不要用 `ab` 手动打。

---

## 决策规则(报错时查这个)

| 错误 | 含义 | 动作 |
|---|---|---|
| **300012** | IP 风控(与 cookie 无关) | **不重试**,换网络/IP |
| **300011** | 账号异常 / cookie 失效 | 重导 cookie → inject → check |
| **300017** | `url is invalid` | xsec_token + xsec_source 不匹配;改用 via-user-profile |
| **300031** | 笔记不可见 | 走 via-user-profile 或 via-search |
| `Security Verification`(search 路径) | search 桶 captcha | **不重试**,等 5-10 min 或换 IP |
| `Security Verification`(user/profile 路径) | user 桶 captcha | **不重试**,等 30+ min 或换 IP |

**经验法则**:300012 → 换网络;300011 → 换 cookie;浏览器卡死 → `agent-browser close --all && sleep 2` 万能解。

---

## 首次 setup(用户手动,一次性)

```bash
# 1. 浏览器登录 xiaohongshu.com → F12 → Application → Cookies → www.xiaohongshu.com
# 2. Console 跑 copy(document.cookie),粘到文件:
cat > $SKILL/data/cookies-raw.txt <<'EOF'
a1=xxx; web_session=xxx; id_token=xxx; ...
EOF
chmod 600 $SKILL/data/cookies-raw.txt

# 3. 转 Netscape + 验证
python3 $SKILL/xhs-keepalive.py inject    # → $SKILL/data/cookies.txt
python3 $SKILL/xhs-keepalive.py check     # exit 0=有效
```

`web_session` 6-12h 短效,过期报 300011 → 重导 cookies。

---

## 🆘 故障排查 (troubleshooting)

### Q1:`user-search` 拿到的 user_id 在 user/profile 桶打开后不是同一个用户(例: "小红薯6A39354A")

**原因**:search 桶笔记页里会有多个 `/user/profile/{uid}` 链接,其中第一个可能是**侧栏推荐用户**(classes 含 `side-bar` / `popover-trigger`),不是笔记 author。旧版直接取了 raw[0] 拿到错的 uid。

**P0 修复**(v1.4.0+):用 classes 特征过滤 author,取 `avatar-container` / `avatar-click` / `info` / `author` 特征的候选,并打开 user/profile 桶验证 name 匹配。

**手动排查**:
```bash
xhs-fetch.py user-search "影视飓风" --list-candidates
# 输出所有候选 + classes,一眼看出哪个是 author:
#  1. ❌ 排除  user_id=6a37ddf5000000000d034c01  classes=['link-wrapper', 'user side-bar-component', 'popover-trigger']
#  2. ✅ author user_id=5c6391880000000012009893  classes=['avatar-container', 'avatar-click', 'info']
```

**Plan B 降级**(逐个验证):
```bash
xhs-fetch.py user-resolve "影视飓风"
# 内部: search listing → candidates → 逐个打开 user/profile 桶验证 name 匹配 → 返回验证通过的
```

### Q2:harvest user --from-name "X" 抓出 0 作品 / 抓了别人

同 Q1 根因。但 harvest user 会在 Phase 1 拿主页后**验证 author name 跟 keyword 匹配**,不匹配会直接报错退出(并提示跑 `--list-candidates`)。

### Q3:search 桶 IP 风控 (300012) 后所有 user-search 失败

**原因**:user-search / user-resolve 都依赖 search 桶拿候选笔记。

**P0 修复**:
- `xhs-fetch.py user` 不依赖 search 桶,**可继续工作**(只要 user_id 已知)
- `xhs-fetch.py user-resolve` 是 Plan B,但仍需 search 桶(无法在 search 桶被锁时工作)
- search 桶衰减 5-10 min / user 桶衰减 30+ min

**手动 fallback**(search 桶锁了,user-resolve 也不能用时):
1. 浏览器登录 xhs → 搜该用户 → 进主页
2. URL 末尾 32 位 hex = user_id
3. `xhs-harvest.py user <user_id> --limit 20 --comments 15`

### Q4:Cookie check 看似正常,但后续请求突然 300012

**原因**:风控指纹 cookie (`webId` / `gid` / `acw_tc` / `websectiga` / `sec_poison_id` / `loadts` / `ets`) 缺失,前 1-2 个请求正常,后面触发风控。

**P0 修复**:`xhs-keepalive.py check` 现在会主动扫描这些 cookie,缺则 warn。
```bash
python3 $SKILL/xhs-keepalive.py check
#  ⚠️  风控指纹 cookie 缺: ['webId', 'websectiga']
#     现象: 前 1-2 个请求看似正常,后面突然 300012
#     解决: 浏览器重新登录 xhs → F12 → Application → Cookies → 重新 copy(document.cookie)
#           确保 F12 Network 面板里能看到上述所有 cookie 都有值
```

### Q5:search listing 拿的 note_id + token 打开 404

**原因**:xsec_token 是 short-lived(search listing 几秒后过期),或 xsec_source 不匹配。

**修复**:用 `xhs-harvest.py user <uid> --limit N` 走 via-user-profile 桶,token 来自主页 DOM 自身,比 search listing 稳定。

### Q6:user.json 里的 likes 跟笔记页 DOM 的 likes 差很多

**已知问题**:笔记页 DOM 的 likes/collects 经常滞后或不显示(尤其是爆款),user.json 里的 likes 才是"用户主页累计点赞"(以 .note-item 里的 like-wrapper 字段为准)。

---

## 边界

- 小红书抓数据 → 本 skill
- 写操作(点赞/评论/关注)/ 其他网站 → agent-browser skill
