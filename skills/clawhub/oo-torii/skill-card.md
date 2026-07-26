## Description: <br>
Torii (toriihq.com). Use this skill for Torii search and read requests through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to retrieve Torii app, contract, organization, user, workflow, and transaction data through OOMOL's Torii connector. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Torii responses can include sensitive business data such as users, transactions, contracts, and app inventory. <br>
Mitigation: Install and use the skill only for accounts where the agent is permitted to read Torii data, and treat returned records as sensitive business information. <br>
Risk: Future connector actions may write or delete Torii data even though this release only documents read and list actions. <br>
Mitigation: Review any connector action tagged as write or destructive, confirm the exact payload and effect, and require explicit user approval before execution. <br>


## Reference(s): <br>
- [Torii homepage](https://www.toriihq.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-torii) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Torii connector actions return JSON data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
