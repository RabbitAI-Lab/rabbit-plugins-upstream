## Description: <br>
Reviews assembled LLM context windows to identify bloated, missing, misplaced, or contradictory context and recommend ordering, caching, and token-budget fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to audit real or template LLM context assemblies, reduce unnecessary token use, find instruction conflicts, and define enforceable context budgets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review inputs may include production context logs containing secrets, private user data, credentials, or proprietary retrieval content. <br>
Mitigation: Review and redact sensitive context before providing it to an agent session unless that session is approved for those materials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/context-engineering-review) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/context-engineering-review.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown review with inventory tables, verdicts, conflicts, ordering and caching recommendations, token budgets, and verification steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory output only; no executable behavior is included in the skill artifact.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
