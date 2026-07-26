## Description: <br>
Generates a Chinese-language dairy market intelligence PDF report from monthly dairy industry PDFs and supporting policy documents, covering prices, production, trade, GDT auction results, landed-cost calculations, outlook, analysis, innovation, and corporate or policy events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robotbird](https://clawhub.ai/user/robotbird) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and market analysts use this skill to convert Chinese dairy-market source documents into an executive-ready 12-section PDF report with validated data tables, KPI cards, GDT landed-cost calculations, and Chinese narrative analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local PDFs, DOCX, CSV, Excel, text, and markdown files in the working directory and can create scratch files and a PDF report. <br>
Mitigation: Run it only in a folder containing the intended dairy-market source documents and review optional pip dependencies before installing them. <br>
Risk: Market reports can become misleading if source documents are incomplete or data points are unavailable. <br>
Mitigation: Use the skill's documented data-source hierarchy, mark missing values as data unavailable, and review the final report before relying on it for business decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/robotbird/skills/dairy-market-report) <br>
- [Report data schema](references/data-schema.md) <br>
- [Data sources and retrieval guidance](references/data-sources.md) <br>
- [GDT landed-cost formulas](references/gdt-formulas.md) <br>
- [Report section template](references/report-template.md) <br>
- [Ministry of Agriculture and Rural Affairs](https://www.moa.gov.cn) <br>
- [National Bureau of Statistics of China](https://www.stats.gov.cn) <br>
- [General Administration of Customs of China](http://www.customs.gov.cn) <br>
- [Global Dairy Trade](https://www.globaldairytrade.events) <br>
- [USDA NASS](https://www.nass.usda.gov) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Chinese narrative guidance, JSON report data, shell commands, and generated PDF report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a single 12-section PDF report and may create scratch extraction files in the working directory.] <br>

## Skill Version(s): <br>
3.0.0 (source: SKILL.md frontmatter; ClawHub release version 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
