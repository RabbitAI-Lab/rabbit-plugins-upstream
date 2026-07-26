## Description: <br>
Measure helps agents read, create, and update Measure billing data through the OOMOL maple_billing connector and oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Measure billing workflows from an agent, including customer, product, pricing, subscription, and checkout-session lookup plus selected customer and checkout creation or update actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access Measure billing data through OOMOL. <br>
Mitigation: Install and use it only when the user intends to grant agent access through OOMOL and trusts that integration. <br>
Risk: Write actions can create or update Measure customers and checkout sessions. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write. <br>
Risk: First-time setup may install the oo CLI or connect an OOMOL account. <br>
Mitigation: Run installer, authentication, or account-connection steps only after a matching command failure and only with user approval. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-maple-billing) <br>
- [Measure Homepage](https://getmeasure.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
