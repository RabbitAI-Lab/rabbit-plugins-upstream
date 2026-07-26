## Description: <br>
BigMailer lets an agent read, create, update, and delete data in a connected BigMailer account through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a connected BigMailer account from an agent, including brand, contact, and contact-list lookup and management. Write and destructive actions require user confirmation before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create or modify BigMailer contacts and contact lists. <br>
Mitigation: Confirm the exact payload and expected account effect with the user before running create, update, or upsert actions. <br>
Risk: Destructive actions can delete BigMailer contacts or contact lists. <br>
Mitigation: Confirm the specific target and obtain explicit approval before running delete actions. <br>
Risk: The skill operates a connected BigMailer account through OOMOL. <br>
Mitigation: Install and use it only when the user intends the agent to act on that connected BigMailer account. <br>


## Reference(s): <br>
- [BigMailer homepage](https://www.bigmailer.io/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands inspect live connector schemas and return JSON responses from the oo CLI.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
