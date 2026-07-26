## Description: <br>
Stannp (stannp.com). Use this skill for ANY Stannp request - reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Stannp recipient and group workflows through an OOMOL-connected Stannp account, including account balance lookup, recipient listing, recipient creation and deletion, group membership changes, and address validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create or modify Stannp recipient and group records. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running any action tagged as write. <br>
Risk: Destructive actions can permanently remove recipients, groups, or group membership. <br>
Mitigation: Get explicit approval for the exact target before running any action tagged as destructive. <br>
Risk: Recipient records can contain postal address data. <br>
Mitigation: Review payloads before approval and avoid exposing unnecessary address details in responses. <br>


## Reference(s): <br>
- [Stannp homepage](https://www.stannp.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-stannp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before constructing payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
