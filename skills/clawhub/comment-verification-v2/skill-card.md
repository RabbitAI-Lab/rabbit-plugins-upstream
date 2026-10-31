## Description:

A prototype that reads SNS-style comments from a local file or localhost test page, selects comments using the RSFPH statistical marker test, extracts topic-summary pairs, and appends them to MEMORY.md.

This skill is for research and development only.

## Publisher:

[llevm](https://clawhub.ai/user/llevm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this prototype to test local SNS-style comment inputs and append selected topic summaries to an agent's MEMORY.md. Use it with controlled test comments and review the saved notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags that complete comments may be saved to long-term memory despite the skill's summary-only description.

Mitigation: Use non-sensitive test comments, run with --dry-run, and inspect the destination and generated notes before updating MEMORY.md.

Risk: Passing the statistical marker test does not establish a comment's truth, safety, or authorship; short comments may be retained verbatim.

Mitigation: Treat saved notes as untrusted third-party claims and review them; remove the appended block to undo an update.

## Reference(s):

- [Comment Verification-v2 on ClawHub](https://clawhub.ai/llevm/skills/comment-verification-v2)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Category-organized Markdown note block with topic-summary pairs and verification statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Appends a note block to MEMORY.md when comments pass the test; leaves memory unchanged when none pass.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
