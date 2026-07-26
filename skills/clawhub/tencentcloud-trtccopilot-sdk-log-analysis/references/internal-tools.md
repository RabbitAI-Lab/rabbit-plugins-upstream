# 内网查询能力（仅内网员工）

> **加载条件**：仅当 `node scripts/internal-check.js` 返回 `allowed: true`（能解析 `copilot.trtc.woa.com`）时，才读取并使用本文件。
> 外网 / 对外部客户的场景下不要加载本文件，也不要提及这些工具的存在；外部场景只用本地日志分析（见 SKILL.md）。

本文件描述内网才可用的 TRTC Clog / Kibana 主动查询能力。两者都通过 `trtccopilot` CLI 获取数据，鉴权走 CLI token（OA SSO），不使用任何 Base URL / 账号密码。

## 前置：安装并登录 trtccopilot CLI

`@tencent/trtccopilot-cli` 仅腾讯内网源可安装，内置 Clog / Kibana 数据获取接口：

```bash
# 全局安装（推荐，脚本会自动复用 PATH 上的 trtccopilot）
npm i -g @tencent/trtccopilot-cli --registry=https://mirrors.tencent.com/npm

# 授权（OA SSO，默认 30 天 token）
trtccopilot login

# 自检
trtccopilot whoami
```

未全局安装时，脚本会自动回退到 `npx --yes --registry=https://mirrors.tencent.com/npm @tencent/trtccopilot-cli`。

## 数据源选择

| 数据源 | 适用 | 说明 |
|---|---|---|
| Kibana | TRTC Web + Native | 自动采集，适合房间/用户关键事件视角，按 7 天窗口处理；经 CLI 服务端抓取+解析，仅支持 TRTC |
| Clog | TRTC Native | 用户主动上报，单用户完整本地日志；Web 端没有 Clog；经 CLI 查询，仅支持 TRTC |

强规则：

- Web 端不要查 Clog（Web 端没有 Clog）。
- Clog 的 `date` 是上报日期，不等于日志内容发生日期。
- Kibana 查询窗口不要超过 7 天。
- Kibana `--type` 必须传对：同一 case 用错 `type` 会静默返回 0 条（Web case 用 `native` 查会查不到）。
- 查询/搜索后必须读取原文上下文，不能只看摘要下结论。
- 结论必须标明依据来自 `Kibana`、`Clog` 还是本地日志。
- 禁止在对客回复、报告或报错中暴露内部服务地址、临时下载 URL、token、密码、Authorization 等敏感信息。

## 查询 TRTC Clog

> 注意：当前 `trtccopilot` CLI（0.2.0）后端 `/clog/query` 路由异常（返回 HTML 404），此脚本按文档契约实现但尚未端到端验证；待后端修复后即可用。

```bash
node scripts/query-clog.js \
  --sdkappid 1400000001 \
  --userid user_a \
  --date 2026-05-26
```

输出：

- `tmp/sessions/clog-*/records.json`：Clog 查询原始记录。
- `tmp/sessions/clog-*/manifest.json`：下载/解压/解码结果。
- `tmp/sessions/clog-*/clog/.../*.log`：解码后的文本日志。

拿到解码后的 `.log` 后，按 SKILL.md 的本地分析流程跑 `timeline.js`。

## 查询 TRTC Kibana

经 CLI 服务端抓取+解析，无需配置 Kibana 地址或账号密码。`--type` 必须区分 `web` / `native`，传错会查不到日志。

```bash
node scripts/query-kibana.js \
  --sdk-app-id 1400000001 \
  --type native \
  --user-id user_a \
  --start '2026-05-26 10:00:00' \
  --end '2026-05-26 10:30:00'
```

输出：

- `logs.txt`：便于直接读取/搜索。
- `logs.ndjson`：结构化日志。
- `raw-response.json`：CLI 原始响应（含 Kibana 跳转 URL + 解析后日志）。
- `manifest.json`：查询元信息。
