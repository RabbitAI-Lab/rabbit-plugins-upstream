## Description:

Guides agents through the OneKey/Craftsman toy generation APIs to create multi-view toy reference sheets, launch 3D model generation tasks, and retrieve generated model previews and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate toy design drafts and multi-view sheets, create 3D model generation tasks, and poll for outputs such as GLB models and preview images through the OneKey/Craftsman gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation prompts, image URLs, returned assets, and share URLs are sent to an external OneKey/Craftsman gateway and downstream 3D providers.

Mitigation: Avoid sending secrets, regulated data, or private unreleased assets unless approved for those services; treat returned share URLs and asset URLs as sensitive.

Risk: The skill requires the DEEPNLP_ONEKEY_ROUTER_ACCESS key for gateway access.

Mitigation: Keep the access key in a secret manager or local environment variable, do not commit it to files or logs, and rotate it if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ai-hub-admin/skills/figurine-generator)
- [Craftsman 3D Generator](https://craftsman-agent.aiagenta2z.com/app/3d-generator)
- [Craftsman website](https://craftsman-agent.aiagenta2z.com)
- [OneKey workspace keys](https://deepnlp.org/workspace/keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown with curl and npx command examples plus JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces task IDs, share URLs, generated image URLs, model URLs, preview URLs, task progress, and provider metadata when API calls succeed.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
