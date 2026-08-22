## Description:

Generates customizable icon, poster, and carousel image assets from prompts, templates, styles, and optional reference images through the Craftsman image-generation service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate editable icon, poster, and carousel image assets from text prompts, style settings, asset dimensions, and optional reference images. It provides API and CLI usage patterns for invoking a remote image-generation service and retrieving generated image URLs, share links, and page-layer data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded or reference images, design configuration, and generated outputs are sent to documented third-party services.

Mitigation: Avoid submitting secrets, private business material, personal data, or confidential images unless the organization has approved the service and its data handling.

Risk: The skill depends on a OneKey Gateway access key for remote API use.

Mitigation: Provide the access key only through the documented environment variable and avoid embedding credentials in prompts, command history, or shared examples.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ai-hub-admin/skills/icon-designer)
- [Publisher Profile](https://clawhub.ai/user/ai-hub-admin)
- [Craftsman Image Generator Console](https://craftsman-agent.aiagenta2z.com/app/image-generator)
- [Craftsman Website](https://craftsman-agent.aiagenta2z.com)
- [OneKey Router API Endpoint](https://agent.deepnlp.org/agent_router)
- [OneKey Access Key Workspace](https://deepnlp.org/workspace/keys)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance, Image assets]

**Output Format:** [Markdown with inline bash and curl examples plus JSON request and response structures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated service responses include session identifiers, share URLs, image URLs, page counts, and editable page-layer data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
