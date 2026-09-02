# 隐私与安全边界

## 本地数据面

- 文件解析、格式校验、schema/画像、Parquet 规范化、SQL 校验与执行、有限结果、XLSX 和 HTML 报告全部位于用户本机。
- 单文件最大 100 MiB；支持 CSV、JSON/JSONL、XLSX 与 Parquet。XLSX 有工作表、压缩比、展开大小和 XML 防护限制。
- 数据目录和产物使用用户权限；Runner 拒绝符号链接跳转与不受信任路径。
- 删除只移除本地数据集。不要在删除成功前声称文件已清理。

## 授权控制面

付费命令先从调用者接收预计算内容哈希，在读取付费输入前只发送以下四个 JSON 字段：

```text
operation
runner_version
installation_id
input_fingerprint
```

平台不会收到文件名、文件字节、问题、schema、manifest、SQL、结果、报告摘要或本地路径。`input_fingerprint` 是 operation、dataset UUID 与内容 SHA-256 的 canonical JSON 摘要，不能还原内容。API Key 只出现在 `Authorization: Bearer` 请求头，重试键只出现在 `Idempotency-Key` 请求头。

签名执行票据是授权 JSON 响应中的 Runner 内部字段。Runner 自动提取并用盖章公钥验签；它不是公开 CLI 字段，宿主模型和用户都不传 `--ticket`。计费响应头仅用于遥测，不是票据验证机制；本地授权由签名票据及其 operation、installation、fingerprint、version 和计费绑定声明决定。

## 预哈希与 TOCTOU 防护

- `ingest` 要求 `--source-sha256`。
- `analysis`/`query` 要求 `--sql-sha256 --manifest-sha256`。
- `report` 要求 `--summary-sha256 --manifest-sha256`。
- Runner 用这些预计算摘要取得票据，然后重新读取本地输入并用常量时间比较；不一致返回 `authorization_invalid`，不执行内容。
- `inspect` 本地返回 schema 与 canonical manifest SHA-256，宿主模型不得用 DuckDB 或 Python REPL 绕过 Runner。
- 对自然语言分析，OpenClaw 宿主模型在本地读取 inspect，把请求转换成 SQL 文件；`analysis` CLI 没有问题文本参数，只接收 SQL 文件及其预计算摘要。

## SQL 与输出

- 只允许一条 `SELECT`/`WITH`；拒绝 DML、DDL、多语句、外部文件读取、网络函数、扩展安装/加载和未知表。
- 查询在隔离子进程中执行，限制内存、线程、临时目录和 30 秒运行时间。
- 返回最多 1,000 行、10 MiB。必须向用户说明 `truncated=true`。
- 报告 summary 有界；XLSX 防公式注入，HTML 使用限制性 CSP 且不加载远程资源。敏感内容仍保留在本机。

## 发布与安装信任

- 源树保持 fail-closed：`https://sql-data-analyst.invalid` 和空 `trusted_keys.json` 不能授权，也不能通过安装器。
- 发布构建器只接受真实、无凭据的 HTTPS origin、非空 Ed25519 公钥映射，以及与 canonical 公钥 JSON 匹配的 SHA-256。
- 发布物包含公钥，不包含签名私钥。Runner 会把内嵌公钥 bundle 与盖章 SHA-256 再次匹配。
- `SHA256SUMS` 覆盖发布文件；构建器与安装器都验证。缺少盖章、占位 origin、空 trust、哈希不符或被篡改时拒绝。
- 安装器仅支持 macOS/Linux；WSL2 走 Linux 分支。只允许 Python 3.12/3.13、用户拥有的真实目录和包内 `.venv`，不使用 sudo 或系统 site-packages。

## 稳定错误

| code | 含义 |
|---|---|
| `dataset_invalid` | 本地文件、数据集或路径无效 |
| `unsafe_sql` | SQL 未通过只读策略 |
| `unknown_table` | SQL 引用本地 manifest 以外的表 |
| `query_timeout` | 本地查询超过时间上限 |
| `query_resource_limit` | 本地内存、结果或进程限制触发 |
| `authorization_invalid` | 摘要、票据、公钥或计费声明不匹配 |
| `license_unavailable` | 平台授权暂不可用 |
| `report_failed` | 本地报告输入或写入失败 |

永远不要输出 `SQL_DATA_ANALYST_API_KEY` 的完整值。
