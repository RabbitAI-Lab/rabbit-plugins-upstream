## Description:

Helps adapt web novels into Chinese-language webtoon drama materials, including genre intake, plot breakdowns, episode tagging, per-episode scripts, and optional dLazy CLI image-generation workflow guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, writers, and agent users can use this skill to convert web-novel material into structured webtoon adaptation outputs in Chinese. The skill also guides users through dLazy CLI setup and single-step hosted image generation when visual assets are requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can invoke npm or npx based dLazy CLI workflows for hosted image generation.

Mitigation: Review the package, install source, and command before execution; use pinned CLI versions or npx for on-demand execution.

Risk: dLazy API keys may be stored locally or passed through an environment variable.

Mitigation: Use normal secret-handling practices, restrict local config file access, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Prompts and referenced media may be sent to dLazy API and file-hosting services.

Mitigation: Avoid submitting confidential source text or media unless the user has approved that hosted processing path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown conversation output with structured Chinese adaptation sections and inline shell commands when invoking dLazy CLI workflows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs returned by dLazy-hosted services.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
