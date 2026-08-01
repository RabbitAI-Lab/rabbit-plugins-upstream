## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams turn Gog-style Google and work-productivity requests into practical workflows, checklists, analysis, code changes, and verification notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to structure Gog-style Google Workspace and work-productivity requests into actionable plans, artifacts, checklists, analyses, code changes, or implementation support that can be validated against explicit success criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording may trigger this helper on general Google Workspace or CLI requests where a narrower skill would be more appropriate. <br>
Mitigation: Review routing triggers and narrow keywords or invoke manually when precise skill selection matters. <br>
Risk: Generated plans, checklists, code changes, or workflow guidance may be wrong if the user's constraints are incomplete. <br>
Mitigation: Keep assumptions visible, ask only for material missing inputs, and validate the output against the user's success criteria before acting on it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Gog Demand Signal](https://clawhub.ai/skills/gog) <br>
- [Google Workspace CLI Reliability Signal](https://github.com/nimbalyst/nimbalyst/issues/1086) <br>
- [Developer Workflow Discussion Signal](https://news.ycombinator.com/item?id=49069300) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with optional code, shell command, and configuration blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include reusable checklists, workflow templates, assumptions, validation notes, and follow-up risks.] <br>

## Skill Version(s): <br>
0.20260729.111836 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
