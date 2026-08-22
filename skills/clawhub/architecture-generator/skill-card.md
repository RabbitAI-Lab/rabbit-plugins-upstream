## Description:

Architecture Generator helps agents create toy design drafts, multi-view sheets, and 3D model generation tasks through the OneKey Agent Gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and 3D asset creators use this skill to guide agents through creating toy reference sheets, launching 3D model generation jobs, and polling for generated model and preview outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, and design requests are sent to the OneKey gateway and downstream generation providers.

Mitigation: Use only inputs approved for external processing, and avoid secrets, private personal data, or confidential proprietary designs unless organizational policy allows it.

Risk: API calls require a registered OneKey access key.

Mitigation: Provide the key through DEEPNLP_ONEKEY_ROUTER_ACCESS and avoid embedding it in prompts, shared files, logs, or copied command examples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ai-hub-admin/skills/architecture-generator)
- [AI-Hub-Admin publisher profile](https://clawhub.ai/user/ai-hub-admin)
- [OneKey Agent Gateway endpoint](https://agent.deepnlp.org/agent_router)
- [Craftsman 3D Generator](https://craftsman-agent.aiagenta2z.com/app/3d-generator)
- [Craftsman Agent website](https://craftsman-agent.aiagenta2z.com)
- [OneKey access keys](https://deepnlp.org/workspace/keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON, files]

**Output Format:** [Markdown guidance with REST and CLI commands plus JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses can include generated image URLs, task IDs, task progress, downloadable GLB model URLs, preview image URLs, and generation metadata.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
