## Description: <br>
Audits a user's AI tool stack by scoring each tool for ROI, identifying redundancies and gaps, and producing a structured productivity report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals and teams use this skill to review AI-tool spend, decide which subscriptions to keep, review, or cut, and identify the top workflow gaps in their current stack. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected user or reviewer context may be sent to configured AI tools. <br>
Mitigation: Confirm which engine is selected, disable web search when it is not needed, and avoid sharing secret-bearing inputs. <br>
Risk: Incomplete tool inventories or rough cost estimates can skew ROI scores and savings estimates. <br>
Mitigation: Collect tool names, monthly costs, primary use cases, and usage frequency before scoring, and present estimates as approximate. <br>
Risk: Optional report exports can overwrite files when an existing output path is reused. <br>
Mitigation: Use explicit report output paths only where overwrites are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yun520-1/ai-productivity-audit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report with ROI scores, spend analysis, gap categories, and next-step guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional Markdown export path may be offered when the user asks to save the report.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
