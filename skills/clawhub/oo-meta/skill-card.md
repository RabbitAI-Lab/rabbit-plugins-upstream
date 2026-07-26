## Description: <br>
Meta (business.meta.com). Use this skill for Meta requests that search or read current user, ad account, campaign, and ads insight data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Meta business data through the oo CLI after confirming the live connector schema for each action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill accesses Meta business data through an OOMOL-connected account. <br>
Mitigation: Install and use it only when OOMOL is an acceptable intermediary for the connected Meta business account. <br>
Risk: Connector schemas and action payloads can change over time. <br>
Mitigation: Review the live connector schema before each action and build payloads from that schema. <br>
Risk: Future write or destructive Meta actions could alter or remove account data. <br>
Mitigation: Require explicit user approval before running any action tagged write or destructive. <br>


## Reference(s): <br>
- [Meta Business](https://business.meta.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-meta) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the oo CLI, OOMOL sign-in, and a connected Meta account.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
