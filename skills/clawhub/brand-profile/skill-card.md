## Description: <br>
Brand Profile helps an agent load or create a reusable brand profile that captures a business's identity, audience, voice, proof, guardrails, and operational defaults before social-media work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Social-media operators, agencies, creators, and business owners use this skill to establish or refresh a concise brand profile before generating captions, scripts, threads, calendars, or other social content. The profile gives downstream skills reusable context for voice, audience, positioning, proof, compliance guardrails, and synthetic-media defaults. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic onboarding or get-started requests may activate the skill when the user did not intend brand setup. <br>
Mitigation: Confirm that the task is about creating, loading, reviewing, or updating a brand profile before starting the interview. <br>
Risk: The generated brand-profile.md can contain private brand, client, proof, compliance, or synthetic-media policy details that downstream skills will reuse. <br>
Mitigation: Include only details intended for reuse in later social-media work, and avoid sensitive private information unless the user explicitly wants it stored in the profile. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/social-media-skills/skills/brand-profile) <br>
- [Voice](artifact/references/voice.md) <br>
- [Audience](artifact/references/audience.md) <br>
- [Positioning, Point of View, and Proof](artifact/references/positioning.md) <br>
- [Brand Profile Template](artifact/references/brand-profile-template.md) <br>
- [Examples](artifact/references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown file named brand-profile.md plus concise conversational summaries, questions, and edit guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The profile is intended as reusable local context for downstream social-media skills.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact frontmatter version: 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
