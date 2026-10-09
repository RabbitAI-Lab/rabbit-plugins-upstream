## Description:

Creates promotional shopping videos from product details or listings, with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and sellers use this skill to create product ads and social-commerce videos from product descriptions, documents, or storefront listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments may be sent to dLazy, and attached files may be uploaded to its storage.

Mitigation: Send only materials you are authorized to share with the hosted service.

Risk: Authentication can save an organization API key to local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it is exposed.

Risk: Continuing an existing project can reuse its prior conversation context.

Mitigation: Check the project before continuing, or start a new project for unrelated work.

Risk: A global CLI install persists beyond the current task.

Mitigation: Use the documented pinned npx invocation if a persistent global install is unwanted.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Streamed text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation is handled by the dLazy hosted service; responses can continue within an existing project.]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata; skill frontmatter states 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
