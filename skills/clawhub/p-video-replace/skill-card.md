## Description:

Use when someone wants to swap a person, outfit, or product inside existing footage while keeping the camera move and audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators use this skill to prepare and run Pruna video replacement jobs that swap a person, outfit, or product into existing footage while preserving motion, camera behavior, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads source videos and reference identity images to a third-party API.

Mitigation: Use only media the operator has rights and consent to process, and treat uploaded media as leaving the local machine for Pruna's service.

Risk: The skill includes unpinned remote companion-skill installation commands.

Mitigation: Prefer pinned or reviewed companion-skill versions before installation instead of copying unpinned `npx ... -y` commands directly.

## Reference(s):

- [p-video-replace ClawHub page](https://clawhub.ai/pruna-ai/skills/p-video-replace)
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl command examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to collect a source video URL, one to four reference image URLs, prompt wording, resolution, target FPS, and Pruna API credentials before making API calls.]

## Skill Version(s):

1.0.12 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
