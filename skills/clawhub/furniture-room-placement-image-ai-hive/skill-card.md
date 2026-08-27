## Description:

This skill helps furniture, interior design, e-commerce, and styling teams turn furniture room-placement requests into a Chinese production workflow with visual briefs, image prompts, runnable AI-HIVE generation commands, and delivery checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, furniture brands, interior designers, e-commerce teams, and soft-furnishing teams use this skill to plan and generate furniture placement previews for marketing, ads, product pages, and social content. It guides users through authorized inputs, style and layout choices, AI-HIVE image generation, task tracking, and review of sizing, claims, and authenticity risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires an AI-HIVE API key, creating a credential exposure risk if keys are pasted into scripts, logs, screenshots, or committed files.

Mitigation: Use environment variables or the local config flow, keep placeholders in shared examples, and review generated files and logs before sharing.

Risk: The workflow can upload user-selected reference images and other media to AI-HIVE, which may include rights-sensitive or private material.

Mitigation: Confirm the user has rights to the input media before upload and avoid using protected logos, likenesses, copyrighted scenes, or private material without authorization.

Risk: Generation requests may spend AI-HIVE credits, especially when batch generation or repeated retries are used.

Mitigation: Review prompts, routing mode, batch size, model choice, and pricing snapshot before execution; start with small batches.

Risk: Generated furniture placement images may be visually plausible while still misrepresenting product dimensions, construction feasibility, claims, availability, or platform performance.

Mitigation: Mark uncertain facts for review, require human measurement or source verification for dimensions and claims, and avoid promises about sales, ranking, approval, or return on investment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/furniture-room-placement-image-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON artifacts and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce blueprint JSON files, AI-HIVE task records, downloaded generated media, and checklist-style review guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
