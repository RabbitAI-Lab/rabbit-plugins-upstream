## Description: <br>
Interact with Linear for issue tracking. Use when creating, updating, listing, or searching issues. Supports viewing assigned issues, changing status, adding comments, and managing tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[emrekilinc](https://clawhub.ai/user/emrekilinc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and workspace users use this skill to let an agent list, search, create, update, and comment on Linear issues while managing team, state, and user IDs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live Linear workspace data, including issue creation, status, assignee, priority, and comments. <br>
Mitigation: Confirm any issue creation, status change, assignee change, priority change, or comment before allowing an agent to run it against a real workspace. <br>
Risk: API requests are built from user-provided text for search, create, update, and comment fields. <br>
Mitigation: Avoid feeding untrusted text into those fields and review generated commands before execution. <br>
Risk: The skill uses a Linear API key to access workspace data. <br>
Mitigation: Use the narrowest Linear API key available and store credentials only in the documented environment variable or credentials file. <br>


## Reference(s): <br>
- [Linear API Examples](references/api-examples.md) <br>
- [Linear API settings](https://linear.app/settings/api) <br>
- [ClawHub skill page](https://clawhub.ai/emrekilinc/skills/linear-issues) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text or raw JSON from Linear API calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Linear API key from LINEAR_API_KEY or ~/.clawdbot/credentials/linear.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
