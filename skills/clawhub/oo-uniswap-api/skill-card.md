## Description:

Enables agents to inspect schemas and run Uniswap API actions through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to request Uniswap quotes, check ERC-20 approval requirements, and prepare swap calldata through the OOMOL connector while confirming write actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can direct an agent to run an unverified remote installer in a shell.

Mitigation: Review OOMOL's official install guide, prefer a pinned or verifiable installer where available, and require explicit confirmation before any setup, authentication, connection, or write action.

Risk: The create_swap action prepares transaction calldata for a Uniswap swap and is tagged as a write action.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-uniswap-api)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Uniswap API homepage](https://uniswap.org)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL authentication, and a connected Uniswap API account; write actions require explicit payload and effect confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
