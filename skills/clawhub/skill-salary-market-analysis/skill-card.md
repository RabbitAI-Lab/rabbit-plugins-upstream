## Description: <br>
薪酬市场调研分析技能（全球版）。支持国内+海外多源数据、28字段全球化模板、多币种自动换算（20+货币）、PPP购买力平价调整、分位值计算、17+章节专业报告、外派薪酬建议、多格式输出。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tuobadaidai](https://clawhub.ai/user/tuobadaidai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
HR, compensation, and recruiting teams use this skill to collect salary-market evidence, normalize salary data, calculate percentiles, compare regions or countries, and generate salary benchmarking reports. Developers and analysts can also use the bundled Python scripts to clean CSV inputs, convert currencies, apply PPP adjustments, export Excel files, and convert Markdown reports to Word. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk web scraping or proxy-based collection may violate source terms, access controls, or acceptable-use expectations. <br>
Mitigation: Collect data only from authorized sources and avoid proxy or anti-blocking tactics. <br>
Risk: Salary reports may influence compensation decisions even when source data is incomplete, stale, or unverified. <br>
Mitigation: Manually verify sources, dates, sample quality, and methodology before using outputs for compensation decisions. <br>
Risk: Salary datasets and generated reports may contain personal, confidential, or sensitive company information. <br>
Mitigation: Exclude personal and confidential data and store outputs in a dedicated controlled folder. <br>


## Reference(s): <br>
- [Skill Salary Market Analysis release page](https://clawhub.ai/tuobadaidai/skills/skill-salary-market-analysis) <br>
- [Report Template](references/report-template.md) <br>
- [Salary Methodology](references/salary-methodology.md) <br>
- [Global Data Sources](references/global-data-sources.md) <br>
- [Data Collection Guide](references/data-collection-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, CSV, JSON, Excel, Word] <br>
**Output Format:** [Markdown reports, JSON summaries, CSV/Excel data tables, Word documents, and Python shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3; optional SALARY_DATA_DIR controls the data directory.] <br>

## Skill Version(s): <br>
3.0.1 (source: server release metadata; artifact frontmatter says 3.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
