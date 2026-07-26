## Description: <br>
This skill helps personal investors and early-stage finance analysts perform company financial analysis, valuation modeling, financial ratio analysis, and risk assessment through natural-language agent instructions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users such as personal investors, finance students, and junior analysts use this skill to structure single-company financial analysis, DCF and comparable valuation work, financial ratio review, and risk screening. It is intended to support analysis workflows and does not provide guaranteed investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read local files, write outputs, and run local commands when the agent uses it. <br>
Mitigation: Review any proposed command before execution, limit file access to the finance task, and avoid unnecessary credentials or private financial files. <br>
Risk: Financial analysis and valuation outputs can be misleading when source data is incomplete, stale, or based on aggressive assumptions. <br>
Mitigation: Use official financial statements where possible, disclose assumptions, compare multiple methods, and treat outputs as analysis support rather than investment advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/accounting-finance-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and optional code or shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce structured financial analysis reports, valuation assumptions, risk ratings, configuration examples, and execution logs from user-provided financial data.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
