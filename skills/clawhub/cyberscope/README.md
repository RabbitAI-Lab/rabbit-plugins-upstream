# 🔭 CyberScope

可搜索的公开网络攻防/监控/审查方法**参考目录** CLI：10 类目、62 方法、83 条公开来源
（MITRE ATT&CK、CISA、NIST、EFF、OWASP、SANS 等 45 个来源方）。纯参考性描述——
不含操作性/利用步骤。

**零依赖**：Python ≥ 3.8 标准库，离线，确定性。无需 Node、npm、PostgreSQL、网络。

## v2.0.0 相对 v1.0.0

v1.0.0 是 Next.js + PostgreSQL 应用（33 文件）：在 agent 沙箱里无法运行（无 Postgres、
~150MB npm 依赖），且搜索忽略 methods 的 `keywords` 数组、无相关性排序、
`/api/stats` 暴露搜索历史（其 skill-card 自述风险）。v2 把目录与功能机械化为离线 CLI：

| v1 能力/问题 | v2 对应 |
|---|---|
| 应用跑不起来（沙箱无 Postgres） | `data/catalog.json` 唯一数据源 + 标准库 CLI，任何有 python3 的环境零安装 |
| 搜索只匹配 title+description，漏 keywords | `search` 加权评分：title 1000 / keywords 500 / description 200 / resources 100+50 + 短语加分；AND 语义；平局按 id 升序 |
| 无排序（恒按编号） | score 降序（`ransomware` → m50 2450 分第一，而非编号序） |
| 搜索历史入库 + stats 暴露（隐私风险） | 无状态、无历史、无网络 |
| 无离线数据验证 | `checksums`（文件 sha + 规范内容 sha 锚点）· `verify-sources`（83 URL 静态检查，9 个已知 WARN 基线） |
| `indexed_content` 死表、无自测 | `catalog-report`（43 个单源方法、1 个重复 URL、2 个 ATT&CK 斜杠格式 → 可执行建议）· `selftest.py` 10 组 |
| 33 文件 ~27KB 应用代码 | 9 文件：文档 5 + 脚本 2 + 数据 1 + （README 不计入树哈希） |

v1 应用代码保留在 ClawHub 版本历史（v1.0.0）中供需要 Web UI 者取用；
v2 数据与 v1 `src/lib/seed-data.ts` 字节语义一致（规范摘要锚点见 `references/catalog_schema.md`）。

## 用法

```bash
python3 scripts/cyberscope.py search "living off the land"        # 加权搜索
python3 scripts/cyberscope.py search ddos --fields all            # 带描述+资源
python3 scripts/cyberscope.py categories                          # 10 类目+计数
python3 scripts/cyberscope.py method 27                           # 单条完整记录
python3 scripts/cyberscope.py export --format md --out /tmp/out   # json|csv|md 确定性导出
python3 scripts/cyberscope.py checksums                           # 数据保真锚点
python3 scripts/cyberscope.py verify-sources                      # 83 URL 静态检查
python3 scripts/cyberscope.py catalog-report                      # 质量报告+改进建议
python3 scripts/selftest.py                                       # 全部自检（应 100% PASS）
```

**退出码**：`0` ok · `2` 输入错误（stderr 单行 JSON）· `3` 结构性数据违规。
**stdout** 恒为单行 JSON（数据）；**stderr** 仅错误 JSON。

## 诚实使用规则

1. **参考性**：目录描述已公开记录的技术（与 MITRE ATT&CK 同类），不是操作指南。
2. **合法用途**：仅限研究、教育、新闻、威胁建模与防御，且只针对你有权研究的系统/情境。
3. **不得武器化**：不得从条目推导/添加可执行的攻击步骤。
4. **引用而不放大**：写作时链接 `resources[].url` 公开来源。

## 文件

```
SKILL.md                    # 加载地图 + 命令契约 + 硬规则 + 边界
README.md                   # 本文件
CHANGELOG.md                # 版本记录
data/catalog.json           # 唯一数据源（10/62/83，schema_version 2）
scripts/cyberscope.py       # 全部命令（纯标准库）
scripts/selftest.py         # 10 组离线自检
references/
  catalog_schema.md         # 数据模型 + 保真锚点
  search_scoring.md         # 评分算法全定义
  source_verification.md    # 静态验证语义与边界
```

## 验证

- TREE-SHA256-v1（发布包 8 个文件，排除 README.md 以破 hash-in-file 循环）：
  `a3c6a9d2efc402a35632a9b08744a87ae4b25d0d661707802c295a477b1b090e`（重算方式同仓库其它 skill；README 只记录值。）
- 数据保真：`python3 scripts/cyberscope.py checksums` 的
  `methods_canon_sha256` / `resources_canon_sha256` 应与 `references/catalog_schema.md` 锚点一致。
