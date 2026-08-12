## Description:

Use this skill for HTML documents that will go through LLM-human review cycles, including drafting, reading annotated files, and revising documents from comments and edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ljn-hust](https://clawhub.ai/user/ljn-hust)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document authors use this skill to create self-contained HTML review documents, extract human comments and edits, and produce revised versions for iterative review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document text, comments, edits, and screenshots may be copied into chat history and stored inside the HTML file.

Mitigation: Use care with confidential documents and review the generated or revised HTML before sharing.

Risk: The skill can write new local HTML documents and overwrite revised documents.

Mitigation: Ask the agent to save a new version or backup before applying revisions to an existing file.

## Reference(s):

- [html-collab ClawHub release](https://clawhub.ai/ljn-hust/skills/html-collab)
- [html-collab live demo](https://ljn-hust.github.io/html-collab/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and complete HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write new HTML review documents, overwrite revised local HTML files, and include document text, comments, edits, and screenshots in the conversation context.]

## Skill Version(s):

0.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
