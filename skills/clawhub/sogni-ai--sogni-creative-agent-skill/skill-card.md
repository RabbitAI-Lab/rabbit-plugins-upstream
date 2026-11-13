## Description:

An agent skill and CLI for creating and editing images, videos, and music with Sogni, with tools for media analysis, upscaling, personas, and multi-step creative workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can ask an agent to generate or edit images, video, and music, analyze media, or run a multi-step creative workflow through Sogni.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the release suspicious with medium confidence, citing privacy and safety-refusal concerns, mutable installers, and incomplete analysis; this does not establish malicious intent.

Mitigation: Review the exact package and installer before setup, keep API keys private, and preserve model refusals rather than disabling filters or retrying rejected requests.

Risk: Hosted workflows upload local reference media to Sogni storage, so private media may leave the device.

Mitigation: Use direct CLI mode for media that must stay local; otherwise submit only media you are allowed to upload.

Risk: Media generation can consume account balance, and priority has a 1.5× fair-use tradeoff.

Mitigation: Check the estimate before generation and ask for explicit opt-in before using priority.

## Reference(s):

- [Sogni](https://sogni.ai)
- [ClawHub release page](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Hosted API and workflows](references/hosted-api.md)
- [Image prompting guide](references/image-prompting.md)
- [Video prompting guide](references/video-prompting.md)
- [Long jobs and queues](references/long-jobs-and-queues.md)

## Skill Output:

**Output Type(s):** [Images, Videos, Audio files, Shell commands, Guidance]

**Output Format:** [Generated media files plus CLI commands and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media formats and generation options depend on the request.]

## Skill Version(s):

3.66.1 (source: frontmatter, CHANGELOG, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
