## Description:

Skyfire helps agents operate the Skyfire connector through an OOMOL-connected account for marketplace service lookup and buyer token creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to inspect Skyfire marketplace services and create buyer tokens through the OOMOL oo CLI. Write actions require confirmation of the exact token payload and intended effect before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path may execute a downloaded installer without independent verification.

Mitigation: Review the installer before use, or prefer a versioned or signed oo CLI release.

Risk: The create_token action can create funded or identity-carrying Skyfire buyer tokens.

Mitigation: Confirm the exact create_token payload and intended effect with the user before running the action.

## Reference(s):

- [Skyfire homepage](https://skyfire.xyz)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skyfire skill listing](https://clawhub.ai/oomol/skills/oo-skyfire)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; returns connector JSON responses when actions run.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
