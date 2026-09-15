## Description:

Baidu Maps (lbsyun.baidu.com). Use this skill for ANY Baidu Maps request -- searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Baidu Maps through an OOMOL-connected account for geocoding, reverse geocoding, place search, route planning, administrative district lookup, IP location, and coordinate-based weather results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer scripts that security evidence marks for review before installation.

Mitigation: Review the installer path first and prefer an official package manager, inspectable installer, or version-pinned release with a verified checksum or signature.

Risk: Map queries may send location-related data through OOMOL and Baidu Maps.

Mitigation: Avoid submitting sensitive location data unless the user has approved the query and the connected account is appropriate for that data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-baidu-maps)
- [Baidu Maps homepage](https://lbsyun.baidu.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill usually returns Baidu Maps connector results as JSON through the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
