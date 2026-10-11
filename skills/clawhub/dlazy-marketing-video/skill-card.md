## Description:

Creates product-focused marketing videos from product details, listings, or briefs, with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and sellers use this skill to create promotional and ecommerce videos for social channels, product listings, and ad campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached brand assets may be uploaded to dLazy's hosted service.

Mitigation: Attach only files intended for upload and avoid including sensitive information in prompts.

Risk: The CLI may save an organization API key locally.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

Risk: Project sessions may retain prior context across requests.

Mitigation: Start a new project for sensitive work and clear its saved session when finished.

## Reference(s):

- [dLazy CLI source (skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text response from the video-generation service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Follow-up responses can use a project session to retain context.]

## Skill Version(s):

1.0.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
