## Description:

Operates Z-Library through an OOMOL-connected account to search books, retrieve metadata and recent additions, check account download limits, and download book files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Z-Library through the OOMOL oo CLI, including book search, metadata lookup, recent-book listing, download-limit checks, and authorized file downloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install the OOMOL oo CLI through remote installer commands.

Mitigation: Prefer a reviewed, version-pinned installation path with checksum or signature verification before using the connector.

Risk: The connector can access a connected Z-Library account and download book files.

Mitigation: Use download actions only for material the user is authorized to obtain, and confirm payloads before actions that create downloaded files.

Risk: The server security verdict is suspicious because compliance guardrails around book downloads are limited.

Mitigation: Review the skill and connector behavior before deployment, and apply organization-specific content access and copyright compliance policies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zlibrary)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Z-Library homepage](https://z-lib.org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing oo CLI payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
