## Description:

Cardly (card.ly) lets an agent read, create, and update Cardly data through the OOMOL `oo` CLI connector instead of calling the Cardly API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Cardly through an OOMOL-connected account, including balance lookup, credit-history lookup, personalization asset listing, and authenticated request debugging. The skill guides agents to inspect each action schema before running connector commands and to confirm write or destructive actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup section includes remote installer commands for the oo CLI, including shell and PowerShell install scripts.

Mitigation: Do not allow an agent to run installer commands automatically; install the oo CLI only from a trusted source and prefer pinned or otherwise verified installation steps.

Risk: The skill can run write-tagged Cardly actions through an authenticated connector.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and require explicit approval for any destructive action.

## Reference(s):

- [Cardly homepage](https://www.card.ly)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Cardly connection settings](https://console.oomol.com/app-connections?provider=cardly)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are expected as JSON with `data` and `meta.executionId`; users should inspect the live schema before preparing payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
