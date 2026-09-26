## Description:

Guides an agent through Kujiale-powered interior design workflows for floor-plan confirmation, style selection, automated layout generation, and rendered output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Homeowners, interior designers, and real-estate teams use this Chinese-language skill to search or upload a floor plan, choose a style, generate a layout, and obtain render images, panorama links, and design highlights through Kujiale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Floorplan images and design data may be sent to Kujiale cloud services during the workflow.

Mitigation: Confirm user consent before uploading or processing floorplans, and avoid sending sensitive floorplan or design data when the user is not comfortable with Kujiale handling it.

Risk: The workflow requires a Kujiale access token.

Mitigation: Store the token outside version control, restrict permissions on local configuration files, and avoid printing or logging token values.

Risk: Layout and render actions may consume account quota or credits.

Mitigation: Ask for explicit user confirmation before running quota-consuming layout or rendering steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-kujiale-design)
- [Kujiale skills token page](https://www.kujiale.com/skills)
- [Kujiale design detail URL pattern](https://www.kujiale.com/pcenter/design/{designId}/setting?from=skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown result file plus direct image and link messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final output is expected at ./outputs/result.md with design highlights, render images, panorama links, and a Kujiale design detail link; progress messages are sent separately.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
