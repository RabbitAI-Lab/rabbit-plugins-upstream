# 发版与回归验证流程（维护者）

本 Skill 的发布与回归验证由维护者侧工具链驱动。该工具链位于**维护者仓库**的 `_audit/` 目录，**不随发布包分发**（发布包仅含 `scripts/` + `rules/` + `config/` + `references/` + `ci_templates/` 等运行与说明资产）。

> **沙箱形态说明（v3.0.1 起）**：发布包以沙箱形态分发——引擎明文源码保存在维护者侧
> `_audit/engine_dev/analyze_skill.txt`（**.txt 扩展名**，避免被杀毒软件对"含恶意载荷检测正则的
> `.py` 引擎源码"的启发式误杀），构建时打包为 `0_engine_b64.txt`（engine.zip 的 base64 文本，SkillHub 允许文本、杀软不识别）；`scripts/` 下**不落明文**
> `analyze_skill.py`，运行时由 `sandbox_run.py`/`_load_engine.py` 经 zipimport 内存加载。
> 引擎开发一律改 `_audit/engine_dev/analyze_skill.txt`（用 Edit/Write 工具或非 .py 读取均安全），
> 改完重建 `0_engine_b64.txt`（base64(engine.zip)）并同步到 `skill-src/scripts/`。

## 工具链（`_audit/*.py`）

| 脚本 | 作用 |
|------|------|
| `patch_v301.py` | 把 v3.0.1 补丁（5 个新检测器 + 沙箱适配等 15 处）应用到 `engine_dev/analyze_skill.txt`（每次从 v3.0.0 基线重建时用；常规迭代直接在 .txt 上改） |
| `gen_engine_hashes.py` | 重新生成 `rules/engine_hashes.json`（沙箱清单：`0_engine_b64.txt` / `build_engine.py` / `sandbox_run.py` / `_load_engine.py` / `selfcheck.py` / `watchdog.py` / `logger.py` / `nosec.py` 的 SHA-256）。**每次重建 `0_engine_b64.txt` 或改 `scripts/*.py` 后必须重跑**，否则运行时自扫描会误报"分析器完整性被破坏"。 |
| `reverse_validate.py` | 反向逻辑自洽校验（**54 项**：新检测器功能 / 版本自检与动态沙箱用例 / 显式更新流用例 / 规则包完整性用例 / **可核验性用例**（v3.0.7：篡改源码锚拒装、build_engine 哈希锚核验、主包无明文引擎源码）/ 门禁与评分不变量 / 模糊输入抗崩溃；从 `0_engine_b64.txt` 沙箱加载引擎）。全 PASS 才可发版。 |
| `gen_manifest.py`（v3.0.4） | 重新生成 `rules/manifest.json`（规则包完整性清单：每个顶层规则文件的 SHA-256）。**每次改动 `rules/*.json`（内容或增删）后必须重跑**，否则 selfcheck「规则包完整性」门禁失败、引擎对失配文件静默回退内置规则。 |
| `gen_signature.py`（v3.0.5，v3.0.7 改源码哈希锚） | 生成根目录 `publisher-signature.json`（发布者离线 SHA-256 指纹链 + 发布者身份锚 + **`engine_sha256` 引擎源码哈希锚**，从 `0_engine_b64.txt` 解码计算）。**每次重建 `0_engine_b64.txt` / `engine_hashes.json` 后必须重跑**，否则 `--update` 签名锚定核验失败。 |
| `selfcheck.py`（包内 `scripts/`） | 发布前回归门禁（自扫描零误报 / 版本一致性 / **规则包完整性（v3.0.4）** / `--corpus` 下加恶意样例命中、检出率误报率、动态沙箱门禁）。**v3.0.5 起主包不含恶意样本夹具**，恶意样例检测从独立基准库取样本。 |
| `build_corpus.py` | 生成对抗基准库样本（`_audit/corpus/`，包外独立分发，用于量化指标）。 |
| `package.py` | 打包为 `skill-analysis X.Y.Z.zip`（顶层 `skill-analysis/`），校验四处版本戳与必备文件齐备 + rules manifest 完整性断言。 |

> 对抗基准库独立分发，单独打包为 `skill-analysis-corpus X.Y.Z.zip`；使用方式见主包 `SKILL.md` 中关于 `selfcheck.py --corpus` 的说明（自检命令与基准库用法）。

## 标准发版流程（沙箱形态）

1. **改引擎**：在 `_audit/engine_dev/analyze_skill.txt`（引擎明文源，.txt 形态）完成改动。
2. **重建引擎文本包**：`python _audit/skill-src/scripts/build_engine.py --build _audit/engine_dev/analyze_skill.txt`（从明文源码可复现重建 `0_engine_b64.txt`，全程原始字节；主包**不携带明文源码**）。
3. **改脚本/文档**：在 `_audit/skill-src/` 下改 `scripts/*.py`、`rules/`、`SKILL.md`、`CHANGELOG.md`、`references/`。
4. **重算引擎哈希**：运行 `gen_engine_hashes.py`，刷新 `rules/engine_hashes.json`（重建 0_engine_b64.txt 或改 scripts 后必做）。
5. **重算规则清单**：改动 `rules/*.json` 后运行 `gen_manifest.py`（v3.0.4 起必做，否则规则被静默回退内置）。
6. **生成发布者签名锚**：运行 `gen_signature.py`（v3.0.7 起锚定 engine_sha256 源码哈希 + 0_engine_b64.txt + engine_hashes.json）。
7. **反向验证**：运行 `reverse_validate.py`，须 **54/54** 全部通过（从 0_engine_b64.txt 沙箱加载引擎）。
8. **发布前自检**：在 `_audit/skill-src/scripts/` 运行 `selfcheck.py --corpus <基准库>`，须六道门禁全 PASS（自扫描零误报 / 版本一致 / 规则包完整性 / 恶意样例命中（基准库）/ 检出率误报率 / 动态沙箱门禁）。
9. **打包**：运行 `package.py`，产出 `skill-analysis X.Y.Z.zip`；确认 zip 完整性（testzip OK）、四处版本戳一致、必备文件齐备（含 `publisher-signature.json` / `build_engine.py`，**不含明文 `analyze_skill.py`、明文 `engine_src.txt` 与二进制 `engine.zip`**）、rules manifest 完整性断言通过。
10. **保留旧版**：新版本 zip 发布时，**不删除**被取代的旧版本 zip，作为交付留档。

## 版本戳一致性约定

发布前须保证人手一致的四处版本号：

- `SKILL.md` frontmatter 的 `version:` 字段
- `_meta.json` 的 `"version"`
- `rules/manifest.json` 的 `pack_version`
- `0_engine_b64.txt` 内 `analyze_skill.py` 引擎 docstring 中的 `vX.Y.Z`（由 `selfcheck.py` 从 base64 解码后读取校验）

缺一处不一致，`selfcheck.py` 的「版本一致性」门禁即失败，无法发布。
