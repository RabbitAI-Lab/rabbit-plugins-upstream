## Description:

People Data Labs (peopledatalabs.com) supports searching and reading People Data Labs data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query People Data Labs through an OOMOL-connected account for person and company enrichment or search workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can execute a remote installer for the oo CLI.

Mitigation: Install only when the CLI is missing and verify or manually inspect the installer before running it.

Risk: People Data Labs queries may send personal, confidential, or regulated data through OOMOL.

Mitigation: Review JSON payloads and file inputs before execution and avoid sending data that the user is not authorized to process.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-peopledatalabs)
- [People Data Labs Homepage](https://www.peopledatalabs.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce People Data Labs query payload guidance and summarize JSON results returned by the connector.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
