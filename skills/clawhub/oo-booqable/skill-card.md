## Description: <br>
This skill helps agents operate Booqable through an OOMOL-connected account for reading, creating, and updating Booqable data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect Booqable schemas and run Booqable connector actions through the oo CLI for company, customer, order, and product group workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access Booqable customer and order data through the connector. <br>
Mitigation: Install it only for intended Booqable account access and review returned data before sharing or using it elsewhere. <br>
Risk: Tagged write or destructive actions could change or remove Booqable data if approved with the wrong payload. <br>
Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive operations. <br>
Risk: Connector input fields may differ from assumptions made before execution. <br>
Mitigation: Fetch the live action schema with oo connector schema before constructing a payload. <br>


## Reference(s): <br>
- [Booqable ClawHub skill page](https://clawhub.ai/oomol/skills/oo-booqable) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Booqable homepage](https://www.booqable.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return Booqable account, customer, order, and product data through the connector.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
