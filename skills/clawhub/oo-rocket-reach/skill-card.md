## Description:

RocketReach (rocketreach.co). Use this skill for searching and reading RocketReach data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and sales or recruiting workflows can use this skill to search people and companies, look up profiles, check lookup status, and retrieve RocketReach account details through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can run remote installer scripts directly in a local shell.

Mitigation: Review the installer before running it, or use a signed and version-pinned oo CLI package when available.

Risk: The connector can access RocketReach data through the user's connected OOMOL account.

Mitigation: Use an account with appropriate RocketReach permissions and review connector payloads before running actions that expose person, company, or account data.

## Reference(s):

- [RocketReach skill page](https://clawhub.ai/oomol/skills/oo-rocket-reach)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [RocketReach homepage](https://rocketreach.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; command responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
