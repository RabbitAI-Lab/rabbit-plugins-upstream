# vibecheck

**Audit code do AI sinh ra trước khi ship.**

`vibecheck` chấm điểm "vibe" 0–100 cho codebase: bắt lỗ hổng bảo mật, anti-pattern và "AI slop" — những thứ trông hợp lý nhưng không nên merge. Zero dependency, chỉ cần Python 3.8+.

> Vibe coding thì ai cũng làm được. Ship code vibe mà không audit lại là chuyện khác.

## Vì sao cần?

- Code AI thường có secret hardcode, `eval()`, exception bị nuốt, SQL ghép chuỗi.
- Reviewer có kinh nghiệm ít khi chê AI "sai thuật toán" — họ chê **bảo mật và chất lượng**.
- `vibecheck` = 1 lệnh, vài giây, trả lời câu "code này ship được chưa?".

## Cài đặt

### ClawHub

```bash
clawhub install thiennhant95/vibecheck
```

### Từ source

Không cần cài — chỉ cần Python 3.8+:

```bash
git clone https://github.com/thiennhant95/vibecheck && cd vibecheck
python3 vibecheck.py --help
```

Hoặc copy riêng file `vibecheck.py` vào dự án.

## Sử dụng

```bash
python3 vibecheck.py ./src                              # quét thư mục
python3 vibecheck.py app.py                             # quét 1 file
python3 vibecheck.py ./src --format md > report.md      # Markdown (PR comment)
python3 vibecheck.py ./src --format json                # JSON
python3 vibecheck.py ./src --format sarif > out.sarif   # GitHub code scanning
python3 vibecheck.py ./src --min-score 80 --fail-on high  # CI gate
python3 vibecheck.py . --exclude "tests" --exclude "generated"

# Nhận nuôi code legacy: ghi nhận lỗi cũ, chỉ fail lỗi mới
python3 vibecheck.py ./src --write-baseline .vibecheck-baseline.json
python3 vibecheck.py ./src --baseline .vibecheck-baseline.json
```

**Exit codes:** `0` pass · `1` fail (dưới `--min-score` hoặc có finding chặn) · `2` input lỗi.

### Điểm bị chặn theo mức nặng

Điểm cao không bao giờ che được lỗi bảo mật:

| Còn finding | Score tối đa | Verdict |
|---|---|---|
| CRITICAL | 30 | DANGER — do not ship |
| HIGH | 69 | RISKY — fix before merge |

Nhờ vậy một lỗi tắt kiểm chứng TLS hay SQL injection không thể bị báo là "production ready".

| Score | Verdict |
|---|---|
| 90–100 | CLEAN — production ready |
| 70–89 | OK — minor cleanup needed |
| 50–69 | RISKY — fix before merge |
| < 50 | DANGER — do not ship |

## Rule

18 rule, 3 scope: `raw` (toàn văn — secret/SQL nằm trong string), `code` (chỉ code — string/comment bị che), `comment` (chỉ comment).

| Rule | Mức | Bắt gì |
|---|---|---|
| `private-key` | critical | Private key commit vào source |
| `secret-aws` | critical | AWS access key id |
| `secret-token` | high | Token OpenAI/GitHub/Slack/Google |
| `secret-assignment` | high | Password/secret gán thẳng |
| `env-secret` | high | Secret thật trong `.env` (có quote hoặc không) |
| `sql-injection` | high | SQL ghép bằng f-string/`.format`/`%`/nối chuỗi |
| `eval-exec` | high | `eval`/`exec` (trực tiếp, alias, `builtins.*`) |
| `js-eval` | high | `eval`/`new Function` trong JS/TS |
| `shell-true` | high | `subprocess` với `shell=True` (kể cả qua biến) |
| `os-shell` | high | `os.system`/`os.popen` |
| `verify-false` | high | Tắt kiểm chứng TLS (kể cả qua biến) |
| `cors-wildcard` | medium | CORS cho mọi origin |
| `weak-hash` | medium | MD5/SHA1 dùng cho bảo mật |
| `pickle-load` | medium | Deserialize không an toàn |
| `yaml-unsafe-load` | medium | `yaml.load` thiếu loader an toàn |
| `except-pass` | low | Exception bị nuốt |
| `debug-log` | low | `console.log` sót lại |
| `todo-fixme` | info | TODO/FIXME |

