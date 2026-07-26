## Description: <br>
Fern lets agents search and read Fern customer, payment-account, transaction, and exchange-rate data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent needs to retrieve Fern customers, payment accounts, transactions, or exchange-rate details without calling the Fern API directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Fern customer, payment account, transaction, and exchange-rate data through an OOMOL-connected account. <br>
Mitigation: Install only when the user trusts OOMOL and intends the agent to access those Fern data categories. <br>
Risk: First-time setup may require installing the oo CLI with a remote installer. <br>
Mitigation: Review the oo CLI installer before running it and follow the user's approved installation process. <br>
Risk: Future Fern connector actions could add write or destructive behavior. <br>
Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running any write or destructive action. <br>


## Reference(s): <br>
- [ClawHub Fern skill page](https://clawhub.ai/oomol/skills/oo-fern) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Fern homepage](https://fernhq.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-oriented Fern connector actions run through the oo CLI.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
