## Description:

Analyze skin tone and facial attributes from a single selfie using YouCam (Perfect Corp) AI, returning color, feature-shape, and facial-proportion information as a readable report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to request skin-tone, facial-feature, face-shape, and facial-proportion analysis from a clear single-person selfie. The skill helps produce a reference report and explicitly avoids skin-condition scoring, makeup try-on, hair try-on, medical assessment, and cosmetic-surgery assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends identifiable selfie images and derived facial attributes to Perfect Corp/YouCam.

Mitigation: Obtain clear user consent before use, use a dedicated YouCam API key, and avoid submitting images when third-party processing is not acceptable.

Risk: The helper can accept public URLs and broader local inputs, while the intended flow is a clear, front-facing single-person selfie.

Mitigation: Prefer local jpg/jpeg files, confirm the image meets the stated selfie requirements, and avoid public URL inputs unless the user understands the exposure.

Risk: The face-attribute API supports age and gender fields even though the skill's stated report does not require them.

Mitigation: Request only the declared color, feature-shape, and ratio fields, and avoid age or gender parameters.

Risk: The generic YouCam helper is broader than this skill's stated skin-tone and face-attribute workflow.

Mitigation: Restrict execution to the documented skin-tone-analysis and face-attr-analysis features and review parameters against the current Perfect Corp documentation before running.

## Reference(s):

- [Facial Consultant interpretation guide](artifact/references/guide.md)
- [Perfect Corp AI Skin Tone Analysis API](https://docs.perfectcorp.com/reference/ai_skin_tone_analysis.md)
- [Perfect Corp AI Face Analyzer API](https://docs.perfectcorp.com/reference/ai_face_analyzer.md)
- [ClawHub skill page](https://clawhub.ai/youcam-api/skills/youcam-facial-consultant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with JSON-backed API results and inline shell commands for setup, cost checks, and analysis runs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report includes color palette, feature summary, approximate facial-proportion buckets, and a required non-medical/non-surgical reference-only note.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
