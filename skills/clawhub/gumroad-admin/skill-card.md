## Description: <br>
Gumroad Admin CLI. Check sales, products, and manage discounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abakermi](https://clawhub.ai/user/abakermi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Creators and operators who manage a Gumroad store can use this skill to check recent sales, list products, and create product discounts from an agent-assisted command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Gumroad access token enables sensitive store administration from the environment where the skill runs. <br>
Mitigation: Install only in environments intended for Gumroad administration and use the least-privileged token available. <br>
Risk: Discount commands can change live product pricing or promotions. <br>
Mitigation: Manually confirm the product ID, discount code, amount, and discount type before creating or changing discounts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/abakermi/skills/gumroad-admin) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GUMROAD_ACCESS_TOKEN in the agent environment before using Gumroad administration commands.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
