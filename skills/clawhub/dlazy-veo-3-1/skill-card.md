## Description:

Generate cinematic videos with Google Veo 3.1 from text prompts and optional image or video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to generate cinematic videos from text prompts, reference images, or an existing video. It supports frame-based generation, reference-image generation, and video extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy-hosted services, and video generation may use paid credits.

Mitigation: Send only prompts and media you are comfortable sharing with dLazy; use --dry-run to preview the request and estimated cost.

Risk: The skill requires an API key for hosted generation.

Mitigation: Prefer device-code login, keep credentials private, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, JSON, Shell commands, Configuration instructions]

**Output Format:** [Generated video assets with JSON task results and Markdown usage instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are returned as hosted asset URLs and can be saved locally; asynchronous tasks return a task identifier.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
