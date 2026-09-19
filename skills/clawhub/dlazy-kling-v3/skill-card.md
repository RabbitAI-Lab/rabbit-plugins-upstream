## Description:

This skill helps agents generate videos with Kling v3, including text-to-video and image-to-video requests through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run dLazy Kling v3 video generation from prompts or reference images, with options for dry runs, asynchronous polling, and saving generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local files may be sent to dLazy cloud services for video generation.

Mitigation: Submit only content intended for third-party processing, avoid sensitive files, and review dLazy service terms before use.

Risk: The skill depends on a local dLazy API key for authenticated requests.

Mitigation: Use scoped keys where possible, protect local configuration, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Video generation requests may consume paid credits.

Mitigation: Use dry-run or cost checks before paid requests and prefer explicit user confirmation for generation parameters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses; generated media is returned as hosted URLs and can optionally be saved to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; supports dry-run cost checks, asynchronous task polling, and optional local save paths.]

## Skill Version(s):

1.3.17 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
