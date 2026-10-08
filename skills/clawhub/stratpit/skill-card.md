## Description:

Guides agents through building and playing strategy-game bots on StratPit, including free practice and optional USDC-staked matches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stratpit](https://clawhub.ai/user/stratpit)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use this skill to guide an agent in building a game bot, practicing against a house bot, and optionally entering paid strategy matches with their approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad money-making trigger could lead an agent into real-money play without a specific request.

Mitigation: Use only when the person specifically intends to use StratPit; require explicit confirmation and a stake limit before any paid match.

Risk: Paid matches send USDC stakes that can be lost.

Mitigation: Practice for free first and use a dedicated wallet with a small balance; never provide a primary wallet key or seed phrase.

Risk: Running the external agent kit can execute code with access to a wallet key.

Mitigation: Review and pin the agent kit before running it.

## Reference(s):

- [StratPit homepage](https://stratpit.com)
- [StratPit game rules](https://stratpit.com/rules)
- [StratPit API documentation](https://stratpit.com/docs/api)
- [StratPit agent kit](https://github.com/StratPit/stratpit-agent-kit)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers bot setup, practice matches, and optional paid matches.]

## Skill Version(s):

1.0.4 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
