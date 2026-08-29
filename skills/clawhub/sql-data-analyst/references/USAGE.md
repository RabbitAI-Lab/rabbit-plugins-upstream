# 本地执行流程

以下所有文件访问与执行均发生在用户本机。平台授权请求使用 `Authorization: Bearer`、`Idempotency-Key` 和四个元数据字段；不发送输入内容。

```sh
export SQL_DATA_ANALYST_API_KEY="你的平台APIKey"
RUNNER="./scripts/sql-data-analyst"
PYTHON_BIN="./runtime/.venv/bin/python"
WORK_DIR="${TMPDIR:-/tmp}/sql-data-analyst-example"
mkdir -p "$WORK_DIR"
chmod 700 "$WORK_DIR"
sha256_file() {
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum "$1" | awk '{print $1}'
    else
        shasum -a 256 "$1" | awk '{print $1}'
    fi
}
new_dataset_id() {
    if command -v uuidgen >/dev/null 2>&1; then
        uuidgen | tr '[:upper:]' '[:lower:]'
    else
        "$PYTHON_BIN" -c 'import uuid; print(uuid.uuid4())'
    fi
}
```

## 1. doctor

```sh
"$RUNNER" doctor
```

doctor 不计费；若发布盖章、Python 依赖或本地工作区无效，先修复，不继续分析。

## 2. 本地导入与 inspect

```sh
SOURCE_FILE="/absolute/path/to/sales.xlsx"
DATASET_ID="$(new_dataset_id)"
SOURCE_SHA256="$(sha256_file "$SOURCE_FILE")"
"$RUNNER" ingest --dataset "$DATASET_ID" --source "$SOURCE_FILE" --source-sha256 "$SOURCE_SHA256"

INSPECT_FILE="$WORK_DIR/inspect.json"
"$RUNNER" inspect --dataset "$DATASET_ID" > "$INSPECT_FILE"
MANIFEST_SHA256="$("$PYTHON_BIN" -c 'import json,sys; from pathlib import Path; payload=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")); digest=payload["data"]["manifest_sha256"]; valid=isinstance(digest,str) and len(digest)==64 and all(character in "0123456789abcdef" for character in digest); sys.exit("invalid manifest_sha256") if not valid else print(digest)' "$INSPECT_FILE")"
test "${#MANIFEST_SHA256}" -eq 64
```

`PYTHON_BIN` 是安装器创建的包内 Python 3.12/3.13；JSON 提取只使用标准库，不依赖单行 JSON、空白或键顺序。Runner 在本地计算 canonical manifest SHA-256。`inspect.json` 包含宿主模型生成 SQL 所需的逻辑表名、列名与类型，不包含数据样例。

## 3. 宿主模型生成 SELECT，Runner 授权后本地执行

用户的自然语言请求保留在宿主上下文。宿主模型根据 `inspect.json` 在本地把自然语言请求转换为一条 UTF-8 SQL，并写入 `SQL_FILE`（下例为 `$WORK_DIR/query.sql`）。`analysis` CLI 不接收自然语言问题，也没有 `--question`；它只接收生成后的 SQL 文件与摘要。例如：

```sql
SELECT month, SUM(amount) AS total
FROM sales
GROUP BY month
ORDER BY month
```

```sh
SQL_FILE="$WORK_DIR/query.sql"
SQL_SHA256="$(sha256_file "$SQL_FILE")"
"$RUNNER" analysis --dataset "$DATASET_ID" --sql-file "$SQL_FILE" --sql-sha256 "$SQL_SHA256" --manifest-sha256 "$MANIFEST_SHA256" > "$WORK_DIR/result.json"
```

用户明确提供 SQL 时使用 `query` 命令。两者都只把摘要用于授权，再由 Runner 在用户本机重新校验并执行。授权响应中的签名执行票据由 Runner 内部自动读取和验签，不是公开 CLI 字段，也没有 `--ticket`。宿主模型随后本地解释 `result.json` 的有限行，并保留 `truncated` 限制。

## 4. 本地报告

宿主模型根据有限结果写入符合以下结构的 `$WORK_DIR/summary.json`：

```json
{"schema_version":1,"title":"销售汇总","findings":["收入按月汇总"],"limitations":["仅代表当前文件"],"tables":[{"title":"结果","columns":["month","total"],"rows":[["2026-01",120]]}],"charts":[{"title":"月收入","kind":"bar","table":0,"x":"month","y":"total"}]}
```

```sh
SUMMARY_FILE="$WORK_DIR/summary.json"
SUMMARY_SHA256="$(sha256_file "$SUMMARY_FILE")"
"$RUNNER" report --dataset "$DATASET_ID" --summary-file "$SUMMARY_FILE" --summary-sha256 "$SUMMARY_SHA256" --manifest-sha256 "$MANIFEST_SHA256"
```

返回的 XLSX 和自包含 HTML 路径都在本地工作区。

## 5. 本地删除

```sh
"$RUNNER" delete --dataset "$DATASET_ID"
```

错误处理：`license_unavailable` 可使用同一次 Runner 调用的持久化幂等键有界重试；`authorization_invalid`、`dataset_invalid`、`unsafe_sql`、`unknown_table`、`query_timeout`、`query_resource_limit`、`report_failed` 应先修正本地状态或输入，不循环盲重试。`X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance` 等计费响应头仅用于遥测，不是票据验证机制；Runner 验证授权响应中的签名执行票据。
