## Description:

Turns product photos, product links, specifications, manuals, or catalog inputs into conversion-focused ecommerce ad videos with support for multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce teams, marketers, and developers use this skill to create product, marketplace, TikTok Shop, and shopping-ad videos from product assets or listing URLs through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service, and attached local files may be uploaded to dLazy media storage.

Mitigation: Review data sensitivity before invoking the skill or attaching files, and avoid sending confidential material unless the user's dLazy service terms and organization policies allow it.

Risk: Authentication stores a dLazy API key in the local CLI configuration unless supplied per invocation.

Mitigation: Use the documented login or auth flow, protect the local config file, and rotate or revoke the API key from the dLazy dashboard when needed.

Risk: The skill depends on an external npm CLI package and hosted API endpoints.

Mitigation: Use the pinned npm package or npx invocation from the artifact metadata, and review the package/source before installation in controlled environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)
- [dLazy Publisher Profile](https://clawhub.ai/user/dlazyai)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Repository](https://github.com/dlazyai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown with inline bash code blocks and streamed CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill invokes the pinned product-to-ecommerce-video template through dLazy CLI; attached files may be uploaded to dLazy media storage before use.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
