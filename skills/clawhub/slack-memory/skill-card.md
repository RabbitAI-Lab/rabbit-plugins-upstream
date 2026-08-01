## Description: <br>
Slack Memory helps agents capture, search, and summarize Slack channel and thread decisions, context, and open loops through BlueColumn API-backed memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and agents working in approved Slack workspaces use this skill to preserve decisions, promises, channel context, and summaries so later answers can draw on workspace history instead of recent messages only. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist and search broad Slack workspace content through an external API without clear consent, channel limits, retention, or deletion guidance. <br>
Mitigation: Use only in explicitly approved workspaces and channels; avoid credentials, customer data, personnel data, and sensitive summaries; confirm retention and deletion controls before relying on it. <br>
Risk: Slack decisions, promises, and channel summaries may include sensitive or regulated business context. <br>
Mitigation: Limit captured content to non-sensitive summaries and review the exact text before sending it to BlueColumn. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/slack-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Guidance, Markdown] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BLUECOLUMN_API_KEY for BlueColumn API interactions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
