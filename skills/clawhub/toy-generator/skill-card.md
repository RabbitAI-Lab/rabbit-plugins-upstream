## Description:

AI Generated Toy Models using SOTA 3D APIs such as Tripo/Meshy/etc served on OneKey Agent Gateway by Craftsman Agent, useful for AI Figurine, Stuffed Toy, 3D Printing, Game Asset and Architecture Toy Generation

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to draft toy designs, create 3D generation tasks, and poll generated model results through the OneKey Agent Gateway and Craftsman Agent toy workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Toy prompts, image URLs, generated assets, and task metadata are sent to the OneKey/Craftsman gateway and downstream providers such as Tripo or Meshy.

Mitigation: Submit only data approved for external processing, and review generated assets before reuse or publication.

Risk: The OneKey Gateway access key could be exposed through source control, logs, or shared shell history.

Mitigation: Store the access key outside source control, avoid logging it, and rotate it promptly if exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ai-hub-admin/skills/toy-generator)
- [Craftsman 3D Generator](https://craftsman-agent.aiagenta2z.com/app/3d-generator)
- [Craftsman Website](https://craftsman-agent.aiagenta2z.com)
- [OneKey Gateway Key Management](https://deepnlp.org/workspace/keys)
- [OneKey Agent Gateway Endpoint](https://agent.deepnlp.org/agent_router)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown with inline shell commands and JSON request/response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a OneKey Gateway access key and sends requests to external generation services.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
