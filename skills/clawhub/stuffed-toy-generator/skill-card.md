## Description:

Generates toy design drafts, multi-view reference sheets, and 3D model generation workflows from text and image prompts through OneKey Agent Gateway APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative tool builders use this skill to guide agents through generating toy concept sheets, creating 3D model generation tasks, and polling for printable or previewable toy assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Toy prompts, image URLs, task metadata, and generated outputs are sent to OneKey Agent Gateway and downstream 3D providers.

Mitigation: Use only data appropriate for those remote services, and avoid confidential, personal, regulated, or proprietary inputs unless provider privacy and retention terms have been reviewed.

Risk: The skill requires an API access key for the OneKey Agent Gateway.

Mitigation: Store the DEEPNLP_ONEKEY_ROUTER_ACCESS value in the agent runtime environment and avoid placing real keys in prompts, logs, examples, or committed files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ai-hub-admin/skills/stuffed-toy-generator)
- [OneKey Agent Gateway endpoint](https://agent.deepnlp.org/agent_router)
- [Craftsman 3D Generator](https://craftsman-agent.aiagenta2z.com/app/3d-generator)
- [Craftsman Agent website](https://craftsman-agent.aiagenta2z.com)
- [OneKey Gateway access keys](https://deepnlp.org/workspace/keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, json]

**Output Format:** [Markdown guidance with curl and npx command examples plus JSON request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a DEEPNLP_ONEKEY_ROUTER_ACCESS key and sends prompts, image URLs, task metadata, and generated outputs to remote services.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
