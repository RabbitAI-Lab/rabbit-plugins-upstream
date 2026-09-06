## Description:

Turns product photos, product documents, catalogs, or ecommerce listings into conversion-focused shopping ad videos with multi-language voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce teams use this skill to create product advertising videos from product images, documents, catalogs, or marketplace listings. It is suited for store, TikTok Shop, cross-border selling, and ecommerce ad video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts, product links, and attached files may be sent to dLazy's hosted service.

Mitigation: Use the skill only when that data transfer is acceptable, and review local files before passing them with --files.

Risk: The dLazy API key is stored locally or supplied through the environment.

Mitigation: Protect the key, rotate or revoke it when needed, and avoid exposing it in shared logs or prompts.

Risk: A global CLI install persists on the system.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text responses with inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate dLazy hosted chat sessions and optional user-selected file uploads through the dLazy CLI.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter reports 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
