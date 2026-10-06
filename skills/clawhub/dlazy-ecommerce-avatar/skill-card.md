## Description:

Guides the creation of ecommerce avatar product videos with portrait recipes and a script-to-voice-to-avatar-to-B-roll workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and content creators use this skill to plan and produce reusable AI-spokesperson videos for product listings and social commerce campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key stored or shared insecurely may expose the dLazy account.

Mitigation: Protect the key and use a per-run environment variable rather than storing a long-lived key when practical.

Risk: Product images and media supplied to the workflow are uploaded to dLazy services.

Mitigation: Upload only assets you are authorized and comfortable to share with the service.

Risk: Avatar generation incurs paid credits, and failed or repeated requests can increase costs.

Mitigation: Check inputs and estimated credits with the documented dry-run option before costly generations.

Risk: Generated product claims or visual credentials may mislead viewers.

Mitigation: Review claims and imagery before publishing, and disclose AI-generated content where the publishing platform requires it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [dLazy homepage](https://dlazy.com)
- [Portrait recipes](artifact/recipes.md)
- [Video production pipeline](artifact/pipeline.md)
- [Troubleshooting and publishing guidance](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and generation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media requires separate paid service calls and video assembly.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
