## Description:

Analyzes a single selfie with YouCam (Perfect Corp) AI and returns skin-condition scores, skin type, and a readable report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to request a skin report from a clear, front-facing, single-person selfie. The skill guides collection of analysis tier, concerns, and image output style, then produces a non-diagnostic report based on returned YouCam scores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads face or selfie data to YouCam/Perfect Corp for analysis.

Mitigation: Use it only with appropriate user authorization, process the intended single local selfie, and review the provider's privacy and retention terms before handling sensitive images.

Risk: API credentials may be supplied through a local credentials.json file.

Mitigation: Prefer the YOUCAM_API_KEY environment variable, keep credential files out of shared artifacts, and rotate keys if exposure is suspected.

Risk: The bundled runner can accept broader inputs than the skin-analysis flow requires, including URLs, video extensions, and multiple source or reference files.

Mitigation: For this skill, restrict use to one local jpg, jpeg, or png selfie and avoid URL, video, reference-file, or batch inputs unless separately reviewed.

Risk: Skin scores could be mistaken for medical advice.

Mitigation: Keep the required non-diagnostic disclaimer, avoid medical claims, and direct users with skin-health concerns to a dermatologist.

## Reference(s):

- [Perfect Corp AI Skin Analysis API documentation](https://docs.perfectcorp.com/reference/ai_skin_analysis.md)
- [YouCam API console](https://yce.perfectcorp.com/api-console)
- [Skin Analysis interpretation](references/interpretation.md)
- [Skin Analysis report format](references/output-format.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report assembled from JSON API results, with scores, star ratings, advice, optional result image references, and a required disclaimer.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses returned ui_score values only, reports up to 16 skin concerns plus skin type, and requires clear retake guidance when the API rejects the photo.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
