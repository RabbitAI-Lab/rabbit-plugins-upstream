## Description: <br>
monday (monday.com) lets an agent read, create, update, and delete monday data through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate monday.com workspaces through an OOMOL-connected account, including board, item, document, dashboard, team, audit log, and activity log workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change or delete monday.com data. <br>
Mitigation: Confirm the exact payload, target, and effect before approving write or destructive actions. <br>
Risk: The skill can access sensitive monday.com workspace or account data, including audit logs on enterprise accounts. <br>
Mitigation: Install and use it only for monday accounts and workspaces where the agent is authorized to operate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-monday) <br>
- [monday homepage](https://monday.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires fetching the connector action schema before constructing payloads; write and destructive actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
