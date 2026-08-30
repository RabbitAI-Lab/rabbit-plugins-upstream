## Description:

Generates toy design drafts, multi-view reference sheets, and 3D model tasks through the Craftsman Agent APIs served by OneKey Agent Gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to generate stuffed-toy or figurine concepts, create 3D generation tasks, and poll for model and preview outputs. It supports text and image prompts, multi-view references, and toy-oriented templates such as stuffed toys, figurines, game assets, architecture toys, and 3D printing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Toy prompts, image URLs, and generation metadata are sent to OneKey Agent Gateway and downstream 3D providers.

Mitigation: Use the skill only for data that can be shared with those external services, and avoid submitting sensitive or confidential prompts, images, or metadata.

Risk: The DEEPNLP_ONEKEY_ROUTER_ACCESS key is required to call the gateway and could be exposed through shared chats, logs, or command history.

Mitigation: Keep the key in a local environment variable or secret store, avoid pasting real keys into shared contexts, and rotate the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ai-hub-admin/skills/stuffed-toy-generator)
- [Craftsman 3D Generator](https://craftsman-agent.aiagenta2z.com/app/3d-generator)
- [Craftsman Agent website](https://craftsman-agent.aiagenta2z.com)
- [OneKey Agent Gateway endpoint](https://agent.deepnlp.org/agent_router)
- [OneKey API key workspace](https://deepnlp.org/workspace/keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON, Configuration]

**Output Format:** [Markdown guidance with curl and CLI command examples plus JSON request and response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include generated image URLs, task IDs, status updates, share URLs, 3D model URLs, and preview URLs returned by external services.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
