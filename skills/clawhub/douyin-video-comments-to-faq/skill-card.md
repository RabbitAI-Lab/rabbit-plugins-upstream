## Description:

Turns seller-selected Douyin comment questions and confirmed answers into a planned FAQ set with one still image per question.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers use this skill to turn selected Douyin comment questions and confirmed product answers into listing FAQ graphics, with a reviewed question-and-answer plan before paid lookups or image creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device authorization grants broad, continuing access to the shared Beatra account.

Mitigation: Authorize only if comfortable with shared account access; revoke the device authorization in the Beatra Console when no longer needed.

Risk: Approved lookups and image creation can spend Beatra credits, and explicitly supplied local files can be uploaded.

Mitigation: Review each approval and live price before paid work; inspect local files before choosing to upload them.

Risk: The installed package can silently update its own code.

Mitigation: Disable automatic updates if unreviewed code changes are unacceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/douyin-video-comments-to-faq)
- [Douyin comment FAQ workflow](artifact/references/workflow.md)
- [Comment lookup](artifact/references/comment-lookup.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Image files, Guidance]

**Output Format:** [Labeled FAQ plan and generated still-image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 4–8 question-and-answer stills; paid work requires separate approval.]

## Skill Version(s):

0.1.8 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
