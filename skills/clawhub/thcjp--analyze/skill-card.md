## Description: <br>
Analyze provides structured analysis for data, code, text, decisions, and visual material. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to turn input content into prioritized findings, contradictions, and recommended next actions. It can support code review, dependency analysis, report generation, and structured decision analysis when human judgment remains responsible for final decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run shell commands and may change project files during analysis or development tasks. <br>
Mitigation: Use it only in trusted workspaces, review proposed commands and diffs before accepting changes, and keep secrets out of the workspace unless containment is clear. <br>
Risk: Broad analysis guidance may produce incorrect or misleading conclusions. <br>
Mitigation: Treat outputs as review aids and verify important findings, dependency advice, and recommendations before acting on them. <br>


## Reference(s): <br>
- [Analyze skill page](https://clawhub.ai/thcjp/skills/analyze) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown or structured text with findings and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose project file changes or shell commands when used for development work.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
