## Description:

Diagnoses hair-health metrics including density, type, frizziness, and length from user-provided hair photos using YouCam (Perfect Corp) AI and returns a combined plain-language report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through an agent to request selected hair-health metrics from selfies or three-angle photo sets, confirm YouCam credit cost before API calls, and receive a non-medical report with gentle care guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hair and selfie photos are sent to YouCam/Perfect Corp APIs and may be sensitive personal data.

Mitigation: Run only with user consent, use photos intended for analysis, avoid private or sensitive internal URLs, and follow applicable privacy and data-handling policies.

Risk: Running selected detections can spend YouCam credits.

Mitigation: Check and disclose per-feature credit costs before running, then execute only the metrics the user selected.

Risk: Results can be affected by photo quality and pose and are not medical diagnosis or treatment.

Mitigation: Request the required front-facing, three-angle, or tilted-head photos for the selected metrics and include the non-medical disclaimer with dermatologist guidance for hair-loss or scalp concerns.

Risk: A local credentials.json file can expose the YouCam API key if mishandled.

Mitigation: Prefer the YOUCAM_API_KEY environment variable and do not commit or share real credentials.

## Reference(s):

- [Hair Diagnostics interpretation guide](artifact/references/guide.md)
- [AI Hair Density Detection API documentation](https://docs.perfectcorp.com/reference/ai_hair_density_detection.md)
- [AI Hair Type Detection API documentation](https://docs.perfectcorp.com/reference/ai_hair_type_detection.md)
- [AI Hair Frizziness Detection API documentation](https://docs.perfectcorp.com/reference/ai_hair_frizziness_detection.md)
- [AI Hair Length Detection API documentation](https://docs.perfectcorp.com/reference/ai_hair_length_detection.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with metric rows, an overall summary, care guidance, and a non-medical disclaimer; helper commands return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a YouCam API key, selected metrics, and appropriate hair photos; density and length use one photo, while type and frizziness use front, right, and left photos.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
