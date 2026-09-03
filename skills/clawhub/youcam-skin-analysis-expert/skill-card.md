## Description:

Analyze a person's skin from a single selfie using YouCam (Perfect Corp) AI, returning 16 skin-condition scores plus skin type as a readable report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run a YouCam skin analysis on a clear single-person selfie, then summarize the returned skin scores, skin type, strongest areas, areas needing attention, and non-medical care guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends a face photo to Perfect Corp/YouCam for analysis.

Mitigation: Use it only when the user is comfortable sending that photo to the service, and prefer a local image file over a URL.

Risk: The shared runner exposes broader inputs and API controls than a single-selfie skin report requires.

Mitigation: Limit execution to a clear front-facing JPG or PNG selfie and the documented skin-analysis parameters unless there is a specific reviewed reason to do otherwise.

Risk: AI skin-analysis output can be mistaken for medical advice.

Mitigation: Keep the report non-diagnostic, include the required disclaimer, and advise consulting a dermatologist for skin-health concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youcam-api/skills/youcam-skin-analysis-expert)
- [Perfect Corp AI Skin Analysis API documentation](https://docs.perfectcorp.com/reference/ai_skin_analysis.md)
- [Skin Analysis - interpretation](artifact/references/interpretation.md)
- [Skin Analysis - report format](artifact/references/output-format.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report based on JSON API results, with shell commands and configuration guidance during execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports only returned ui_score values, skin type, optional result images, and a required non-medical disclaimer.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
