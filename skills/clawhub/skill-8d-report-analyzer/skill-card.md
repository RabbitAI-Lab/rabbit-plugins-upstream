## Description: <br>
Analyzes the quality of each step in an 8D report, with emphasis on D4 root-cause analysis, D3 containment, and D5/D6 corrective and preventive action logic. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
SQE, quality engineers, and supplier quality reviewers use this skill to parse Chinese 8D reports, confirm extracted content with the user, evaluate D1-D8 report quality, and produce prioritized improvement recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded 8D reports may contain customer, supplier, defect, or internal process details that are parsed and shown back in the conversation. <br>
Mitigation: Redact sensitive fields before use and confirm the parsed content before proceeding to analysis. <br>


## Reference(s): <br>
- [8D report evaluation criteria](references/8d-criteria.md) <br>
- [Source repository](https://github.com/duding-engicool/skill-8d-report-analyzer) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-8d-report-analyzer) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown analysis with optional JSON document parsing output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation of parsed report content before deep analysis.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
