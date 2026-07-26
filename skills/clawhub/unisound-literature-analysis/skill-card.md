## Description: <br>
Analyzes medical affairs research literature by matching user-provided topics and keywords to supplied literature records, summarizing evidence, and returning AI-assisted Markdown analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Medical affairs and pharmaceutical R&D teams use this skill to organize supplied literature records, screen them against a research topic, extract key findings, and produce a research-focused evidence summary. It is for literature analysis and does not provide clinical diagnosis, treatment advice, or promotional drug claims. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected literature fields are sent to a disclosed remote medical model endpoint. <br>
Mitigation: Use only documents your organization permits for that endpoint; avoid confidential, unpublished, patient-identifiable, or regulated content unless approved. <br>
Risk: The appkey is passed as a command-line argument and may be visible in local shell history or process listings. <br>
Mitigation: Provide the key through a protected runtime wrapper or secrets manager where possible, avoid logging commands with secrets, and rotate exposed keys. <br>
Risk: PDF, Office, spreadsheet, and image preprocessing uses local parsers and optional external tools on user-supplied files. <br>
Mitigation: Run conversion on trusted files or in a constrained environment, and install only the optional parsing tools required for approved input formats. <br>


## Reference(s): <br>
- [ClawHub listing for unisound-literature-analysis](https://clawhub.ai/unisound-llm/skills/unisound-literature-analysis) <br>
- [Referenced Literature Review skill](https://agent-skills.md/skills/ovachiever/droid-tings/literature-review) <br>
- [Remote medical model endpoint disclosed by the skill](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [json, markdown, text] <br>
**Output Format:** [UTF-8 JSON containing structured literature-analysis data and an AI-generated Markdown text field.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided appkey and supported input containing a topic, optional keywords, and literature records.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
