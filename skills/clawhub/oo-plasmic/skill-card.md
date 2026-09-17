## Description:

Plasmic (plasmic.app). Use this skill for searching and reading Plasmic data through OOMOL's oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Plasmic connector schemas and run read-only CMS actions, including listing and counting model rows, through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute local code.

Mitigation: Review the skill before installing and prefer an official package manager or a downloaded installer with signature or checksum validation; do not run curl-to-shell or irm-to-iex commands unless the OOMOL installer source is trusted and verified.

## Reference(s):

- [ClawHub Plasmic skill page](https://clawhub.ai/oomol/skills/oo-plasmic)
- [Plasmic homepage](https://www.plasmic.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL-connected Plasmic credentials and returns connector responses with data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
