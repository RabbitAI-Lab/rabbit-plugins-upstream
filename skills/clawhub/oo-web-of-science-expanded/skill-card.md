## Description:

Web of Science Expanded (clarivate.com) supports searching and reading Web of Science Expanded data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Web of Science Expanded, retrieve publication records, inspect citation relationships, and generate citation reports from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Web of Science queries, document UIDs, and retrieved bibliographic data pass through the OOMOL connector.

Mitigation: Use the skill only when OOMOL is an acceptable intermediary for the intended Web of Science activity and data.

Risk: Use depends on the oo CLI and a valid OOMOL-managed Web of Science connection.

Mitigation: Verify the oo CLI installer source before first use and perform sign-in or connection setup only after an authentication or connection error.

## Reference(s):

- [Web of Science Expanded homepage](https://clarivate.com/academia-government/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector calls return JSON data and execution metadata when run with the oo CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
