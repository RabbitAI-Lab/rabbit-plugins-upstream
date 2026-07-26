## Description: <br>
The Bitquery skill lets agents run Bitquery V2 GraphQL read queries through an OOMOL-connected account instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run Bitquery V2 GraphQL read queries through an OOMOL-connected account while checking the live connector schema before constructing payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill depends on OOMOL and Bitquery account access and may consume account credits when queries run. <br>
Mitigation: Install and connect the oo CLI only when the user trusts OOMOL, intends to use Bitquery through the connector, and accepts account credit usage. <br>
Risk: Bitquery requests depend on the current connector action schema and user-provided GraphQL query intent. <br>
Mitigation: Inspect the live action schema before constructing payloads and run only user-directed read queries unless the user explicitly approves a state-changing action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bitquery) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Bitquery homepage](https://bitquery.io) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON response envelopes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the OOMOL bitquery connector and may return Bitquery GraphQL response data with an execution id.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
