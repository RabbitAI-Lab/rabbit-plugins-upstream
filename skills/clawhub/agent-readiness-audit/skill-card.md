## Description: <br>
Audits whether AI agents can use a product's docs, APIs, onboarding, errors, and discovery surfaces, then produces a scored readiness report with findings and a prioritized fix list. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product teams, and documentation owners use this skill to evaluate whether agents can discover, understand, onboard to, and operate their product without human help. The audit produces surface-level scores, evidence-backed findings, prioritized fixes, and a re-test protocol. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may fetch and quote supplied product URLs and documentation during an audit. <br>
Mitigation: Use it only with product surfaces and documentation that the agent is permitted to inspect and quote. <br>
Risk: Audit findings can affect product documentation, onboarding, API, or agent-access policy decisions. <br>
Mitigation: Review the cited artifacts and proposed fixes before acting on the report. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/agent-readiness-audit) <br>
- [Agent Readiness Audit homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/agent-readiness-audit.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report with tables, findings, prioritized recommendations, and a re-test protocol] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scores six audit surfaces from 0 to 4 and requires cited artifacts for scores below 3.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
