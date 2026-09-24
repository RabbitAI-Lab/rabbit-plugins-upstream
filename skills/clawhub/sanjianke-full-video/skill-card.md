## Description:

This skill helps agents submit and query a7w full_video jobs for text-to-video, first/last-frame video, and multimodal reference video generation using the user's api.a7w.cn API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to prepare requests, run shell commands, and parse JSON responses for a7w full_video video generation workflows. It supports task submission, asynchronous polling, and task-result lookup for generated video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included client can use the user's API key against arbitrary a7w apps, not only the documented full_video APIs.

Mitigation: Use the skill for the documented full_video submit and query endpoints unless the broader a7w app access has been separately reviewed.

Risk: The client accepts a caller-supplied host through --host or A7W_HOST, which can redirect where the API key is sent.

Mitigation: Do not set --host or A7W_HOST unless the destination is fully trusted; use the default api.a7w.cn host for normal operation.

Risk: Calls can spend points from the user's a7w account and repeated asynchronous submissions can create additional charges.

Mitigation: Use an API key with an acceptable spending limit, validate parameters before submitting, and avoid resubmitting the same generation task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-full-video)
- [Submit API reference](references/api-submit.md)
- [Query API reference](references/api-query.md)
- [Getting started](references/getting-started.md)
- [General usage notes](references/通用说明.md)
- [a7w API marketplace](https://api.a7w.cn/)
- [a7w plugin marketplace](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled client prints JSON to stdout and human-readable status messages to stderr.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
