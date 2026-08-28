## Description:

Generates toy design drafts and 3D toy model tasks through the OneKey/Craftsman Agent Gateway for figurines, stuffed toys, 3D-printing assets, game assets, and architecture toys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users use this skill to call Toy Generator APIs that produce multi-view toy design drafts, start 3D model generation jobs, and poll for model and preview outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, image URLs, and generated toy assets are sent to the OneKey/Craftsman remote service and downstream generation providers.

Mitigation: Use the skill only with data suitable for those remote services and avoid submitting confidential or sensitive assets.

Risk: Access keys and share URLs can expose service access or private generation results.

Mitigation: Keep DEEPNLP_ONEKEY_ROUTER_ACCESS and share_url values private, especially links containing pwd or other key-like parameters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ai-hub-admin/skills/toy-generator)
- [Craftsman 3D Generator Online](https://craftsman-agent.aiagenta2z.com/app/3d-generator)
- [Craftsman Website](https://craftsman-agent.aiagenta2z.com)
- [OneKey Agent Gateway endpoint](https://agent.deepnlp.org/agent_router)
- [OneKey API keys workspace](https://deepnlp.org/workspace/keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with REST and CLI examples; remote API responses are JSON containing image, model, preview, task, and share URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DEEPNLP_ONEKEY_ROUTER_ACCESS; remote generation can return private share_url values and 3D model or preview URLs.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
