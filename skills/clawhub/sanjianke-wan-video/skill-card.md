## Description:

Creates and queries Wan video-generation tasks through the a7w API, including text-to-video, role/reference-image video, and video-edit workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to submit Wan video-generation jobs, poll task status, and retrieve generated video URLs using their own api.a7w.cn API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can access broader authenticated a7w marketplace capabilities beyond the advertised Wan workflow.

Mitigation: Use a dedicated, low-balance API key and avoid generic marketplace commands unless broader billable access is intended.

Risk: API keys and payment details could be exposed if shared in chat or stored in project files.

Mitigation: Use only an official a7w API key, keep it in the local config or A7W_API_KEY environment variable, and revoke or rotate it if exposed.

Risk: Changing the API host can send credentials to an unexpected endpoint.

Mitigation: Verify the configured host remains api.a7w.cn before login or task execution.

Risk: Repeated asynchronous task submissions can consume account points.

Mitigation: Submit once, track the returned task_id, poll for completion, and use --no-wait only when manual task tracking is planned.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-wan-video)
- [Getting started with a7w API keys](references/getting-started.md)
- [Wan create video task API](references/api-create.md)
- [Wan query video task API](references/api-query.md)
- [a7w compute marketplace](https://api.a7w.cn/)
- [a7w AI plugin marketplace](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task IDs, status JSON, generated video URLs, and local JSON files when an output path is requested.]

## Skill Version(s):

1.0.5 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
