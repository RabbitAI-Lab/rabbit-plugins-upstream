## Description:

Jungle Scout helps agents use an OOMOL-connected Jungle Scout account to inspect connector schemas and run supported keyword, product, sales, and share-of-voice actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Jungle Scout Amazon keyword, product, sales-estimate, and share-of-voice data through the oo CLI with live connector schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inline remote installer commands can execute arbitrary code if the installer source is not independently trusted.

Mitigation: Avoid running remote installer commands unless the OOMOL installer source has been independently verified.

Risk: Write-tagged connector actions may change Jungle Scout state, and evidence notes internal inconsistency around get_share_of_voice.

Mitigation: Require explicit user confirmation of the exact payload and expected side effect before running write-tagged actions.

## Reference(s):

- [Jungle Scout Skill Page](https://clawhub.ai/oomol/skills/oo-junglescout)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Jungle Scout Homepage](https://www.junglescout.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command output is expected as JSON when actions are run with --json.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
