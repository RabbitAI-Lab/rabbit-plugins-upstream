## Description: <br>
Analyze guides an agent to structure analysis of data, code, text, decisions, and visuals by stating purpose, choosing a framework, prioritizing findings, checking counter-evidence, and ending with an action. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and workflow authors use this skill to guide structured analysis of user-provided data, code, text, visual material, and decisions. It emphasizes source labeling, prioritization, counter-evidence, and action-oriented conclusions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill text advertises command execution, file writing, and external API use without clear scope or consent boundaries. <br>
Mitigation: Run with least-privilege tool permissions; allow command execution, file writes, or external calls only after explicit user approval and a clear data scope. <br>
Risk: The skill may produce analysis or recommendations from incomplete, inferred, or user-provided information. <br>
Mitigation: Require source labels, counter-evidence, and human review before using the output for operational, business, or safety-relevant decisions. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with prioritized findings and recommended actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Claims should be marked as from input or inferred; findings are prioritized by severity.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