Thêm cảnh báo cấu trúc mức info: `file-too-long`, `long-lines`, `long-function`.

### Ngoài regex

- **AST cho Python**: alias, constant propagation một bước, `builtins.eval`, `pickle` alias, `shell=True`/`verify=False` ẩn sau biến, YAML loader không an toàn (`UnsafeLoader`/`Loader` bị chặn; `SafeLoader`/`FullLoader` được phép).
- **Redact secret** trong mọi output (text, Markdown, JSON, SARIF, baseline, preview autofix).
- **Windows-safe**: ignore dùng path POSIX; stdout ép UTF-8 để report không crash trên console cũ.

## Suppression

```python
# vibecheck: disable=eval-exec      # dòng dưới bị bỏ qua cho rule này
dangerous_call(trusted_input)

risky_call(arg)  # vibecheck: disable=eval-exec

# vibecheck: ignore   (dòng đầu file = bỏ qua cả file)
```

Toàn dự án: tạo `.vibecheckignore`, mỗi dòng 1 regex (path kiểu POSIX trên mọi OS).

## Autofix

`--fix` ghi file trực tiếp. Mọi fix hiện tại đều đổi hành vi nên cần opt-in rõ ràng `--fix-unsafe`:

```bash
python3 vibecheck.py ./src --fix-dry-run --fix-unsafe   # xem trước, không ghi
python3 vibecheck.py ./src --fix --fix-unsafe           # áp dụng
```

| Tier | Rule | Fix |
|---|---|---|
| unsafe | `yaml-unsafe-load` | `yaml.load` → `yaml.safe_load` (bỏ qua nếu có `Loader=`) |
| unsafe | `verify-false` | Bỏ tham số tắt TLS |
| unsafe | `debug-log` | Xoá dòng `console.log` |

Autofix không sửa ngoài thư mục quét, bỏ qua symlink. Luôn review diff; không chạy autofix trong CI mà không commit kết quả.

## Kiểm chứng

- **44 test** (`python tests/test_vibecheck.py`): exact-line, regression dogfood, chống false positive, baseline, SARIF, file 1 MB một dòng, binary, Unicode, hardening v1.0 (alias, constant propagation, `.env`, score cap, ignore Windows-safe), redaction, autofix confinement.
- **Benchmark**: `benchmark.py` chạy corpus 9 file (15 cặp ground-truth) như regression gate — không phải benchmark toàn ngành.
- **Dogfood**: quét chính `vibecheck.py` được 100, chỉ còn cảnh báo cấu trúc mức info.
- Thử thực tế: `pallets/click` → 84 OK; `python-dotenv` → 100 CLEAN.

## Giới hạn

- Phân tích tĩnh, alias/AST một bước; không theo dõi luồng dữ liệu xuyên file.
- Secret `KEY=value` không quote chỉ được kiểm trong `.env*`; secret chia nhỏ/ghép chuỗi có thể lọt.
- SQL injection dựa trên pattern; truy vấn dựng động phức tạp có thể lọt.
- Không thay thế Semgrep/Bandit/CodeQL — đây là lớp kiểm tra nhanh trước khi merge.

## Quyền riêng tư

`vibecheck` không gọi mạng, không thực thi code được quét. Nó chỉ đọc file bạn trỏ tới và ghi output bạn yêu cầu (report, baseline, autofix). Report có thể chứa ngữ cảnh source; secret đã được redact nhưng vẫn nên coi là tài liệu nội bộ.

## Tích hợp

- `examples/github-action.yml` — upload SARIF cho GitHub code scanning
- `examples/pre-commit-config.yaml` — pre-commit hook

## Skill liên quan

- **vibegit** — ước lượng tỷ lệ AI-assisted của repo từ git history (slop score, badge, CI gate): [ClawHub](https://clawhub.ai/thiennhant95/vibegit) · [GitHub](https://github.com/thiennhant95/vibegit)
- **skill-firewall** — quét skill bên thứ ba trước khi cài: [ClawHub](https://clawhub.ai/thiennhant95/skill-firewall) · [GitHub](https://github.com/thiennhant95/agent-skills)
- **undo-first** — guard hành động có thể rollback (snapshot, risk gate, restore): [ClawHub](https://clawhub.ai/thiennhant95/undo-first) · [GitHub](https://github.com/thiennhant95/agent-skills)

## License

MIT. Xem [LICENSE](LICENSE).

---

English documentation: [README.md](README.md).
