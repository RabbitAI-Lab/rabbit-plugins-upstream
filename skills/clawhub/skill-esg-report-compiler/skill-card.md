## Description: <br>
协助企业完成ESG报告全流程编制；支持ESG数据收集整理、GRI/TCFD标准框架映射、数据验证、多维度可视化及PDF/HTML报告导出；当用户需要编制/生成ESG报告、分析ESG绩效数据或准备可持续发展披露文件时使用 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sustainability, compliance, and reporting teams use this skill to organize company ESG data, map it to GRI and TCFD-oriented disclosures, validate completeness, generate charts, and export PDF or HTML reports. Developers and operators can run the bundled scripts for repeatable local data collection, validation, visualization, and report generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Company ESG data or generated report claims may be incomplete, outdated, or unsuitable for publication without review. <br>
Mitigation: Review source data, validation findings, charts, and final ESG claims before external use or disclosure. <br>
Risk: Local Python dependencies are required for data processing, charts, and PDF generation. <br>
Mitigation: Install pandas, matplotlib, reportlab, and related dependencies only from trusted package sources and verify the environment before running the scripts. <br>


## Reference(s): <br>
- [GRI standards reference](references/gri_standards.md) <br>
- [TCFD framework reference](references/tcfd_framework.md) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-esg-report-compiler) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-esg-report-compiler) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, files] <br>
**Output Format:** [Markdown guidance with shell commands; generated JSON validation data, chart image files, and PDF or HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally on user-provided CSV, Excel, or JSON ESG data and requires Python dependencies such as pandas, matplotlib, and reportlab.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
