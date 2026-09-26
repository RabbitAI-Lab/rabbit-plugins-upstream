## Description:

Digest support snippets and post prepared case comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Support operations teams use this skill to turn user-provided support snippets into concise intake digests and draft case comments for handoff or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Draft case comments may be mistaken for approved operational updates, especially because the package summary says comments are posted while the inspected artifact builds a comment object.

Mitigation: Review generated case comments before operational use and confirm the case ID, priority, subject, follow-up category, and tags against the source support snippet.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/support-case-intake-desk)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Structured text objects for support_digest and case_comment outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No credentials, private-file access, persistence, code execution, or network behavior are described in the artifact.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
