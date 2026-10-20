## Description:

Analyzes hair photos with YouCam AI for selected density, type, frizziness, and length metrics, then combines the results into a non-medical report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking hair-care insights can use an assistant to assess selected hair metrics from photos and receive a combined report with gentle care suggestions. Density and length use one photo; type and frizziness require three angles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hair and selfie images are sent to Perfect Corp/YouCam for analysis.

Mitigation: Share photos only with the user's informed consent and avoid sending images the user does not want processed by the service.

Risk: Running detections can spend API credits; starting a task again while it is pending may incur another charge.

Mitigation: Explain per-metric costs and get the user's selection before running; check the existing task status instead of restarting it.

Risk: Saving the API key in a local credentials file can expose it.

Mitigation: Prefer setting YOUCAM_API_KEY through the environment or a secret manager.

Risk: Photo quality or incomplete angles may affect results, which are not medical diagnoses.

Mitigation: Request three angle photos for type and frizziness, follow the density pose guidance, and direct hair-loss or scalp concerns to a dermatologist.

## Reference(s):

- [Hair Diagnostics interpretation guide](references/guide.md)
- [YouCam AI hair density detection documentation](https://docs.perfectcorp.com/reference/ai_hair_density_detection.md)
- [YouCam AI hair type detection documentation](https://docs.perfectcorp.com/reference/ai_hair_type_detection.md)
- [YouCam AI hair frizziness detection documentation](https://docs.perfectcorp.com/reference/ai_hair_frizziness_detection.md)
- [YouCam AI hair length detection documentation](https://docs.perfectcorp.com/reference/ai_hair_length_detection.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with selected metric results, a summary, care directions, and a non-medical disclaimer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Omits unavailable metrics; results depend on photo quality and pose.]

## Skill Version(s):

1.1.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
