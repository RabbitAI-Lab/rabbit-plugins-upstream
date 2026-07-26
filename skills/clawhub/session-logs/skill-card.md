## Description: <br>
Search and analyze your own session logs (older/parent conversations) using jq. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guogang1024](https://clawhub.ai/user/guogang1024) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to search local session JSONL logs, recover prior conversation context, and summarize message, cost, and tool-usage details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Session logs may contain private conversation content. <br>
Mitigation: Use narrow searches by date, topic, or session, and prefer summaries or redacted results instead of raw transcript output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/guogang1024/skills/session-logs) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq and rg; results should be scoped to requested sessions or search terms.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
