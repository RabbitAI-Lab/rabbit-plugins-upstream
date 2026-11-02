## Description:

product video, product demo video, product ad video, product showcase — turn a product's photos or link into a polished demo / ad video. Use when the user wants a product demo, showcase, or ad video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce teams use this skill to turn product photos, specifications, manuals, catalogs, or marketplace listings into product showcase, demo, and advertising videos, with multilingual voiceover and an optional virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product files are sent to dLazy, and attached files are uploaded to its media storage.

Mitigation: Send only content approved for this service; avoid including sensitive product or customer information.

Risk: The dLazy API key is saved in local CLI configuration, paid credits are used, and the external CLI package has not been fully audited.

Mitigation: Use the intended organization and project, protect the saved key, revoke it when no longer needed, and install only if comfortable with the service and its credit costs.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, Text, Shell commands]

**Output Format:** [Generated video with text responses and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include multilingual voiceover and an optional virtual host.]

## Skill Version(s):

1.0.33 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
