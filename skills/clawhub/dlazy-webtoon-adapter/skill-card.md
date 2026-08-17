## Description:

Adapts web novel material into Chinese webtoon workflows, including genre confirmation, plot breakdown, episode tagging, per-episode script writing, and reviewed dLazy CLI image-generation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, writers, and agents use this skill to turn supplied web novel content into Chinese webtoon adaptation artifacts: genre baselines, plot breakdowns, episode tags, and episode scripts. When visual generation is requested, it guides stepwise, user-confirmed dLazy CLI usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can require third-party dLazy CLI or npx execution.

Mitigation: Install or run the CLI only when dLazy cloud generation is intended, keep the pinned package version under review, and approve each command before execution.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use organization-scoped keys, restrict local configuration access, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: Prompts and local media paths used for generation may be sent to dLazy API and file-hosting endpoints.

Mitigation: Avoid submitting sensitive or restricted material unless the data handling is approved for dLazy cloud processing.

Risk: Generated adaptation guidance, scripts, or image prompts can contain story errors, inconsistencies, or unsuitable creative choices.

Mitigation: Review plot breakdowns, episode scripts, commands, and generated results before publication or downstream use.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Chinese structured Markdown-style conversation text with optional reviewed shell commands and generated media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are produced in conversation and may depend on user-supplied novel text, revision notes, dLazy API credentials, and dLazy-hosted generation results.]

## Skill Version(s):

1.3.7 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
