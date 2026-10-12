## Description:

Analyzes reference ads into shots and prompts, then helps create a similarly structured video or preview editable changes and pricing before generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers, creators, and developers use this skill to break down reference ad videos and produce similarly structured ads, with optional dialogue, person, or product edits. They can also request analysis without generating a video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos, images, audio, prompts, and edits are sent to AdsTurbo under the user's account.

Mitigation: Upload only material the user is permitted to share; do not submit private or regulated media without authorization.

Risk: Video generation and draft submission spend account credits, and retries can duplicate charges.

Mitigation: Show the quoted credit cost and obtain confirmation before submission; use idempotency keys for retries and check existing work rather than resubmitting after a timeout.

## Reference(s):

- [AdsTurbo Ad Video Clone on ClawHub](https://clawhub.ai/adsturbo/skills/adsturbo-ad-clone)
- [AdsTurbo API key workspace](https://adsturbo.ai/iris/api)
- [AdsTurbo pricing](https://adsturbo.ai/pricing)
- [Ad clone reference](references/ad_clone.md)
- [Asset upload reference](references/upload.md)
- [Work status reference](references/work.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with shot analysis, prompts, credit quotes, or generated video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis can be provided without generating a video; generation results may require waiting for completion.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
