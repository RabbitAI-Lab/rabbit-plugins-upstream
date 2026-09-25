## Description:

A Chinese-language agent skill for adapting web novels into webtoon plot breakdowns, episode tags, per-episode scripts, and optional dLazy CLI image-generation prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, writers, and developers use this skill to turn web-novel material into Chinese webtoon adaptation plans, episode breakdowns, and scripts. The skill can also guide terminal-driven dLazy CLI image generation after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or run the dLazy CLI and store an API key in a local configuration file.

Mitigation: Use the npx or DLAZY_API_KEY environment-variable path when possible, and rotate or revoke the key from the dLazy dashboard when it is no longer needed.

Risk: Prompts and uploaded media can be sent to dLazy services and generation results can be returned as externally hosted URLs.

Mitigation: Only confirm generation commands for content intended for dLazy processing, and avoid sending sensitive text or media unless that transfer is approved.

Risk: The artifact mixes a writing workflow with terminal-driven image generation and vague metadata.

Mitigation: Review the skill and generated commands before deployment, especially when the expected use is only text adaptation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with structured Chinese prose and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include externally hosted generation URLs returned by dLazy services.]

## Skill Version(s):

1.3.20 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
