# 标准miRNA靶基因预测 + 注释分析流程

## 完整工作流步骤

### 1. 准备输入文件

**Input 1: miRNA list (`mirna_list.txt`)**
```
hsa-miR-21-5p
hsa-miR-155-5p
hsa-miR-146a-5p
```

**Input 2: miRNA FASTA (`mirna.fa`)**
```
>hsa-miR-21-5p
UAGCUUAUCAGACUGAUGAUGA
>hsa-miR-155-5p
UUAAUGCUAAUCGUGAUAGGGGU
```

**Input 3: 3'UTR FASTA (`3utr.fa`)**  
可以从Ensembl/UCSC下载。

### 2. 检查环境

```bash
python3 ~/.openclaw/skills/mirna-target-tools/scripts/check_env.py
```

如果有缺失，运行安装脚本：
```bash
bash ~/.openclaw/skills/mirna-target-tools/scripts/install_dependencies.sh
```

### 3. 运行TargetScan

```bash
python3 ~/.openclaw/skills/mirna-target-tools/scripts/targetscan_predict.py \
  --input mirna_list.txt \
  --output results/targetscan_raw.txt \
  --database /path/to/targetscan_db \
  --species human \
  --parse
```

输出：
- `results/targetscan_raw.txt` - 原始输出
- `results/targetscan_raw.txt.tsv` - 解析后的表格

### 4. 运行miRanda

```bash
python3 ~/.openclaw/skills/mirna-target-tools/scripts/miranda_predict.py \
  --mirna mirna.fa \
  --mrna 3utr.fa \
  --output results/miranda_raw.txt \
  --energy-cutoff -15 \
  --score-cutoff 60 \
  --parse
```

输出：
- `results/miranda_raw.txt` - 原始输出
- `results/miranda_raw.txt.tsv` - 解析后的表格

### 5. 合并结果

```bash
python3 ~/.openclaw/skills/mirna-target-tools/scripts/merge_targets.py \
  --targetscan results/targetscan_raw.txt.tsv \
  --miranda results/miranda_raw.txt.tsv \
  --output results/merged_high_confidence.tsv
```

### 6. 靶基因注释分析（新增）

对合并后的高置信度靶基因做功能注释 + GO/KEGG 富集：

```bash
# 从合并结果提取靶基因（列名 TargetGene），做注释 + 富集
python3 ~/.openclaw/skills/mirna-target-tools/scripts/annotate_targets.py \
  --input results/merged_high_confidence.tsv \
  --gene-col TargetGene \
  --species goat \
  --output-dir results/annotation
```

输出（在 `results/annotation/` 下）：
- `merged_high_confidence_gene_annotation.tsv` - 基因注释（symbol → Entrez/Ensembl ID + 功能描述）
- `merged_high_confidence_enrichment_all.tsv` - 全部富集结果
- `merged_high_confidence_GO_BP.tsv` / `_GO_CC.tsv` / `_GO_MF.tsv` / `_KEGG.tsv` - 分来源结果

**支持的物种**：human / mouse / rat / sheep（绵羊）/ goat（山羊）/ cow

**基因列表直接输入**（无需从合并结果提取）：
```bash
python3 ~/.openclaw/skills/mirna-target-tools/scripts/annotate_targets.py \
  --input gene_list.txt --plain-list \
  --species human --output-dir results/annotation
```
其中 `gene_list.txt` 每行一个基因符号。

### 7. 富集结果可视化（新增）

```bash
python3 ~/.openclaw/skills/mirna-target-tools/scripts/plot_enrichment.py \
  --input results/annotation/merged_high_confidence_enrichment_all.tsv \
  --output results/annotation/enrichment_bubble.png \
  --source KEGG --top 15
```

输出：`results/annotation/enrichment_bubble.png`（300 dpi 气泡图）

### 8. 生成Cytoscape网络

```bash
python3 ~/.openclaw/skills/mirna-target-tools/scripts/format_cytoscape.py \
  --input results/merged_high_confidence.tsv \
  --output results/mirna_target_network.sif \
  --attr-output results/node_attributes.txt
```

