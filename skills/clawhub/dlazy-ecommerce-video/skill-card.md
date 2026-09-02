## Description:

Turns product photos, specifications, manuals, catalogs, or ecommerce listings into conversion-focused shopping ad videos with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce operators use this skill to turn product media, product documents, or marketplace listings into shopping ad videos for stores, TikTok Shop, and cross-border selling workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected attached files are sent to dLazy's hosted service.

Mitigation: Review the dLazy service and CLI before use, and avoid attaching sensitive files unless sharing them with dLazy is appropriate.

Risk: The dLazy API key can be stored in the local CLI configuration.

Mitigation: Protect the local config file and rotate or revoke the API key when machine access or organization membership changes.

Risk: The skill relies on the third-party dLazy CLI, npm or npx, and hosted API endpoints.

Mitigation: Use the pinned CLI install or npx command from the release evidence, and review the CLI source or package before installing in managed environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or continue a dLazy project; user-selected files can be uploaded to dLazy media storage when attached.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
