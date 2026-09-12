## Description:

Generates high-quality videos from text prompts or image inputs using Kling v3 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run dLazy's hosted Kling v3 workflow for text-to-video and image-to-video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on installing or invoking the third-party @dlazy/cli npm package.

Mitigation: Review the @dlazy/cli source or package before first use, avoid elevated privileges, and prefer the pinned npx invocation when a persistent global install is unnecessary.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Use per-invocation credentials when appropriate and rotate or revoke the organization API key if exposure is suspected.

Risk: Prompts and local media inputs are sent to dLazy's hosted API and media storage.

Mitigation: Submit only prompts and files that are acceptable to upload to dLazy's service.

Risk: Hosted video generation can incur service charges or fail when credits are insufficient.

Mitigation: Use the documented dry-run option for cost estimates when needed and confirm account credits before long-running generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted file URLs or async task identifiers; local input media can be uploaded to dLazy.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
