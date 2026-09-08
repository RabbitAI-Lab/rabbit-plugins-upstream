## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy Jimeng text-to-image CLI from an agent, sending prompts and optional image inputs to generate hosted image results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media paths passed to image fields are sent to dLazy hosted services.

Mitigation: Only submit prompts and files suitable for processing by the dLazy service, and avoid sensitive local files unless the user has approved that transfer.

Risk: The skill depends on the npm-distributed dLazy CLI and hosted API endpoints.

Mitigation: Review the dLazy CLI source or npm package when supply-chain risk matters, and prefer the documented npx invocation when a persistent global binary is not needed.

Risk: The CLI stores API credentials in the local dLazy configuration when using the login or auth setup flows.

Mitigation: Use organization-scoped keys, rotate or revoke keys from the dLazy dashboard when needed, and use the DLAZY_API_KEY environment variable for per-invocation credentials when appropriate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image results are returned as hosted file URLs; async calls may return a task identifier for later polling.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
