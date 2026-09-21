## Description:

Tanium (tanium.com). Use this skill for ANY Tanium request: reading, creating, and updating data through the OOMOL-connected Tanium connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Tanium Gateway GraphQL work through an OOMOL-connected account, including read and write-capable Tanium administration tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector routes broad Tanium work through a generic write-capable GraphQL action.

Mitigation: Inspect the live connector schema before building payloads and require explicit human approval for every GraphQL payload that can change Tanium state.

Risk: The first-time setup includes pipe-to-shell CLI installation instructions.

Mitigation: Review installer scripts or use a safer verified install path before installing the oo CLI.

Risk: The skill depends on OOMOL as an intermediary for Tanium administration.

Mitigation: Install only when the user trusts OOMOL for the connected Tanium account and understands that OOMOL injects credentials server-side.

## Reference(s):

- [Tanium homepage](https://www.tanium.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tanium)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce write-capable GraphQL requests that require explicit human approval before execution.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
