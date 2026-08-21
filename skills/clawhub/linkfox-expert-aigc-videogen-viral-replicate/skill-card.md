## Description:

This skill helps agents analyze a reference viral product video and product imagery, generate a high-fidelity replacement video prompt, and delegate final short-video generation through LinkFox subskills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce marketers and agent users use this skill to turn a reference TikTok, Reels, Shorts, or product video and their own product images into a generated product short video that follows the reference video's structure and style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote LinkFox services may process supplied videos, product images, extracted frames, prompts, and generated media.

Mitigation: Avoid sensitive or private media, use only authorized product and reference materials, and confirm the user understands what will be sent to remote services before upload or generation.

Risk: The package includes bundled onboarding flows for phone-based login, API-key retrieval, plan selection, and payment QR generation.

Mitigation: Require explicit user confirmation before any login, API-key, upload, or payment action, and verify LINKFOX_* gateway environment variables before use.

Risk: Video generation may fail or raise compliance concerns for moderation, infringement, face, celebrity, or unauthorized likeness issues.

Mitigation: Stop on content-review failures and ask the user to provide authorized, compliant replacement product imagery rather than retrying or changing models to bypass the failure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-aigc-videogen-viral-replicate)
- [Workflow reference](artifact/references/workflow.md)
- [API mapping reference](artifact/references/api.md)
- [Prompt contract](artifact/references/prompts.md)
- [Data fields reference](artifact/references/data-fields.md)
- [Orchestration test cases](artifact/examples/test-cases.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain-text agent response with generated prompts, task status, failure explanations, and local media paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The final generation path is delegated to LinkFox subskills; successful runs should expose local MP4 paths rather than temporary remote media URLs.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
