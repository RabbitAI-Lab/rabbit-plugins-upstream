## Description:

Wraps the a7w action_transfer API so an agent can submit a reference image and input video for motion transfer, then query the generated video result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to call the a7w action-transfer service with their own API key, public reference image URL, and public input video URL. It helps agents prepare API calls, submit asynchronous generation jobs, poll task status, and interpret the returned video result and usage data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can send the user's API key to a configurable host and can call APIs beyond the action-transfer endpoints.

Mitigation: Use only the default api.a7w.cn host unless you control the destination, avoid --host and A7W_HOST for normal use, and prefer a limited or disposable API key if available.

Risk: API calls can consume the user's a7w account points, especially when submitting longer videos or higher-quality modes.

Mitigation: Review mode, video duration, and returned frozen or actual point costs before repeated submissions.

Risk: Generated video content may raise consent, copyright, likeness, or policy concerns.

Mitigation: Use only media the user has rights to process and review generated results before publication or distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-action-transfer)
- [Getting started](references/getting-started.md)
- [Submit task API](references/api-submit.md)
- [Query task API](references/api-query.md)
- [General a7w plugin notes](references/通用说明.md)
- [a7w API marketplace](https://api.a7w.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided api.a7w.cn API key and public URLs for input media; submit calls are asynchronous and may consume account points.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
