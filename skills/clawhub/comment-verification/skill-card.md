## Description:

Reads comments from local files or test pages, selects them using an RSFPH statistical marker test, and can append topic summaries to memory.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[llevm](https://clawhub.ai/user/llevm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users can organize comments from controlled local tests by selecting those that match a statistical marker pattern and appending topic summaries to memory. The test does not establish whether a comment is true, safe, or authentic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The prototype can save an entire short comment in persistent memory despite its documented claim to retain summaries only.

Mitigation: Use non-sensitive test comments and --dry-run before updating memory. Treat selected comments as unverified claims; remove the labeled memory block to undo an update.

## Reference(s):

- [SNSwatcher on ClawHub](https://clawhub.ai/llevm/skills/comment-verification)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown memory note block with topic summaries and audit statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can preview with --dry-run; a normal run appends the note block to memory.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
