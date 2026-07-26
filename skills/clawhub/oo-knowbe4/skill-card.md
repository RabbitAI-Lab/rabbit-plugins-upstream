## Description: <br>
KnowBe4 lets an agent search and read KnowBe4 account, subscription, group, and user data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and operators use this skill to retrieve KnowBe4 account, subscription, group, and user information from an OOMOL-connected KnowBe4 account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read KnowBe4 account, group, and user information through an OOMOL-connected account. <br>
Mitigation: Install and use it only with an appropriate KnowBe4 connection and OOMOL account for the data being queried. <br>
Risk: Setup, authentication, connection, or billing steps may be unnecessary during normal read workflows. <br>
Mitigation: Run setup or billing recovery steps only when an oo command fails with the matching error. <br>


## Reference(s): <br>
- [ClawHub KnowBe4 skill page](https://clawhub.ai/oomol/skills/oo-knowbe4) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [KnowBe4 homepage](https://www.knowbe4.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector command responses are JSON objects containing data and meta.executionId when actions run.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
