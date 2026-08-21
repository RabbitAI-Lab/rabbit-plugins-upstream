## Description:

Figurine Generator helps agents call OneKey Gateway toy-generation APIs to draft multi-view toy reference sheets, create 3D generation tasks, and poll for model and preview outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate toy design drafts, multi-view reference sheets, 3D generation tasks, and final model or preview assets for figurines, stuffed toys, 3D printing, game assets, and architecture toys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, supplied image URLs, generation metadata, and API-key-authenticated requests are sent to the OneKey Gateway and external 3D generation providers.

Mitigation: Avoid confidential, personal, regulated, or proprietary reference images unless you have permission and understand the provider terms.

Risk: Generated reference sheets, previews, and 3D models may be unsuitable for the intended toy, printing, game, or architecture use without review.

Mitigation: Review generated assets, provider metadata, model file type, and preview output before reuse, publication, or production workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ai-hub-admin/skills/figurine-generator)
- [OneKey Agent Gateway Endpoint](https://agent.deepnlp.org/agent_router)
- [Craftsman 3D Generator](https://craftsman-agent.aiagenta2z.com/app/3d-generator)
- [OneKey Gateway Access Keys](https://deepnlp.org/workspace/keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files]

**Output Format:** [Markdown instructions with REST and CLI examples, plus JSON API responses containing generated image, preview, and model URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DEEPNLP_ONEKEY_ROUTER_ACCESS and sends prompts, image URLs, generation metadata, and API-key-authenticated requests to the OneKey Gateway and provider services.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
