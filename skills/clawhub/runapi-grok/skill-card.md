## Description:

Call Grok 4.6 through RunAPI Responses only; use Grok 4.3, 4.5, or Grok 4.20 non-reasoning through their verified OpenAI-compatible interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call supported Grok models through RunAPI with the appropriate OpenAI-compatible protocol, model identifier, credential setup, streaming behavior, tool constraints, and response verification steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, and model requests may be sent to RunAPI when the skill is used.

Mitigation: Confirm RunAPI is an approved destination for the data and use a scoped RunAPI key for Grok access.

Risk: Incorrect model, protocol, or request shape can produce rejected or misleading integration behavior.

Mitigation: Use the exact model and protocol documented for the workflow, verify terminal usage and completion fields, and stop after the documented bounded retry or shape correction.

## Reference(s):

- [RunAPI Grok model documentation](https://runapi.ai/models/grok.md)
- [RunAPI xAI provider documentation](https://runapi.ai/providers/xai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Grok homepage](https://runapi.ai/models/grok)
- [Grok compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Python examples, environment variable setup, protocol guidance, and validation checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires RunAPI credentials and endpoint configuration; no executable automation is included in the artifact.]

## Skill Version(s):

0.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
