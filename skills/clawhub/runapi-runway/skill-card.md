## Description:

Generate or extend videos with Runway through RunAPI. Use the RunAPI CLI for one-off results and an SDK when integrating Runway into an app, backend, worker, library, or production codebase.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create or extend Runway videos through RunAPI, either as one-off CLI tasks or SDK-backed application integrations. The skill guides contract discovery, request construction, task execution, result download, and deliverable verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected media files may be sent to RunAPI or Runway.

Mitigation: Use a dedicated API key where possible and review request.json before submission for sensitive content or file paths.

Risk: Submitting generation tasks may create billable work.

Mitigation: Submit only after authentication and request validation, and do not create replacement paid tasks without user authorization.

Risk: Incomplete or unexpected media results could be mistaken for finished deliverables.

Mitigation: Download every requested media output and verify each file is non-empty with the expected MIME type before reporting completion.

## Reference(s):

- [RunAPI Runway model overview](https://runapi.ai/models/runway.md)
- [RunAPI Runway provider overview](https://runapi.ai/providers/runway.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Runway homepage](https://runapi.ai/models/runway)
- [RunAPI Runway SDK](https://github.com/runapi-ai/runway-sdk)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request and response files, SDK integration code, and downloaded media deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the runapi CLI for CLI workflows and may use RUNAPI_API_KEY authentication.]

## Skill Version(s):

0.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
