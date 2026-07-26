## Description: <br>
Gift Up enables agents to read, create, and update Gift Up account data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and business operators use this skill to manage Gift Up company, gift card, order, item, promotion, location, and transaction workflows from an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Gift card balance, redemption, void, reactivation, and undo actions can affect money-bearing records. <br>
Mitigation: Review the exact action, target, payload, and expected effect with the user before running state-changing Gift Up commands. <br>
Risk: The security evidence reports that several money-affecting actions are under-labeled in the artifact. <br>
Mitigation: Treat redeem, redeem in full, top up, undo redemption, reactivate, and void actions as requiring explicit approval even when the skill text does not tag them as write or destructive. <br>
Risk: The skill gives an agent access to Gift Up through an OOMOL-connected account. <br>
Mitigation: Install and use it only when that account access is intended, and keep Gift Up connection scopes aligned with the user's operational needs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-gift-up) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Gift Up Homepage](https://www.giftup.com/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector action responses are returned as JSON when commands are executed.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
