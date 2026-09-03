## Description:

Use when someone wants one short video clip from text or images - B-roll, start/end frame animation, or a quick motion shot. Not for full multi-scene films or lip-synced hosts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creative operators use this skill to create one short p-video clip from text, first or last frame images, or an audio-conditioned scene anchor through Pruna's hosted video API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Pruna's hosted video API with a user-provided API key.

Mitigation: Use a dedicated PRUNA_API_KEY and install the skill only when Pruna API use is intended.

Risk: Image and audio inputs may be uploaded to the Pruna service.

Mitigation: Avoid uploading sensitive images or audio unless the user is comfortable sending those files to Pruna.

Risk: A paid or irreversible API call could be made with an unintended prompt or mode.

Mitigation: Show the drafted prompt and mode fields before POST when wording is not already locked, then proceed only with user-approved inputs.

## Reference(s):

- [ClawHub p-video skill page](https://clawhub.ai/pruna-ai/skills/p-video)
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash code blocks and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for one p-video prediction per invocation; uploaded audio controls clip length up to 20 seconds.]

## Skill Version(s):

1.0.10 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
