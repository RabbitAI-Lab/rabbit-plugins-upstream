## Description:

html-collab helps agents create, read, and revise single-file HTML documents for iterative LLM-human review cycles with annotations, edits, and optional clean presentation output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ljn-hust](https://clawhub.ai/user/ljn-hust)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and reviewers use this skill to generate review-ready HTML documents, extract human comments and edits from annotated files, and produce revised or presentation-ready HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can become the default path for generic document drafting requests.

Mitigation: Install or enable it only when review-ready HTML is the intended document format; use plain HTML mode for finished presentation documents.

Risk: Revisions can overwrite annotated HTML files without creating a backup.

Mitigation: Keep an original copy or use version control before asking an agent to revise an annotated document.

Risk: Annotated documents and screenshots may include sensitive content that is retained in the conversation.

Mitigation: Remove sensitive content before sharing annotated files or screenshots with an agent.

Risk: The image-compression workflow uses local shell commands and processes pasted image data.

Mitigation: Review commands before running them and process images only in environments approved for the document contents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ljn-hust/skills/skill)
- [Publisher profile](https://clawhub.ai/user/ljn-hust)
- [html-collab live demo](https://ljn-hust.github.io/html-collab/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [HTML files, Markdown guidance, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated documents may include collab-data JSON, data-cid attributes, an embedded review engine, comments, edits, and optional base64 image data.]

## Skill Version(s):

0.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
