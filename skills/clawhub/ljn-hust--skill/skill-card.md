## Description:

Use this skill for HTML documents that will go through LLM-human review cycles, including drafting, reading annotated files, revising feedback, and exporting clean presentation HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ljn-hust](https://clawhub.ai/user/ljn-hust)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and reviewers use this skill to create single-file HTML documents with stable review anchors, machine-readable feedback metadata, and revision workflows for LLM-human collaboration. It can also produce clean presentation HTML when review metadata is no longer needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated documents retain AI-readable collab-data metadata, comments, edits, and optional base64 screenshots that may persist sensitive review context.

Mitigation: Use the plain HTML mode for final audience-ready documents and avoid using review-mode files for content where persistent metadata is unacceptable.

Risk: Opening untrusted html-collab files in a networked browser may expose users to unexpected file or network behavior.

Mitigation: Review files before installing or opening them, and avoid opening untrusted html-collab documents in a networked browser.

Risk: The revision workflow can overwrite originals when file access is available.

Mitigation: Keep backups or versioned copies before applying revisions to annotated documents.

## Reference(s):

- [html-collab live demo](https://ljn-hust.github.io/html-collab/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with complete HTML file output or extracted document-feedback context blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated review documents include data-cid anchors, collab-data metadata, comments, edits, and optional base64 screenshot attachments; plain HTML mode omits review metadata and engine UI.]

## Skill Version(s):

0.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
