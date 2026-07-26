## Description: <br>
Aircall helps agents search and read Aircall calls, contacts, numbers, teams, and users through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and support operations teams use this skill to retrieve Aircall records from an OOMOL-connected Aircall account without calling the Aircall API directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Aircall call, contact, number, team, and user data is routed through OOMOL's connected workflow when read requests are made. <br>
Mitigation: Use only authorized Aircall accounts and install the skill only when the organization accepts that OOMOL connector data path. <br>
Risk: The current release is described as read-only and does not support write or admin Aircall tasks. <br>
Mitigation: Do not rely on this skill for write or administrative changes unless a future release explicitly lists and scopes those actions. <br>


## Reference(s): <br>
- [ClawHub Aircall Skill](https://clawhub.ai/oomol/skills/oo-aircall) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Aircall](https://aircall.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return Aircall connector JSON containing data and meta.executionId when actions are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
