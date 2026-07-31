## Description: <br>
Memos (usememos.com). Use this skill for ANY Memos request — reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent operate their connected Memos account through OOMOL, including memo reads, writes, updates, deletes, attachment management, and user lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, replace attachments for, upload attachments to, or delete data in the user's connected Memos account. <br>
Mitigation: Require user confirmation of the exact target, payload, and effect before write or destructive actions. <br>
Risk: The agent may act on an incorrect action schema or stale assumptions about available connector fields. <br>
Mitigation: Fetch the live action schema with oo connector schema before constructing each payload. <br>
Risk: Installation or connection troubleshooting can initiate authentication, billing, or service-connection flows. <br>
Mitigation: Use first-time setup steps only after a command fails with the matching auth, connection, command-not-found, or billing error. <br>


## Reference(s): <br>
- [Memos homepage](https://usememos.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [OOMOL Memos connection](https://console.oomol.com/app-connections?provider=memos) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, json, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector command results are returned as JSON when the skill uses the documented --json flag.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
