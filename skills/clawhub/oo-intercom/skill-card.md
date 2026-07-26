## Description: <br>
Intercom (intercom.com). Use this skill for ANY Intercom request: reading, creating, and updating data through an OOMOL-connected Intercom account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Support, operations, and developer teams use this skill to let an agent inspect Intercom workspace data and perform confirmed contact or conversation updates through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update Intercom contacts and reply to, close, or reopen conversations. <br>
Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write action. <br>
Risk: The skill can read workspace data such as contacts, companies, conversations, tickets, events, tags, and admin records. <br>
Mitigation: Install only for Intercom workspaces where agent access to this data is intended. <br>
Risk: Connector schemas can change over time. <br>
Mitigation: Fetch the live action schema before constructing each payload. <br>


## Reference(s): <br>
- [ClawHub Intercom skill page](https://clawhub.ai/oomol/skills/oo-intercom) <br>
- [Intercom homepage](https://www.intercom.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
