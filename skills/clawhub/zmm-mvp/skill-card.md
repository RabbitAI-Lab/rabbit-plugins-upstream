## Description:

Turns rough topic fragments into plain-text X test posts and records validation signals so a solo knowledge creator can decide whether to advance, expand, or discard a topic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to cheaply test topic demand with X posts before investing time in video production or long-form expansion. It supports drafting, local workflow registration, and data-based follow-up decisions for a solo publishing workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended to read and update local zmm vault files.

Mitigation: Install it only in a workspace where those vault files may be read and modified, and review generated draft and pipeline changes before relying on them.

Risk: The voice calibration workflow uses historical X-post data when available.

Mitigation: Point it only at X-post CSV data that the user is comfortable using for local content analysis.

Risk: The workflow may copy finished drafts to the local clipboard.

Mitigation: Check clipboard contents before pasting into a public posting surface.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-mvp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and plain text with optional shell commands for local workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local draft and pipeline records and copy finished text to the clipboard when used in its intended vault environment.]

## Skill Version(s):

0.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
