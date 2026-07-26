## Description: <br>
PIPL Check helps small personal information processors run local PIPL compliance self-assessments and generate PDF or Markdown audit and impact assessment reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwumit](https://clawhub.ai/user/wwumit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, compliance staff, and small organizations use this skill to run local PIPL audit checklists, complete impact assessment prompts, import JSON responses, and produce self-check reports for internal review. <br>

### Deployment Geography for Use: <br>
China (CHN) <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes generated report files in the working directory. <br>
Mitigation: Run it in an intended project folder or disposable workspace and review generated files before sharing them. <br>
Risk: PDF output depends on the optional reportlab package. <br>
Mitigation: Pin and review the dependency before enabling PDF generation in stricter environments. <br>
Risk: Generated compliance reports may be mistaken for legal advice or formal regulatory submissions. <br>
Mitigation: Use the reports as self-check aids and have qualified counsel review compliance conclusions before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wwumit/skills/pipl-check) <br>
- [Small Personal Information Processor Simplified Measures reference](references/2026-simplified-measures.md) <br>
- [CAC official source for simplified measures](https://www.cac.gov.cn/2026-07/24/c_1786638889704872.htm) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, Files] <br>
**Output Format:** [Markdown guidance with bash commands and generated PDF or Markdown report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated reports are written locally; PDF output uses the optional reportlab dependency.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release, package.json, CHANGELOG, released 2026-07-24) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
