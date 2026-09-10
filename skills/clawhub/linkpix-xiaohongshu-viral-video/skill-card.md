## Description:

Helps agents plan and run Xiaohongshu-focused product video generation through qhkit, including model discovery, prompt shaping, cost estimation, paid job submission, status polling, and delivery guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce operators, and marketers use this skill to prepare Xiaohongshu product, seeding, and paid-placement short videos from prompts and uploaded media. The skill guides an agent through qhkit setup, model selection, image-to-video or storyboard workflows, estimates, explicit user confirmation, generation, polling, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update third-party qhkit and Node.js tooling in the local environment.

Mitigation: Use a disposable or contained environment where possible, review installation commands before execution, and prefer pinned or reviewed tooling for production workflows.

Risk: The workflow handles reusable Qinghu API credentials.

Mitigation: Configure credentials out of band or through environment variables, use limited tokens with spending controls, and avoid exposing secrets in prompts, logs, or shared transcripts.

Risk: Selected local images or video references may be uploaded to remote services for generation.

Mitigation: Use only media that is approved for upload, remove sensitive content before submission, and confirm the exact files included in each generation request.

Risk: Generation jobs may consume paid credits and cannot be canceled after submission.

Mitigation: Run estimates where supported, present model, duration, media, language, orientation, and estimated credits to the user, and submit only after explicit confirmation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-xiaohongshu-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, cost estimates, status updates, generated video URLs, and credential setup guidance.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
