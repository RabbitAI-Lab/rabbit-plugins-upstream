## Description:

Generate and remix images with Flux 2 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent create or transform Flux 2 images through RunAPI for one-off outputs, or to integrate Flux 2 requests with SDKs in applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit billable RunAPI image generation jobs.

Mitigation: Authenticate deliberately, submit each request once, preserve the task id, and do not submit replacement paid requests without user authorization.

Risk: Requested local media inputs may be uploaded to RunAPI.

Mitigation: Only place user-intended local media paths in request.json and validate inputs before execution.

Risk: The installed CLI contract and online API reference may disagree or omit required request details.

Mitigation: Discover the installed command help and API reference before building the request, and stop on mismatches or unresolved contract gaps.

## Reference(s):

- [RunAPI Flux 2 model page](https://runapi.ai/models/flux-2)
- [RunAPI Flux 2 model documentation](https://runapi.ai/models/flux-2.md)
- [Black Forest Labs provider overview](https://runapi.ai/providers/black-forest-labs.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Flux 2 SDK integration](https://github.com/runapi-ai/flux-2-sdk)
- [ClawHub skill listing](https://clawhub.ai/runapi-ai/skills/runapi-flux-2)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with shell commands, JSON request and result files, optional SDK code, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the RunAPI CLI for one-off generation and SDK references for application integration; expected media output family is image/*.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
