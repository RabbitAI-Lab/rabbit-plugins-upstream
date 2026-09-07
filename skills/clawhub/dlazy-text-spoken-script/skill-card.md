## Description:

Guides an agent to generate short-video spoken scripts with contrast-driven hooks, emotional resonance, story structure, and personal IP framing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content teams use this skill to draft colloquial short-video spoken scripts for persona-led storytelling, character stories, and viewpoint scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's stated text-script purpose does not match its instructions to install and use a networked image-generation CLI.

Mitigation: Install or invoke the dLazy CLI only when that integration is intentionally needed; otherwise split or revise the package to keep the spoken-script helper text-only.

Risk: The dLazy CLI can store a dLazy API key in local user configuration.

Mitigation: Use an account and key approved for this workflow, protect the local config file, and rotate or revoke the key from the dLazy dashboard when access changes.

Risk: Prompts and explicitly passed media files may be sent to dLazy API and file-hosting endpoints.

Mitigation: Do not submit confidential prompts or media unless policy permits use of dLazy-hosted services for that content.

Risk: Using npm or npx runs third-party package code on the host system.

Mitigation: Review the package source and pin the intended CLI version before installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with optional bash command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Direct script output follows a seven-step spoken-script structure; CLI-related guidance may require npm/npx and a dLazy API key.]

## Skill Version(s):

1.3.14 (source: server release evidence; artifact frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
