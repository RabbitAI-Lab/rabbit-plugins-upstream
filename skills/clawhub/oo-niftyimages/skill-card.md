## Description:

NiftyImages (niftyimages.com). Use this skill for ANY NiftyImages request - searching and reading data. Whenever a task involves NiftyImages, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate NiftyImages through an OOMOL-connected account, including retrieving image details, listing account images and widgets, and reviewing image, widget, user, and impression statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path recommends executing remote installer scripts for the oo CLI.

Mitigation: Review the setup path before installing and prefer a verified, version-pinned, or package-manager installation method where available.

Risk: Connector commands can expose data from the connected NiftyImages account if run for the wrong target or date range.

Mitigation: Inspect the live action schema and confirm user-supplied identifiers, URLs, and date ranges before running account-scoped queries.

## Reference(s):

- [NiftyImages homepage](https://niftyimages.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when commands are run with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
