## Description:

Flagsmith skill for retrieving feature flags, evaluating identity flags and traits, and identifying identities in a connected Flagsmith environment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Flagsmith feature flags and evaluate identity-specific flag state through their connected OOMOL account. It can also identify a Flagsmith user and optionally set identity traits when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends a remote OOMOL CLI installer that the security evidence says is unverified.

Mitigation: Use safer OOMOL CLI installation methods where possible and verify installer provenance before installation.

Risk: `identify_identity` can update identity traits and change Flagsmith state.

Mitigation: Require explicit confirmation of the identity, payload, and trait changes before running the action.

## Reference(s):

- [ClawHub Flagsmith skill page](https://clawhub.ai/oomol/skills/oo-flagsmith)
- [Flagsmith homepage](https://www.flagsmith.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flagsmith connector responses are JSON objects with data and meta execution identifiers.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
