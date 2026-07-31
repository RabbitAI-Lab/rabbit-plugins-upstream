## Description: <br>
Nusii Proposals helps agents read, create, and update Nusii Proposals data through the OOMOL `nusii_proposals` connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate a connected Nusii Proposals account, including account, client, proposal, template, theme, and user reads plus proposal workflow actions. Write actions require confirming the exact payload and effect before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read actions can expose account, client, proposal, template, theme, and user data from the connected Nusii Proposals account. <br>
Mitigation: Install and use the skill only for accounts where this access is intended, and scope requests to the minimum data needed. <br>
Risk: Write actions can create clients or proposals, update proposals, archive proposals, or send proposals. <br>
Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write actions. <br>


## Reference(s): <br>
- [Nusii Proposals homepage](https://nusii.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nusii-proposals) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
