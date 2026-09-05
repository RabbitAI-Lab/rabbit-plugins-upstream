## Description:

Z-Library (z-lib.org). Use this skill for ANY Z-Library request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Z-Library, retrieve book metadata, check account download limits, browse recent books, and request book downloads through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The download_book_to_file action transfers a book file using the connected account and transit storage, although the release evidence says the skill under-labels this as a safe read-only operation.

Mitigation: Require user confirmation for the exact book identifier, hash, and download intent before running download_book_to_file; use search and metadata actions for read-only workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zlibrary)
- [Z-Library homepage](https://z-lib.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce connector action results, metadata summaries, quota information, and file-transfer guidance.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
