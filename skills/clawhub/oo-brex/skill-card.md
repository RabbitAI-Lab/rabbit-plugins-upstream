## Description: <br>
Brex helps agents inspect connector schemas and run OOMOL-connected Brex read actions for company, user, budget, card account, expense, and transaction data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business operators use this skill to retrieve Brex account, budget, expense, transaction, company, and user information through an OOMOL-connected Brex account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Brex account and expense data may include sensitive financial or employee information. <br>
Mitigation: Ask for the specific Brex data or action needed, retrieve only task-relevant fields, and avoid exposing more account or expense detail than necessary. <br>
Risk: Financial or account changes could have business impact if a future Brex action proposes a write or destructive operation. <br>
Mitigation: Confirm the exact payload, target, and expected effect with the user before approving any write or destructive action. <br>
Risk: The broad Brex trigger can route many Brex-related requests through this connector even when the user only needs general guidance. <br>
Mitigation: Use connector actions only when the task requires Brex account data or an authenticated Brex operation. <br>


## Reference(s): <br>
- [ClawHub Brex skill](https://clawhub.ai/oomol/skills/oo-brex) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Brex homepage](https://www.brex.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing Brex action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
