# Infoseek 合规审计报告（v2.2.0）

> 生成：2026-09-21T02:22:29+00:00 ｜ 根目录：`/root/.skills/infoseek` ｜ 总判定：**pass**

本报告由 `scripts/compliance_audit.py`（D-8 / P3-9 合规审计自动化）生成，四链均**只读复用**既有真源模块，不重复实现口径、不发网络请求。

## 一、总览

| 链路 | 真源模块 | 判定 | 要点 |
|---|---|---|---|
| ① 凭证审计 | scripts/leak_scan.py + core/key_manager.py | pass | 扫描 231 文件；可处置 0 / 白名单 8；key 记录 0 |
| ② 抓取合规 | core/capability_registry.py + consent.log | pass | 能力 12 项；需授权 5；运行时已授权 0 |
| ③ 网络边界 | scripts/boundary_gate.py（静态声明校验） | pass | 校验 12 能力；不通过 0；分布 {'open': 5, 'local': 4, 'sandbox_restricted': 3} |
| ④ 版权来源 | references/trusted-sources.json | pass | v2.0.0；white_list 85；kb_sources 29 |


## 二、① 凭证审计链

- 扫描器：`scripts/leak_scan.py`（可用=True，字面量模式 9 条，白名单 13 项）
- 扫描结果：231 文件 / 命中 8；分级 {'placeholder': 3, 'test_fixture': 5}
- 可处置项：**0**

| 文件 | 行 | 模式 | 分级 | 值 |
|---|---|---|---|---|
| scripts/infoseek_auth.py | 174 | OpenAI/通用 sk- key | placeholder | sk-*** |
| scripts/infoseek_auth.py | 175 | OpenAI/通用 sk- key | placeholder | sk-*** |
| scripts/infoseek_auth.py | 176 | OpenAI/通用 sk- key | placeholder | sk-*** |
| tests/test_async_tools.py | 8 | OpenAI/通用 sk- key | test_fixture | sk-*** |
| tests/test_async_tools.py | 9 | OpenAI/通用 sk- key | test_fixture | sk-*** |
| tests/test_key_manager_v101.py | 57 | OpenAI/通用 sk- key | test_fixture | sk-*** |
| tests/test_key_manager_v101.py | 59 | OpenAI/通用 sk- key | test_fixture | sk-*** |
| tests/test_key_manager_v101.py | 128 | OpenAI/通用 sk- key | test_fixture | sk-*** |


- KeyManager 状态（脱敏指纹）：

| 项 | 值 |
|---|---|
| 可用 | True |
| providers | 0 |
| 记录数 | 0 |
| 状态分布 | {} |
| 熔断中 | [] |
| 阈值 | {'fail': 3, 'circuit': 5, 'cooldown_s': 60.0} |


## 三、② 抓取合规链

- 注册表：`capabilities/registry.yaml`（12 项，声明启用 2，有效启用 2）
- 需授权：['Maigret', 'Sherlock', 'AccountTrustScorer', 'AgentKey', 'FakeDetect']
- 运行时已授权：[]
- 未授权（默认关闭）：['Maigret', 'Sherlock', 'AccountTrustScorer', 'AgentKey', 'FakeDetect']
- 声明冲突（启用∧需授权）：[]
- consent 台账：path=`/root/.infoseek/consent.log` 存在=True grant=86 revoke=71 格式异常=0

| 能力 | 类别 | 声明启用 | 需授权 | 已授权 | 有效启用 | 网络边界 |
|---|---|---|---|---|---|---|
| QVeris | structured_data_api | True | False | None | True | open |
| Maigret | identity_attribution | False | True | False | False | open |
| Sherlock | identity_attribution | False | True | False | False | open |
| AccountTrustScorer | identity_attribution | False | True | False | False | local |
| PublicApisCatalog | free_api | False | False | None | False | local |
| AgentKey | gateway_api | False | True | False | False | open |
| L2Renderer | browser_engine | False | False | None | False | open |
| FakeDetect | account_forensics | False | True | False | False | local |
| WikiVerify | knowledge_verify | False | False | None | False | sandbox_restricted |
| L4Transcribe | multimedia_transcribe | False | False | None | False | sandbox_restricted |
| PatentLookup | patent_lookup | False | False | None | False | sandbox_restricted |
| manual_review | graceful_fallback | True | False | None | True | local |


## 四、③ 网络边界链

- 模式：**static_only**（probe=False）—— 只校验能力声明的边界/要求主机，不探测可达性（零网络）
- 校验结果：12 项 / 通过 12 / 不通过 0
- 边界分布：{'open': 5, 'local': 4, 'sandbox_restricted': 3}；合法值 ['open', 'sandbox_restricted', 'local']
- 不通过明细：{}
- 边界报告产物：`references/network-boundary-report.md`（存在=True，3359 字节）

## 五、④ 版权来源链

- 台账：`references/trusted-sources.json`（v2.0.0，更新 2026-09-11）
- 规模：white_list 85 / kb_sources 29
- 层级分布：{'1': 48, '2': 33, '3': 4}
- 可信度分布：{'90': 20, '82': 29, '74': 28, '66': 8}
- 未验证条目：[]

## 六、结论

- 总判定 **pass**（各链：{'pass': 4}）
- 可处置项：0（actionable 凭证明文不落报告，仅记脱敏占位）
- 待办：可处置凭证需人工复核；consent 台账缺失属预期（默认关闭 + 无授权事件）
