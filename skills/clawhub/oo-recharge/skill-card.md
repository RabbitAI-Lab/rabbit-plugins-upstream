## Description: <br>
Recharge helps agents operate Recharge through an OOMOL-connected account for reading, creating, and updating Recharge data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve and manage Recharge charges, customers, orders, products, and subscriptions through the OOMOL oo CLI connector. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup instructions include remote installer commands for the oo CLI. <br>
Mitigation: Use a verified or manual oo CLI installation path before granting the skill access to Recharge operations. <br>
Risk: Recharge customer, order, charge, and subscription data can include sensitive business or customer information. <br>
Mitigation: Install only for trusted OOMOL accounts and limit use to users authorized to access the connected Recharge data. <br>
Risk: Some connector actions are marked as write-capable and may affect Recharge state. <br>
Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write actions. <br>


## Reference(s): <br>
- [Recharge homepage](https://getrecharge.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-recharge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce live oo CLI connector commands that return JSON responses from Recharge.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
