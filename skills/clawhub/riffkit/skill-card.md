## Description:

Helps agents turn a source video, template, or original creative brief into short AI-generated videos and ad creatives using Riffkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use the skill to plan, generate, and retrieve short-form videos or UGC-style ads from a video, template, or original brief, with optional characters, products, and languages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded videos, product images, and creative data are shared with Riffkit.

Mitigation: Upload only approved media and product data after confirming the file's purpose and trusting the service.

Risk: The skill keeps an account session locally after sign-in.

Mitigation: Use Riffkit logout and remove ~/.riffkit/session when the agent no longer needs account access.

Risk: The heartbeat can replace skill instructions from the web without integrity verification.

Mitigation: Disable automatic updates unless desired, and review changes before adopting a new skill definition.

Risk: Video generation and retries can spend account credits.

Mitigation: Check the service quote and obtain the user's approval before each credit-spending submission or retry.

## Reference(s):

- [Riffkit homepage](https://riffkit.ai)
- [Riffkit on ClawHub](https://clawhub.ai/riffkit/skills/riffkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Video links]

**Output Format:** [Markdown with video download links, captions, and a creative summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation occurs through the Riffkit service; browser-accessible download links expire after six hours.]

## Skill Version(s):

1.8.28 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
