## Description: <br>
Reorder Foodora orders and track ETA/status with ordercli, requiring explicit user approval before order placement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent operators use this skill to preview and reorder previous Foodora orders, manage country/login setup for ordercli, and track active order status. The skill is intended for Foodora-specific requests where purchase actions require explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent toward placing a Foodora order, which may create a real purchase. <br>
Mitigation: Run preview-only reorder steps first, show what will happen, and execute confirmed purchase commands only after explicit user approval. <br>
Risk: Using ordercli may access a Foodora account or browser session. <br>
Mitigation: Install and use ordercli only when the user trusts it, keep requests Foodora-specific, and prefer scoped or throwaway configuration for testing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/steipete/skills/food-order) <br>
- [ordercli homepage](https://ordercli.sh) <br>
- [Foodora Austria](https://www.foodora.at/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts the user to preview order actions and requires explicit confirmation before purchase commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
