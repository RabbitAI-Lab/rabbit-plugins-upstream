## Description:

Loyverse lets an agent retrieve Loyverse merchant, store, category, item, customer, and receipt data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect and retrieve read-only Loyverse account data after their OOMOL account is authenticated and connected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes pipe-to-shell installer commands from a remote URL.

Mitigation: Prefer an official, verifiable installation method for the oo CLI and avoid running remote installer scripts as written.

Risk: The skill depends on OOMOL as an intermediary for Loyverse account data.

Mitigation: Use only after confirming the OOMOL account connection, billing state, and data-sharing expectations are acceptable for the intended Loyverse account.

## Reference(s):

- [ClawHub Loyverse skill page](https://clawhub.ai/oomol/skills/oo-loyverse)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Loyverse homepage](https://loyverse.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses connector schemas before action payloads and returns read-only Loyverse data from get and list actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