### 9. Cytoscape可视化

1. 打开Cytoscape
2. `File -> Import -> Network from File` → 选择 `.sif` 文件
3. `File -> Import -> Table from File` → 选择 `node_attributes.txt`，选"Import as Node Table"
4. 应用布局：`Layout -> yFiles Organic`
5. 样式设置：
   - 将 `NodeType` 映射到 **Node Fill Color**
   - 根据节点度调整 **Node Size** 突出核心基因
   - 应用Style默认模板或VizMapper美化

## miRNA 保守序列分析（独立功能）

对目标 miRNA 做多物种保守性分析，验证种子区保守性（论文发表级）。该功能独立于靶基因预测流程，可单独使用。

### 从 miRBase 自动提取同源序列

```bash
python3 ~/.openclaw/skills/mirna-target-tools/scripts/conservation_analysis.py \
  --mirna miR-504-5p \
  --reference-species chi \
  --outdir results/conservation \
  --prefix miR-504
```

首次运行会自动下载 miRBase `mature.fa`（缓存于 `~/.cache/mirna-target-tools/`），
也可用 `--mature-fa` 指定本地文件。

### 提供自己的多序列 FASTA

```bash
python3 ~/.openclaw/skills/mirna-target-tools/scripts/conservation_analysis.py \
  --input-fa homologs.fa \
  --reference-species chi \
  --outdir results/conservation
```

### 关键参数

| 参数 | 说明 | 默认 |
|------|------|------|
| `--mirna` | 目标 miRNA（如 miR-504-5p，不含物种前缀） | — |
| `--input-fa` | 用户提供的多序列 FASTA（与 --mirna 二选一） | — |
| `--reference-species` | 比对锚点参考物种前缀（如 chi/hsa） | 第一个序列 |
| `--species` | 物种前缀白名单（逗号分隔） | 全部 |
| `--seed-start/--seed-end` | 种子区范围 | 2 / 8 |
| `--mature-fa` | 本地 miRBase mature.fa | 自动下载 |
| `--no-plot` | 跳过绘图（仅输出 TSV） | 绘图 |

### 输出

- `{prefix}_aligned.fa` - 多序列比对（含 gap）
- `{prefix}_conservation.tsv` - 每位置保守性（identity%、bits、碱基计数、覆盖率）
- `{prefix}_summary.tsv` - 汇总（种子区/核心区保守性、平均成对同一性）
- `{prefix}_sequence_logo.png/.svg` - 信息量序列 logo
- `{prefix}_alignment.png/.svg` - 多序列比对图

## 参数选择建议

| 参数 | 宽松 | 严格 |
|------|------|------|
| TargetScan context score | -0.1 | -0.5 |
| miRanda energy | -10 | -20 |
| miRanda score | 50 | 80 |
| 富集 p-value 阈值 | 0.05 | 0.01 |

## 常见问题

**Q: TargetScan找不到数据库？**  
A: 需要手动从 https://www.targetscan.org/ 下载对应物种的数据库，然后用 `--database` 参数指定路径。

**Q: miRanda编译报错？**  
A: 检查是否安装了gcc。在Ubuntu上 `sudo apt-get install build-essential`。

**Q: 结果太少怎么办？**  
A: 放宽cutoff参数，或者取消只取交集。

**Q: 注释分析报 "Invalid organism"？**  
A: 确认物种名正确。山羊用 `goat`（映射到 g:Profiler 的 `chircus`）、绵羊用 `sheep`（`oarambouillet`）。脚本会自动映射，直接用通用名即可。

**Q: 注释分析需要联网吗？**  
A: 需要。基因注释走 MyGene.info，富集走 g:Profiler，均为在线 API（无需下载本地数据库）。离线场景请预先下载结果缓存。

**Q: 富集结果为空？**  
A: 可能物种注释数据库中该基因集无显著富集通路；可放宽 p 阈值或确认基因符号与所选物种匹配。
