## Description: <br>
Search and order pharmacy products from apohealth.de via apo-cli for medication or health-product search, product details, category browsing, and cart management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lars147](https://clawhub.ai/user/lars147) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to search apohealth.de pharmacy products, inspect product details and prices, browse categories, and prepare a cart link for user-completed checkout. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can add, remove, or clear items in a live apohealth.de cart. <br>
Mitigation: Review add, remove, and clear actions before execution; require confirmation before clearing the cart and keep checkout user-completed in the browser. <br>
Risk: The skill stores apo_cookies.json and apo_cart.json as local session files. <br>
Mitigation: Treat those files as private session data and avoid sharing or committing them. <br>
Risk: Medication and pharmacy-product lookup can be mistaken for medical advice. <br>
Mitigation: Use the skill only for product lookup and cart management, not diagnosis, treatment selection, or medical advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lars147/skills/apo-cli) <br>
- [apo-cli command reference](references/commands.md) <br>
- [apohealth.de](https://www.apohealth.de) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and cart URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include apohealth.de cart URLs; checkout remains user-completed outside the agent.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
