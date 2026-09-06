# need-to-parse-complex-medical-dicom-file

**纯标准库、离线、确定性的医学 DICOM 解析 / 检查 / 去标识化工具。**
解析复杂 DICOM 文件（Implicit/Explicit VR LE、序列、私有标签），导出未压缩像素，
一致性检查，PS3.15 基础配置子集去标识化，生成确定性合成测试文件。

## v1.0.6 → v2.0.0 变更

v1 是一个 987 字节的"元认知存根"：正文只有 Detection/Mitigation/Verification 三句
声明式描述，**零脚本、零数据、零参考**；frontmatter 版本 1.0.0 与注册表 1.0.6 漂移；
README 声称 "Requires python3 + pydicom" 却什么都不提供（幻觉依赖）；
"Complete Skill Reference (Unchanged)" 复述同一个空壳。

v2 把承诺变成可运行的字节：

| | v1.0.6 | v2.0.0 |
|---|---|---|
| 脚本 | 0 | `scripts/dicom_tools.py`（~1000 行，纯 stdlib）+ `scripts/selftest.py`（102 项自检） |
| 参考 | 0 | `references/` 3 份（日期+来源标注，定性/供参考） |
| 解析 | 无 | Implicit/Explicit VR LE、SQ 嵌套、私有标签、File Meta |
| 像素 | 无 | 未压缩 8/16 位 → PNM（P5/P6，16 位大端 maxval=65535） |
| 压缩像素 | 声称能"处理复杂 DICOM"（幻觉） | **诚实检测**：报告 fragments + pydicom/pylibjpeg 精确命令，绝不猜测像素值 |
| 去标识化 | 无 | PS3.15 基础配置子集：PHI 置空/移除、私有标签全删、DA/DT/TM 按 VR 清洗、UID 确定性重映射、(0012,0062/0063) 合规声明、固定 limitations |
| 测试 | 无 | 102/102 自检（生成器确定性、像素图案逐像素、deid PHI 清零、封装诚实性、错误退出码） |
| 幻觉面 | 高（声称能力=0，宣称依赖=pydicom） | 低：每个能力都可 `selftest` 复现；能力边界写进 docstring/SKILL/参考 |
| token 经济 | — | `summary` 默认紧凑 JSON；`parse --tags` 过滤；错误 JSON 结构化（stderr） |
| 速度 | — | 离线瞬时（本地 python3，零网络、零依赖） |

## 用法

```bash
python3 scripts/dicom_tools.py summary FILE.dcm                 # 默认首选
python3 scripts/dicom_tools.py parse FILE.dcm --tags 0010,0020 0028,0010
python3 scripts/dicom_tools.py pixels FILE.dcm --out img.pnm
python3 scripts/dicom_tools.py check FILE.dcm                   # exit 3 = 有错误
python3 scripts/dicom_tools.py deid FILE.dcm --out FILE_deid.dcm
python3 scripts/dicom_tools.py gen --out test.dcm --rows 64 --cols 64 --seed 7 [--vr implicit] [--bits 8] [--encapsulated]
python3 scripts/selftest.py                                     # 102/102
```

退出码：`0` 成功 · `2` 输入错误/诚实拒绝 · `3` check 发现一致性错误。
stdout 为 JSON（`ensure_ascii=False`）；错误 JSON 在 stderr（`{"status":"error","tool":...,"error":...}`）。

## 诚实边界（写进代码与文档的硬规则）

1. **不用于诊断** —— 所有输出仅技术检查用途（每条输出含 `purpose` 字段）。
2. **不解码压缩像素**（JPEG/JPEG-LS/JPEG2000/RLE/MPEG）—— 检测后报告 +
   `pip install 'pydicom pylibjpeg[all]'` 的精确命令；`pixels` 对此 exit 2。
3. **去标识化 ≠ 合规认证** —— `deid` 是 PS3.15 Annex E（300+ 标签）的直接标识符子集；
   输出 JSON 固定携带 `limitations`（burned-in 像素注释不移除等 4 条）。
4. **不联网、不写输入文件、确定性**（gen/deid 相同输入 → 相同字节）。

## 交付校验

- 最终自检：**102/102 PASS**（离线、确定性、合成数据，无 PHI、无网络）。
- 性能：525 KB（512×512×16-bit）文件各命令 <100 ms。
- **TREE-SHA256-v1：ff5a2b170d8fde9194a0574e6524e4eb042f4ed4eba9c3505b96014800ff3f65（7 文件）**
  算法：对每文件 entry=`<relpath>|<sha256(bytes)>`，按 entry 字典序排序后整体 sha256；
  排除 readme.md/skill-card.md/_meta.json/.published/.DS_Store 与
  .git/.clawhub/__pycache__/.pytest_cache（构建目录与现场安装目录同算法可比）。

## 依据（2026-09-06 核对，详见 references/）

- DICOM PS3.5 2026c（NEMA）§6.2/§7.1.2/§7.1.3/§7.5/§7.8/§8.2 —— 文件结构与值编码
- DICOM PS3.15 2026c（NEMA）§6.9/Annex E —— 属性保密配置与去标识化
- Transfer syntax UID 表（meddream 2020-08-19 / Gdcm 3.0 / postdicom 交叉核对）
- pylibjpeg 2.1.0（GitHub/PyPI）—— 外部解码路径的精确指向
