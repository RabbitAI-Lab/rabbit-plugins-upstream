## Description:

Recommend a hairstyle and hair color based on the user's face shape and skin tone, then preview them with YouCam (Perfect Corp) AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze a clear front-facing selfie, recommend hairstyle and color options, and generate YouCam try-on previews after the user confirms the desired paid generation path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends selfies and hair try-on inputs to YouCam/Perfect Corp APIs.

Mitigation: Use only user-approved images or trusted URLs, and limit analysis parameters to what the hair recommendation requires.

Risk: The skill requires a YouCam API key.

Mitigation: Store the key securely and prefer the YOUCAM_API_KEY environment variable over credentials.json.

Risk: Generation can spend API credits.

Mitigation: Check and disclose feature costs before generation, then run only the restyle, recolor, or combined path the user approves.

Risk: AI hair previews may not match real salon results.

Mitigation: Keep the required preview disclaimer and recommend consulting a professional stylist for coloring decisions.

## Reference(s):

- [Hair Color & Style Advisor recommendation guide](references/guide.md)
- [Perfect Corp AI Face Analyzer API](https://docs.perfectcorp.com/reference/ai_face_analyzer.md)
- [Perfect Corp AI Skin Tone Analysis API](https://docs.perfectcorp.com/reference/ai_skin_tone_analysis.md)
- [Perfect Corp AI Hairstyle API](https://docs.perfectcorp.com/reference/ai_hairstyle.md)
- [Perfect Corp AI Hair Color API](https://docs.perfectcorp.com/reference/ai_hair_color.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with command examples, recommendation rationale, and an exact result image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to disclose credit costs before generation and to keep the final AI-generated preview note.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
