## Description:

Helps agents use the OOMOL CLI to discover TiMEM Space tools and manage memories through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

TiMEM Space users and developers use this skill to search, create, classify, and soft-delete memories and discover available tools through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup recommends running a remote CLI installer without verification.

Mitigation: Check the official OOMOL installation instructions independently and approve the installation before running it.

Risk: Write and destructive actions can change, overwrite, or delete account memories or other data.

Mitigation: Review the live action schema and exact target and payload; obtain explicit user approval before any write or destructive action.

## Reference(s):

- [TiMEM Space skill release](https://clawhub.ai/oomol/skills/oo-timem-space)
- [TiMEM Space](https://space.timem.cloud)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and structured results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain account memories; available actions depend on live tool schemas.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
