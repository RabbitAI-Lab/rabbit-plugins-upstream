## Description:

Diagnose hair-health metrics--density, type, frizziness, and length--from selfie photos using YouCam (Perfect Corp) AI, then return one combined report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to request selected hair-health detections from YouCam APIs, confirm credit cost before execution, and receive a concise hair metrics report with non-medical care guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hair and selfie photos are sent to YouCam/Perfect Corp APIs for processing.

Mitigation: Use the skill only when the user consents to sending the selected images to the third-party service, and prefer trusted local image files.

Risk: Selected API detections may spend account credits.

Mitigation: Check and disclose the per-feature cost first, then run only the metrics the user confirms.

Risk: An API key can be stored in credentials.json.

Mitigation: Prefer the YOUCAM_API_KEY environment variable and avoid committing or sharing credential files.

Risk: Hair analysis results could be mistaken for medical advice.

Mitigation: Keep the output non-medical and include the required note that results are AI-based, for reference only, and not a diagnosis or treatment.

Risk: The generic helper supports arguments outside the hair-diagnostics workflow.

Mitigation: Use only the documented hair-density, hair-type, hair-frizziness, and hair-length features for this skill.

## Reference(s):

- [Hair Diagnostics interpretation guide](references/guide.md)
- [AI Hair Density Detection API](https://docs.perfectcorp.com/reference/ai_hair_density_detection.md)
- [AI Hair Type Detection API](https://docs.perfectcorp.com/reference/ai_hair_type_detection.md)
- [AI Hair Frizziness Detection API](https://docs.perfectcorp.com/reference/ai_hair_frizziness_detection.md)
- [AI Hair Length Detection API](https://docs.perfectcorp.com/reference/ai_hair_length_detection.md)
- [ClawHub skill page](https://clawhub.ai/youcam-api/skills/youcam-hair-diagnostics)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with selected metric rows, plain-language notes, care guidance, and JSON from API helper commands when executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill asks which metrics to run, checks feature costs first, and skips missing API metrics instead of filling them in.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
