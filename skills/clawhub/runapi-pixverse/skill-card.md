## Description:

Create, edit, transition, and extend PixVerse V6 videos through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to generate, edit, transition, or extend PixVerse videos through RunAPI from text, images, references, transitions, or completed tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use RunAPI authentication and upload selected media inputs for remote PixVerse generation.

Mitigation: Review the generated request and selected local media paths before submission; use environment or saved CLI authentication, and use browser login only when explicitly requested.

Risk: Submitting a PixVerse task can incur paid task charges.

Mitigation: Submit exactly once, preserve the task response, and retry only under the bounded recovery conditions described by the skill.

Risk: A mismatch between installed CLI help and the current API reference can produce invalid requests or unverifiable outputs.

Mitigation: Discover the installed operation contract and API reference before building the request, and stop on contract mismatch instead of guessing.

## Reference(s):

- [ClawHub PixVerse skill page](https://clawhub.ai/runapi-ai/skills/runapi-pixverse)
- [RunAPI PixVerse model page](https://runapi.ai/models/pixverse)
- [RunAPI PixVerse model documentation](https://runapi.ai/models/pixverse.md)
- [RunAPI PixVerse provider overview](https://runapi.ai/providers/pixverse.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI PixVerse SDK integration](https://github.com/runapi-ai/pixverse-sdk)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, JSON, Files]

**Output Format:** [Markdown guidance with shell commands, JSON request and response files, and downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce PixVerse video deliverables after authenticated RunAPI task execution and response verification.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
