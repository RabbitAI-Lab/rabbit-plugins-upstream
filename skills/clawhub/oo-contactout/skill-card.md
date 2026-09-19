## Description:

ContactOut helps agents search, count, enrich, verify, and retrieve ContactOut people and company data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ContactOut through OOMOL for people and company search, profile enrichment, contact availability checks, email verification, decision-maker lookup, and usage statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code from the network if run without independent verification.

Mitigation: Use a trusted oo CLI installation path where available, or verify the installer source, signature, or checksum before running it.

Risk: ContactOut actions can retrieve personal contact data and may enable bulk or unsolicited data collection.

Mitigation: Use the skill only for legitimate ContactOut workflows, apply data-minimization practices, and follow applicable privacy, consent, and outreach policies.

Risk: Connector actions depend on live schemas and account connection state.

Mitigation: Inspect the live action schema before building payloads and run setup, login, or connection steps only after a command fails for the matching reason.

## Reference(s):

- [ContactOut homepage](https://contactout.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub ContactOut skill page](https://clawhub.ai/oomol/skills/oo-contactout)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; responses are returned as JSON with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
