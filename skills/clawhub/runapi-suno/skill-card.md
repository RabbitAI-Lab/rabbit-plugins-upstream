## Description:

Generate and transform music or compose lyrics with Suno through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create, extend, transform, or verify music and audio deliverables with Suno through RunAPI. Agents use it to discover the current operation contract, build valid requests, run tasks through the CLI or SDK, and verify returned media before reporting completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to RunAPI or Suno.

Mitigation: Review request files before submission and provide a RunAPI API key only in trusted environments.

Risk: Generation tasks may incur paid usage or create asynchronous jobs.

Mitigation: Submit each task once, preserve task evidence, and require user authorization before replacing failed paid requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-suno)
- [RunAPI Suno Homepage](https://runapi.ai/models/suno)
- [Suno Model Overview](https://runapi.ai/models/suno.md)
- [Suno Provider Overview](https://runapi.ai/providers/suno.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)
- [RunAPI Suno SDK](https://github.com/runapi-ai/suno-sdk)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce request JSON, task identifiers, result files, downloaded audio deliverables, SDK integration code, and verification notes.]

## Skill Version(s):

0.4.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
