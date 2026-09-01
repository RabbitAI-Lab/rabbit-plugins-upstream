## Description:

This skill helps agents guide ecommerce teams and content creators through generating HappyHorse 1.1 product marketing videos with qhkit, including model selection, media upload, task status checks, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand product teams, live-commerce teams, and commercial content creators use this skill to prepare and run product-display, advertising, and social commerce video generation workflows through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or upgrade the external qhkit package.

Mitigation: Install only after confirming that the qhkit package and Qinghu AI service are trusted for the environment.

Risk: API keys could be exposed if pasted into chat.

Mitigation: Use a secure environment variable or platform-managed secret instead of sharing credentials in conversation.

Risk: Local image, video, or audio references may be uploaded to Qinghu or related storage for generation.

Mitigation: Review media sensitivity and obtain appropriate approval before using the skill with local assets.

Risk: Video generation can consume paid credits.

Mitigation: Review the estimated credit cost and require explicit approval before submitting generation tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-happyhorse-sales)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce task IDs, status summaries, cost estimates, and generated video URLs from the qhkit service.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
