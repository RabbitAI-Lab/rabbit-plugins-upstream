## Description:

Generates videos with Kling v3 from text prompts or input images through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to have an agent run the pinned dLazy CLI for Kling v3 text-to-video or image-to-video generation. It can check generation cost with dry-run, wait for async results, and save generated media when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media paths provided to the skill may be sent to dLazy's hosted service, and generated files may be hosted on files.dlazy.com.

Mitigation: Avoid sensitive prompts or media unless the user accepts dLazy service handling, and review the service terms before use.

Risk: Authentication may save a dLazy API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when preferred, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Video generation can consume paid credits.

Mitigation: Use dry-run or explicit user confirmation before paid generations when cost matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI source listed in package metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, async task IDs, cost estimates with --dry-run, or saved local assets when --save is used.]

## Skill Version(s):

1.3.20 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
