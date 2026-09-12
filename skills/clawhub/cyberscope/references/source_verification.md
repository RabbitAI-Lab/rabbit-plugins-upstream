# 来源静态验证的语义与边界（供参考 · 定性）

> 实现：`cyberscope.py` `check_url()`；命令 `verify-sources`；自检 G6 锚定 9 个已知 WARN。

## 检查项（纯静态、不联网）

| 代码 | 级别 | 判据 |
|---|---|---|
| `SCHEME` | ERR | 非 `https://` 开头 |
| `HOST_EMPTY` | ERR | 无主机名 |
| `HOST_CHAR` | ERR | 主机名含空白/非 ASCII |
| `PORT` | WARN | 显式端口（https 默认 443） |
| `NULL_ENCODED` | WARN | 含 `%00` |
| `DOUBLE_SLASH` | WARN | 路径含连续 `//` |
| `BACKSLASH` | WARN | 含反斜杠 |
| `COMMERCIAL_DOMAIN` | WARN | 商业域名来源（信息性；allowlist 按裸主机名匹配，`www.` 前缀不算不同域） |
| `ATTACK_SLASH_FORMAT` | WARN | ATT&CK 子技术 URL 用 `T1234/005` 斜杠（规范为 `T1234.005` 点号） |

域分类：机构 allowlist（attack.mitre.org、cisa.gov、nist.gov/csrc.nist.gov、eff.org、
owasp.org、sans.org、torproject.org…）∪ TLD 启发式（.gov/.edu/.ac./.int → institution；
.org → org；.com/.net/.io/.dev/.ca → commercial）。

## 退出码

- `0`：无 ERR（可以有 WARN——WARN 是数据画像，不是违规）。
- `2`：输入错误（catalog 缺失等）。
- `3`：存在 ERR（结构性数据违规）。

## 证明了什么 / 没证明什么（输出 `limits` 字段自带此声明）

**证明**：URL 可解析、scheme/主机/路径格式合法、域名类别画像、ATT&CK URL 格式合规性。
**不证明**：链接存活（不探测 HTTP）、内容正确、证书有效、来源仍覆盖所述主题。
沙箱常离线，故刻意不联网；需要存活确认时由使用者自行打开 URL。

## 当前数据画像（v2.0.0 基线，自检锚定）

- 0 ERR；9 WARN = 7 × COMMERCIAL_DOMAIN（m9 m20 m24 m25 m36 m45 m46：
  KnowBe4、CrowdStrike、Recorded Future、Cloudflare Radar、Top10VPN×2、Comparitech）
  + 2 × ATTACK_SLASH_FORMAT（m30 `T1584/002`、m48 `T1195/002`）。
- 改进入口：`catalog-report` 的 `recommendations`（`fix_attack_url_format` /
  `dedupe_or_keep` / `add_source`）。
