## Description: <br>
Operates Sendmator through OOMOL for reading, creating, updating, and deleting contacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to manage Sendmator contacts from an agent through their OOMOL-connected account. It supports contact lookup, listing, creation, updates, deletion, and first-time connection guidance when execution fails for setup reasons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create and update actions can change Sendmator contact data. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running write actions. <br>
Risk: Delete actions can permanently remove Sendmator contacts. <br>
Mitigation: Confirm the target contact and get explicit approval before running destructive actions. <br>
Risk: Connector schema drift or malformed payloads can cause failed requests or unintended contact changes. <br>
Mitigation: Inspect the live Sendmator action schema before constructing payloads and match its fields exactly. <br>
Risk: Using the skill requires trusting the OOMOL account connection that executes Sendmator actions. <br>
Mitigation: Complete OOMOL connection or setup steps only for an account integration the user trusts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sendmator) <br>
- [Sendmator Homepage](https://sendmator.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution and returns connector JSON responses with execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
