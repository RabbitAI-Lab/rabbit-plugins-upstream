## Description:

Breeze (breezechms.com). Use this skill for ANY Breeze request -- searching and reading data. Whenever a task involves Breeze, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Breeze church management data through an OOMOL-connected account. It supports retrieving people, listing people with filters and pagination, and listing profile fields, tag folders, and tags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands for the oo CLI, and the security verdict flags this for review.

Mitigation: Install the CLI only from a verifiable official release or package manager, and review installer contents before execution.

Risk: Future Breeze write or destructive actions could modify or remove account data if added to the connector.

Mitigation: Require explicit user confirmation of the exact payload, target, and expected effect before running any write or destructive Breeze action.

## Reference(s):

- [Breeze homepage](https://www.breezechms.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Breeze action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
