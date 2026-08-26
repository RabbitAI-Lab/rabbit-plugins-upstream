## Description:

Generates toy and game asset design drafts, multi-view sheets, and 3D model tasks through Craftsman Agent APIs served by the OneKey Agent Gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative technical users use this skill to draft toy or game asset concepts, create 3D generation tasks, and poll for generated model and preview outputs. It is suited for figurines, stuffed toys, 3D-printing assets, game assets, and architecture toy workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, image URLs, session metadata, and generated assets may be sent to the OneKey Gateway and downstream 3D model providers.

Mitigation: Use only approved non-confidential content unless that external data sharing has been reviewed and authorized.

Risk: The DEEPNLP_ONEKEY_ROUTER_ACCESS key is required for API access and could be exposed if embedded in shared commands, logs, or files.

Mitigation: Store the key as a secret, pass it through the environment, and avoid committing or pasting real key values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ai-hub-admin/skills/game-asset-generator)
- [OneKey Agent Gateway endpoint](https://agent.deepnlp.org/agent_router)
- [Craftsman 3D Generator Online](https://craftsman-agent.aiagenta2z.com/app/3d-generator)
- [Craftsman website](https://craftsman-agent.aiagenta2z.com)
- [AI Agent Marketplace keys](https://deepnlp.org/workspace/keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with curl, npx, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When executed, the documented APIs can return image URLs, task IDs, progress status, preview URLs, and downloadable 3D model URLs.]

## Skill Version(s):

1.0.0 (source: release metadata and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
