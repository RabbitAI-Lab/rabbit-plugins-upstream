---
name: pansou
description: 网盘资源搜索。当用户想找影视剧、动漫、软件、资料的观看/下载链接时用。直接说片名也触发（如韩国制造），观看意图也触发（看、想看、我要看、找、搜、求链接、哪里能看、求资源、推荐个好看的），片名+网盘也触发（如韩国制造 夸克）。支持多个 PanSou 站点并发搜索，谁先有数据先给用户。模糊兴趣（如听说某剧好看）先问是不是想找来看再搜。
metadata:
  openclaw:
    requires:
      bins:
        - go
      env:
        - PANSOU_URL
        - PANSOU_URLS
---

## 何时使用（意图 -> 动作）

用户很少说“搜索网盘”“找资源”，都是直接提需求。看到以下意图直接用本技能，不用等明确触发词：

- 直接说片名/资源名：如韩国制造、韩国制作
- 观看意图词：看、想看、我要看、找、搜、求链接、哪里能看、有资源吗、求资源、链接发我、搜索、推荐个好看的
- 组合句：我要看韩国制造、帮我找韩国制造、韩国制造哪里能看、听说韩国制造好看、求韩国制造链接、搜索韩国制造
- 片名 + 网盘限定：如韩国制造 夸克 -> 去掉网盘词，用 `--cloud-types quark` 再搜
- 网盘别名：夸克=quark、百度=baidu、阿里=aliyun、天翼=tianyi、UC=uc、移动=mobile、115=115、迅雷=xunlei、123=123、磁力=magnet、电驴=ed2k
- 模糊兴趣：如“听说XX剧好看”“最近有啥好看的” -> 先问一句“是不是想找XX来看？偏好哪个网盘（夸克/百度/阿里）？”确认后再搜

只聊剧情、评价、演员、不找链接时不用本技能。

## 首次使用引导

用户第一次安装、环境变量缺失，或直接问“怎么用/怎么配置”时，按以下步骤一步步引导，确认一步再走下一步：

1. 先确认是否已有 `PANSOU_URL` / `PANSOU_URLS`。当前会话可能没继承用户级变量，先问用户是否保存过。
2. 没有就向用户要至少 1 个自建 PanSou 服务地址（形如 `http://ip:port`）。用户没有地址时，先让他自己部署或拿到地址，不要编造。
3. 引导保存地址。Windows 用户永久保存：
   `[Environment]::SetEnvironmentVariable("PANSOU_URLS","http://a,http://b","User")`
   macOS/Linux 用户在 `~/.zshrc` / `~/.bashrc` 加：`export PANSOU_URLS="http://a,http://b"`
   单站点用 `PANSOU_URL`，多站点用 `PANSOU_URLS`。
4. 本会话想立即测试，可先用临时变量：`$env:PANSOU_URLS="http://a,http://b"`（仅当前窗口有效）。
5. 先在 `scripts` 目录编译 `go build -o pansou .`（自动适配当前平台），然后跑健康检查：Windows `pansou.exe health`，Linux/macOS `./pansou health`，全部 ok 再进行下一步。
6. 让用户发一个想看的内容，实跑一次搜索，确认能正常出 Markdown 链接才算完成引导。

注意：不要一次性丢一大段文档，引导过程中一次推进一步即可。

## 多站点并发

- 配置一个站点：`PANSOU_URL=https://pansou.example.com`
- 配置多个站点：`PANSOU_URLS=https://a.example.com,https://b.example.com`，优先于 `PANSOU_URL`
- `--strategy first`（默认）：所有站点并发搜索，谁先返回有效数据就先给用户，返回结果带 `_site` 标记来源
- `--strategy merge`：所有站点并发搜索，等全部返回后按站点合并，输出 `{"strategy":"merge","sites":{...}}`
- 多站点时 token 按 host 分开存在 `~/.config/pansou/tokens/`；某个站点失败不会卡死其他站点

```bash
# 多站点并发，先到先展示
{baseDir}/scripts/pansou.exe search "韩国制造" --strategy first

# 多站点并发，等全部返回后合并
{baseDir}/scripts/pansou.exe search "韩国制造" --strategy merge

# 多站点并发健康检查
{baseDir}/scripts/pansou.exe health
```

## 网址健康度提醒

