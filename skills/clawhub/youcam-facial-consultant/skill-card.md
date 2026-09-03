## Description:

Analyze skin tone and facial attributes from a single selfie using YouCam (Perfect Corp) AI, returning skin, eye, eyebrow, lip, and hair colors plus facial feature shapes and golden-ratio proportions as a readable report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze a clear, front-facing selfie for skin-tone colors, facial feature labels, and approximate facial proportions. It is intended for reference-style facial analysis reports, not skin-condition scoring, makeup or hair try-on, medical assessment, or cosmetic-surgery advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selfie images to YouCam/Perfect Corp for analysis.

Mitigation: Use it only when the user is comfortable sharing the selfie with YouCam/Perfect Corp, and process only a clear, front-facing JPEG selfie as documented.

Risk: The helper exposes broader inputs and parameters than the written skill instructions clearly limit.

Mitigation: Keep execution to the documented skin-tone-analysis and face-attr-analysis commands, avoid age and gender parameters, and avoid URL or video inputs unless reviewed.

Risk: A plaintext credentials.json file can store the YouCam API key.

Mitigation: Prefer the YOUCAM_API_KEY environment secret and avoid committing or sharing credentials.json.

Risk: Facial proportion and attribute results can vary with lighting, pose, and repeated API runs.

Mitigation: Label ratios as approximate, skip missing values, do not infer unsupported undertones, and include the documented non-medical, non-cosmetic-surgery disclaimer.

## Reference(s):

- [Facial Consultant interpretation guide](references/guide.md)
- [YouCam AI Skin Tone Analysis API](https://docs.perfectcorp.com/reference/ai_skin_tone_analysis.md)
- [YouCam AI Face Analyzer API](https://docs.perfectcorp.com/reference/ai_face_analyzer.md)
- [ClawHub skill page](https://clawhub.ai/youcam-api/skills/youcam-facial-consultant)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with optional inline shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should include returned colors only, label facial ratios as approximate, skip missing values, and end with the documented AI-analysis disclaimer.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
