## Description:

Connects an AI agent to Sogni workflows for generating and editing images, video, and music, with support for related creative media tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

Creative users and developers can ask an AI agent to create or edit media through Sogni, and to manage reference assets and saved creative preferences. The agent uses the skill's guidance and command workflows to carry out those requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, voice clips, or other reference media may be processed remotely.

Mitigation: Do not use the skill for media that must stay on-device, and approve which photos and voice clips may be processed remotely.

Risk: Generation can incur costs, and publication may be immutable.

Mitigation: Set spending limits and require approval before immutable publication.

Risk: Replay JSON may contain secrets when ingested.

Mitigation: Remove secrets from replay JSON before ingestion.

Risk: External installers, dependencies, and server behavior have not been fully verified.

Mitigation: Review installers and dependencies and verify service behavior before relying on the skill for sensitive workflows.

## Reference(s):

- [Sogni Creative Agent on ClawHub](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI](https://sogni.ai)
- [Sogni hosted MCP documentation](https://docs.sogni.ai/agents/mcp/)
- [Sogni Creative Agent npm package](https://www.npmjs.com/package/@sogni-ai/sogni-creative-agent-skill)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Creative media files]

**Output Format:** [Natural language guidance, CLI commands, and generated media files such as images, video, audio, and 3D assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media outputs are saved to the user's working directory; some workflows send prompts and reference media to Sogni for remote processing.]

## Skill Version(s):

3.65.1 (source: CHANGELOG, released 2026-11-05; ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
