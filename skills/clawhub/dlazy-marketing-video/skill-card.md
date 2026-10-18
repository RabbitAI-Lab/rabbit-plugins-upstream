## Description:

Helps create ecommerce marketing videos from product details, listings, or briefs, with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and sellers use this skill to turn product information or shopping listings into short promotional videos for ecommerce and social campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to an external dLazy service.

Mitigation: Share only content approved for that service and review attachments before upload.

Risk: The CLI stores an API key locally and project conversations may retain prior context.

Mitigation: Protect or rotate the key as needed; start a fresh project or clear saved context for sensitive work.

Risk: The video workflow is focused on ecommerce products rather than all brand-video formats.

Mitigation: Check that the product-to-ecommerce-video workflow fits the intended campaign.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with commands and links to generated video results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ecommerce video generation uses the external dLazy service; follow-up requests may reuse project context.]

## Skill Version(s):

1.0.26 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
