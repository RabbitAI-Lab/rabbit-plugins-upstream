## Description:

Generates sound effects and voice-over audio for videos by submitting and querying mmaudio jobs on api.a7w.cn with a user-provided API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and content production teams use this skill to configure an a7w API key, submit video-to-audio generation jobs, and query asynchronous task results for generated audio or dubbed video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can use the user's paid a7w API key and account points for broader marketplace calls than the audio-only purpose suggests.

Mitigation: Review the client before installation, run only the intended mmaudio commands, monitor point usage, and use a scoped or disposable key when available.

Risk: Changing A7W_HOST or passing --host can send the API key and request data to a different service.

Mitigation: Leave the host at the default api.a7w.cn unless the destination is explicitly trusted.

Risk: Submitted media URLs and prompts are sent to a third-party platform for processing.

Mitigation: Do not submit private, proprietary, or regulated media unless the platform's data handling and contractual terms are acceptable.

Risk: Asynchronous submissions may consume account points, and repeated submissions can create duplicate charges.

Mitigation: Use --no-wait only when task tracking is planned, query existing task IDs instead of resubmitting, and review returned point costs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/2253128/skills/sanjianke-mmaudio)
- [Publisher Profile](https://clawhub.ai/user/2253128)
- [Getting Started](artifact/references/getting-started.md)
- [Submit API Reference](artifact/references/api-submit.md)
- [Query API Reference](artifact/references/api-query.md)
- [General Usage Notes](artifact/references/通用说明.md)
- [a7w API Platform](https://api.a7w.cn/)
- [AI Plugin Market](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled client emits JSON to stdout and human-readable status messages to stderr.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
