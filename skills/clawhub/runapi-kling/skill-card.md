## Description:

Generate and edit video with Kling through RunAPI for one-off CLI generation or SDK-based application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to guide agents through Kling video generation or editing with RunAPI, including contract discovery, request construction, task execution, result verification, and SDK integration when building applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media paths placed in requests may be uploaded to RunAPI.

Mitigation: Confirm user intent for any local media input, validate paths before submission, and use separate file upload only when the discovered contract or user need requires it.

Risk: RunAPI API authentication may be used or stored by the CLI.

Mitigation: Prefer environment authentication or saved CLI configuration, avoid exposing API keys in outputs, and use interactive browser login only when explicitly requested.

Risk: Submitted Kling generation tasks may incur provider costs.

Mitigation: Submit a task once, preserve task evidence, and avoid replacement or paid retries unless the user authorizes them or evidence confirms no task and no billing occurred.

Risk: Contract mismatch or incomplete result verification can produce invalid requests or incomplete deliverables.

Mitigation: Treat installed CLI help and current API reference as authoritative, stop on unresolved mismatches, and verify each returned media deliverable is non-empty and has the expected MIME type.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-kling)
- [RunAPI Kling model overview](https://runapi.ai/models/kling)
- [RunAPI Kling documentation](https://runapi.ai/models/kling.md)
- [Kuaishou provider overview](https://runapi.ai/providers/kuaishou.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Kling SDK](https://github.com/runapi-ai/kling-sdk)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Code, Files]

**Output Format:** [Markdown guidance with shell commands and JSON request or result artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce downloaded video files and preserved task/result JSON when the agent executes RunAPI operations.]

## Skill Version(s):

0.2.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
