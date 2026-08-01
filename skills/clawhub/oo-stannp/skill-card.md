## Description: <br>
Operate a connected Stannp account through OOMOL's oo CLI for account balance lookup, recipient and group management, and postal address validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to manage direct mail account data in a connected Stannp account, including recipients, recipient groups, balance lookup, and UK, US, or Canadian address validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read actions may expose recipient contact and postal address data from the connected Stannp account. <br>
Mitigation: Use the skill only for intended Stannp account operations and review returned recipient data before sharing or reusing it. <br>
Risk: Write actions can create recipients or groups and change group membership. <br>
Mitigation: Confirm the exact payload and expected account change with the user before running any action tagged as write. <br>
Risk: Destructive actions can permanently delete recipients or groups or remove recipients from groups. <br>
Mitigation: Require explicit approval for the target and effect before running any action tagged as destructive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-stannp) <br>
- [Stannp homepage](https://www.stannp.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON payload or response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses oo CLI connector actions; write and destructive actions require explicit user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
