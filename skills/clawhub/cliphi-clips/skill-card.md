## Description:

Turns the user's long videos into ready-to-post vertical clips with captions and branding, using the Cliphi API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cliphi](https://clawhub.ai/user/cliphi)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to find strong moments in long videos, generate free preview links, and render selected short clips only after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit video-processing jobs and renders that may use Cliphi credits.

Mitigation: Require explicit user approval before rendering and show preview links and reported costs before any paid render.

Risk: The skill requires a Cliphi API key for authenticated API calls.

Mitigation: Use the CLIPHI_API_KEY environment variable and revoke the key if access should stop.

## Reference(s):

- [Cliphi API Reference](https://www.cliphi.com/cliphi-actions.json)
- [Cliphi Skill on ClawHub](https://clawhub.ai/cliphi/skills/cliphi-clips)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown]

**Output Format:** [Markdown with inline bash code blocks and API response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CLIPHI_API_KEY for authenticated Cliphi API calls; a keyless demo endpoint is available.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
