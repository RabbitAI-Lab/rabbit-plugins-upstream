## Description:

Kujiale AI Interior Design guides an agent through floor-plan confirmation, style selection, automated layout generation, and rendering output using Kujiale account capabilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, and real-estate teams use this skill to generate interior-design previews from a searched or uploaded floor plan, choose a style, run layout generation, and collect rendered images, panorama links, and design highlights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kujiale access tokens may be exposed if stored in local project configuration.

Mitigation: Prefer a secret store or environment variable, keep token files out of shared repositories, and avoid logging token values.

Risk: Selected floor-plan images can be uploaded to Kujiale for processing.

Mitigation: Require the agent to confirm the exact image with the user before upload and avoid watching or uploading unrelated files.

Risk: Automated layout generation can consume account quota or credits.

Mitigation: Require explicit user confirmation before layout actions that spend Kujiale account resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-kujiale-design)
- [Kujiale skills token page](https://www.kujiale.com/skills)
- [Kujiale design detail URL pattern](https://www.kujiale.com/pcenter/design/{designId}/setting?from=skills)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown result file with rendered image links, panorama links, design highlights, and inline shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Kujiale access token and user confirmation before image upload or credit-consuming layout actions.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
