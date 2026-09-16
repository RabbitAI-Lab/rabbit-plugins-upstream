## Description:

Buildium helps agents search and read Buildium rental owner, property, unit, and property note data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and property-management operators use this skill to retrieve Buildium rental owners, properties, units, and property notes without constructing Buildium API calls directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags an unverified remote installer command for the oo CLI.

Mitigation: Prefer a pinned, verifiable CLI installation path instead of running the pipe-to-shell installer as written.

Risk: The security evidence states that the connector action scope is broader than the read-only description.

Mitigation: Treat deployment as review-worthy unless the action list is constrained to documented read-only actions or write and destructive actions require explicit user approval.

## Reference(s):

- [ClawHub Buildium Skill](https://clawhub.ai/oomol/skills/oo-buildium)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Buildium Homepage](https://www.buildium.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector execution metadata such as an execution id when an action is run.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
