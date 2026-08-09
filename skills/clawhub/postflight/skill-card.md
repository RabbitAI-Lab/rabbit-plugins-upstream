## Description:

Postflight drafts scheduled X posts, reply options, and photo-library entries for a user's own account, then publishes only after authorized approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[soos3d](https://clawhub.ai/user/soos3d)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Postflight to prepare X posts from configured content pillars, manage media and photo-library inputs, draft replies for the user to send, and publish approved posts to their own account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Posts could be published to X unintentionally if the approval channel or credentials are misconfigured.

Mitigation: Configure telegramTo carefully, keep X/xurl credentials under user control, and publish only after reviewing the approval package and replying ship from the authorized account.

Risk: Drafts may include incorrect or misleading claims from repository material, metrics, or fetched public posts.

Mitigation: Review every draft and its source links before approval; the skill is designed to report uncertain or unverified content instead of publishing it.

Risk: Photo posts can expose sensitive location metadata if media bypasses the intended ingestion flow.

Mitigation: Use the photo ingestion script, which strips metadata, require user-provided location text, and verify photo metadata before upload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/soos3d/skills/postflight)
- [Skill Definition](artifact/SKILL.md)
- [Content Sourcing](artifact/CONTENT.md)
- [Publishing via the X API](artifact/PUBLISH-API.md)
- [Publishing via Browser](artifact/PUBLISH-BROWSER.md)
- [Reply Drafting](artifact/REPLY-DRAFTING.md)
- [Photo Ingestion](artifact/PHOTO-INGESTION.md)
- [Voice](artifact/VOICE.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text and Markdown with inline shell commands and JSON state entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts, approval packages, reply options, post logs, media paths, and configuration guidance are produced for the agent to present or execute with user approval.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
