---
name: mirna-target-tools
description: miRNA靶基因预测与注释分析：TargetScan/miRanda预测、GO/KEGG富集、Cytoscape网络构建。
---

# miRNA Target Tools — miRNA靶基因预测工具

## Overview

集成常用生物信息学工具，自动化执行miRNA靶基因预测分析、靶基因功能注释与富集分析，并输出可直接导入Cytoscape的网络文件，完成调控网络可视化。

## 核心功能

### 1. TargetScan miRNA靶基因预测
运行TargetScan对输入miRNA序列进行靶基因预测，输出靶基因列表与评分。

使用脚本：`scripts/targetscan_predict.py`

### 2. miRanda miRNA靶标分析
运行miRanda进行miRNA-mRNA靶标结合预测，支持自由能计算和保守性分析。

使用脚本：`scripts/miranda_predict.py`

### 3. 结果整合与去重
合并多个工具预测结果，取交集提高可信度，生成基因列表。

使用脚本：`scripts/merge_targets.py`

### 4. 靶基因注释分析（新增）
对高置信度靶基因进行功能注释与富集分析：

- **基因注释**：基因符号 → Entrez ID / Ensembl ID / 功能描述（走 MyGene.info 在线 API，无需本地数据库）
- **GO/KEGG 富集**：GO（BP/CC/MF）+ KEGG 通路富集（走 g:Profiler REST API，标准库实现、零第三方依赖）
- **物种支持**：human / mouse / rat / **sheep（绵羊）/ goat（山羊）** / cow

使用脚本：`scripts/annotate_targets.py`

### 5. 富集结果可视化
将富集结果绘制为发表级气泡图（-log10(p) vs 通路，气泡大小=基因数）。

使用脚本：`scripts/plot_enrichment.py`

### 6. Cytoscape网络文件生成
生成可直接导入Cytoscape的`.sif`网络文件和属性文件，用于调控网络可视化分析。

使用脚本：`scripts/format_cytoscape.py`

### 7. miRNA 保守序列分析（新增）
对目标 miRNA 做多物种保守性分析（论文发表级）：

- **同源序列提取**：从 miRBase 自动提取目标 miRNA 在多个物种中的成熟序列（精确 mirbase-id 匹配，避免 miR-5046 类误配）
- **多序列比对**：端 gap 免费的全局比对（Needleman-Wunsch 变体，纯标准库实现），gap 集中于 5'/3' 端（isomiR 变异），种子区严格对齐
- **保守性量化**：Shannon 信息量（bits，Schneider-Stevens 1990）+ 每个位点同一性百分比 + 种子区（默认 2-8nt）单独统计
- **发表级可视化**：信息量序列 logo + 多序列比对图（300dpi PNG + SVG 矢量，WebLogo 配色）

使用脚本：`scripts/conservation_analysis.py`

## 完整分析工作流

**标准miRNA靶基因预测 + 注释分析 + 调控网络分析流程：**

1. 检查环境：确认TargetScan、miRanda、Python依赖已安装
2. 输入miRNA列表/序列文件
3. 分别用TargetScan和miRanda预测靶基因
4. 合并结果，取交集得到高置信度靶基因
5. 对靶基因做注释分析（基因注释 + GO/KEGG富集），并生成富集气泡图
6. （可选）对目标 miRNA 做多物种保守序列分析，验证种子区保守性
7. 生成Cytoscape网络文件（.sif格式）
8. 指导用户导入Cytoscape进行可视化和聚类分析

## 环境检查

使用前先运行`scripts/check_env.py`检查工具是否已安装：

```bash
python3 ~/.openclaw/skills/mirna-target-tools/scripts/check_env.py
```

如果工具未安装，会提示安装步骤。

## 输入格式

支持两种输入格式：
- `.txt`文件：每行一个miRNA名称（如hsa-miR-21-5p）
- `.fa`文件：FASTA格式miRNA序列文件

## 输出文件

**靶基因预测阶段：**
- `{sample}_targetscan_results.txt` - TargetScan原始结果
- `{sample}_miranda_results.txt` - miRanda原始结果
- `{sample}_merged_high_confidence.txt` - 合并后的高置信度靶基因列表

**注释分析阶段（annotate_targets.py 输出）：**
- `{sample}_gene_annotation.tsv` - 基因注释表（symbol → Entrez/Ensembl ID + 功能描述）
- `{sample}_enrichment_all.tsv` - 全部富集结果（GO:BP/CC/MF + KEGG）
- `{sample}_GO_BP.tsv` / `{sample}_GO_CC.tsv` / `{sample}_GO_MF.tsv` / `{sample}_KEGG.tsv` - 分来源富集结果
- `{sample}_enrichment_bubble.png` - 富集气泡图（plot_enrichment.py 输出）

**保守性分析阶段（conservation_analysis.py 输出）：**
- `{prefix}_aligned.fa` - 多序列比对结果（含 gap）
- `{prefix}_conservation.tsv` - 每个位点保守性统计（identity%、bits、碱基计数、覆盖率）
- `{prefix}_summary.tsv` - 汇总统计（种子区/核心区保守性、平均成对同一性）
- `{prefix}_sequence_logo.png/.svg` - 信息量序列 logo
- `{prefix}_alignment.png/.svg` - 多序列比对图

**网络构建阶段：**
- `{sample}_mirna_target_network.sif` - Cytoscape网络文件
- `{sample}_node_attributes.txt` - 节点属性文件（可导入Cytoscape）

## 示例用法

### 靶基因预测
```
python targetscan_predict.py --input mirna.txt --output results/targetscan.txt
python miranda_predict.py --mirna mirna.fa --mrna 3utr.fa --output results/miranda.txt
python merge_targets.py --targetscan targetscan.txt --miranda miranda.txt --output merged.txt
```

### 靶基因注释分析（新增）
```
# 从合并结果中提取靶基因，做注释 + GO/KEGG 富集（山羊示例）
python annotate_targets.py --input merged.txt --gene-col TargetGene \
    --species goat --output-dir results/annotation

# 富集结果可视化（气泡图）
python plot_enrichment.py --input results/annotation/merged_enrichment_all.tsv \
    --output results/annotation/merged_bubble.png --source KEGG --top 15
```

### miRNA 保守序列分析（新增）
```
# 从 miRBase 自动提取 miR-504-5p 的多物种同源序列并做保守性分析
python conservation_analysis.py --mirna miR-504-5p \
    --reference-species chi --outdir results/conservation --prefix miR-504

# 或提供自己的多序列 FASTA
python conservation_analysis.py --input-fa homologs.fa \
    --reference-species chi --outdir results/conservation

# 限定物种白名单 + 自定义种子区
python conservation_analysis.py --mirna miR-504-5p \
    --species hsa,chi,bta,mmu,oar --seed-start 2 --seed-end 8
```

### 网络构建
```
python format_cytoscape.py --input merged.txt --output network.sif --attr-output node_attributes.txt
```

## 环境依赖安装脚本

如需安装，可以使用`scripts/install_dependencies.sh`，支持Ubuntu/Debian和macOS。

Python依赖：
- `pandas`、`numpy`（必需）
- `mygene`（可选，仅基因注释功能需要；GO/KEGG富集为纯标准库实现，零额外依赖）
- `matplotlib`（可选，仅富集气泡图需要）
