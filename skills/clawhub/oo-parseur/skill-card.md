## Description:

Provides Parseur access for searching and reading documents, mailboxes, mailbox schemas, and parsed document data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Parseur document and mailbox data through an OOMOL-connected Parseur account. It is intended for read-oriented search and inspection workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of unverified remote installer scripts.

Mitigation: Review the setup path before installing and prefer verified, version-pinned, or signed vendor installation instructions.

Risk: Use outside the intended Parseur read operations could expose unintended account behavior.

Mitigation: Use the skill only with an OOMOL-connected Parseur account for the documented get and list actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-parseur)
- [Parseur Homepage](https://parseur.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented Parseur connector actions; live schemas are inspected before payload construction.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
