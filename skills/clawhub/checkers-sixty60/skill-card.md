## Description: <br>
Shops on Checkers.co.za's Sixty60 delivery service through browser automation for grocery search, cart management, backup preferences, reorder flows, and deal evaluation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[snopoke](https://clawhub.ai/user/snopoke) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users who want an agent to help assemble a Checkers Sixty60 grocery basket use this skill to search products, compare deals, manage quantities and backups, and prepare cart changes before explicit confirmation. <br>

### Deployment Geography for Use: <br>
South Africa <br>

## Known Risks and Mitigations: <br>
Risk: The skill can affect a live Checkers/Sixty60 account, cart, delivery choices, checkout, payment, or order submission. <br>
Mitigation: Invoke it only for explicit Checkers/Sixty60 shopping requests and require confirmation before cart changes, delivery selection, checkout, payment, or order submission. <br>
Risk: Cart state can be inaccurate if product add, remove, or quantity controls fail to update. <br>
Mitigation: Verify the page state after each cart action and report stock, validation, or quantity mismatches before proceeding. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/snopoke/skills/checkers-sixty60) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text] <br>
**Output Format:** [Text instructions and step-by-step browser automation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires confirmation before cart, delivery, checkout, payment, or order submission actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