- `search` 搜索时会并发探测所有站点的 `/api/health`（和搜索同时跑，不额外阻塞）。失联地址超过 3 个时，会打印警告并列出失联地址，提醒用户更新 `PANSOU_URLS`。
- 想单独查看各站点状态：`{baseDir}/scripts/pansou.exe health`。
- 收到“超过 3 个失联”的警告时，先让用户更新或移除失效地址，再继续搜索，避免拿到空结果。

## 使用

调用前确认 `PANSOU_URL` 或 `PANSOU_URLS` 已配置。部署详见 [PanSou GitHub](https://github.com/fish2018/pansou)。

本技能附带 Go 源码，零依赖，不打包预编译二进制。首次使用（或换机器后）先在 `scripts` 目录编译：Windows 运行 `go build -o pansou.exe .`（必须带 .exe，否则 PowerShell 拒绝运行），Linux/macOS 运行 `go build -o pansou .` 再 `chmod +x pansou`。下面的命令里的 `pansou.exe` 在 Linux/macOS 上换成 `./pansou`。

```bash
# 健康检查（无需认证）
{baseDir}/scripts/pansou.exe health

# 验证 token 是否有效，无效自动重新登录（单站点）
{baseDir}/scripts/pansou.exe verify

# 搜索（自动处理认证）
{baseDir}/scripts/pansou.exe search "关键词"

# 指定网盘类型
{baseDir}/scripts/pansou.exe search "关键词" --cloud-types quark,aliyun,baidu

# 指定插件
{baseDir}/scripts/pansou.exe search "关键词" --plugins labi,zhizhen,shandian

# 指定TG频道
{baseDir}/scripts/pansou.exe search "关键词" --channels tgsearchers3

# 过滤结果
{baseDir}/scripts/pansou.exe search "觉醒年代" --include 合集,全集 --exclude 预告,花絮

# 仅TG / 仅插件
{baseDir}/scripts/pansou.exe search "关键词" --src tg
{baseDir}/scripts/pansou.exe search "关键词" --src plugin

# 强制刷新缓存
{baseDir}/scripts/pansou.exe search "关键词" --refresh

# 使用 GET 方式搜索
{baseDir}/scripts/pansou.exe search "关键词" --get
```

单站点 token 自动存储在 `~/.config/pansou/token.json`，多站点按 host 存到 `~/.config/pansou/tokens/`，过期自动重新登录。

## 意图解析示例

- “韩国制造” -> `search "韩国制造"`
- “我要看韩国制造”/“想看韩国制造”/“看韩国制造” -> `search "韩国制造"`
- “韩国制造 夸克” -> `search "韩国制造" --cloud-types quark`
- 配置了多个站点时，默认并发查所有站点，谁先有结果先展示

## 安全说明

- `PANSOU_URL` / `PANSOU_URLS` 由用户自行部署或指定，脚本仅向这些地址发起 HTTP 请求
- `PANSOU_USER` / `PANSOU_PWD` 仅在服务返回 401 时用于获取 JWT token
- Token 仅通过 HTTP POST 发送至用户指定的站点，不会外泄
- 认证为可选：未启用认证的服务无需设置 `PANSOU_USER` / `PANSOU_PWD`

## 支持的网盘类型

简要列表：`baidu` `aliyun` `quark` `tianyi` `uc` `mobile` `115` `pikpak` `xunlei` `123` `magnet` `ed2k` `others`

完整清单（含各类型对应的插件和说明）见 [references/cloud-types.md](references/cloud-types.md)。

## 搜索参数详解

所有 CLI 参数（`--res`、`--conc`、`--refresh`、`--strategy` 等）详细说明见 [references/api-params.md](references/api-params.md)。

## 搜索结果格式

默认 `merge` 模式，按网盘类型分类返回：

```json
{
  "total": 15,
  "merged_by_type": {
    "quark": [
      {"url": "https://pan.quark.cn/s/abcdefgxxxx", "password": "", "note": "标题", "datetime": "...", "source": "plugin:labi"}
    ]
  }
}
```

如需原始消息列表，使用 `--res results`。多站点 `first` 模式的结果会带 `_site` 字段标明来自哪个站点。

## 输出格式注意事项

### 链接展示格式
向用户展示搜索结果中的链接时，**必须使用 Markdown URL 形式**，不要用代码块包裹：

正确示例：
```
1. 更新至20集 4K HDR
https://pan.quark.cn/s/abcdefgxxxx
```

错误示例：
```
1. 更新至20集 4K HDR
`https://pan.quark.cn/s/abcdefgxxxx`
```

原因：代码块形式的链接无法直接点击，用户体验差。Markdown URL 可以直接点击打开。
