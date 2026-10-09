## Description:

Helps agents analyze a reference ad into shots and prompts, then create a similarly structured video or preview an editable draft before generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creators use this skill to analyze the structure of an existing ad and generate a new video with optional dialogue and subject edits. They can also request an analysis without generating a video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference media and prompts are sent to AdsTurbo, and local media uploads may yield publicly accessible URLs.

Mitigation: Upload only media approved for external processing and URL-based access; avoid sensitive material.

Risk: Submitting a generation task can spend AdsTurbo credits.

Mitigation: Review the draft preview and quoted cost, then submit only after user approval.

Risk: The skill requires an AdsTurbo API key.

Mitigation: Keep the key in the environment and do not include it in replies or shared materials.

## Reference(s):

- [AdsTurbo Ad Video Clone release](https://clawhub.ai/adsturbo/skills/adsturbo-ad-clone)
- [Ad Clone workflow](references/ad_clone.md)
- [Media upload guidance](references/upload.md)
- [Task status guidance](references/work.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with analysis, draft options, cost quotes, and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation is asynchronous; analysis can be requested without generation.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
