## Description:

Wolfram|Alpha (products.wolframalpha.com) skill for searching and reading data through Wolfram|Alpha instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Wolfram|Alpha through an OOMOL-connected account for short answers, spoken-style results, and query validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that can be piped directly into a shell.

Mitigation: Review the oo CLI installation path first and prefer an official versioned package or separately download, inspect, and verify the installer before execution.

Risk: The skill depends on an external OOMOL-connected Wolfram|Alpha account and may fail when authentication, app connection, or billing is missing or expired.

Mitigation: Run setup only after an auth or connection failure, then verify sign-in, Wolfram|Alpha connection status, and billing before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wolfram-alpha-api)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Wolfram|Alpha API](https://products.wolframalpha.com/api/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Wolfram|Alpha answer text and connector execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
