## Description: <br>
Amplemarket (amplemarket.com). Use this skill for Amplemarket requests involving reading, creating, and updating data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Amplemarket connector schemas, run read actions for contacts, lead lists, accounts, tasks, statuses, and types, and perform approved task state updates through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Amplemarket task state. <br>
Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running actions tagged as write or destructive. <br>
Risk: Connector commands depend on an authenticated OOMOL account, an active Amplemarket connection, and available OOMOL credit. <br>
Mitigation: Run setup or recovery steps only after command failures indicate missing CLI installation, authentication, connection scope, expired credentials, app readiness, or billing limits. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-amplemarket) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Amplemarket Homepage](https://www.amplemarket.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
