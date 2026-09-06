## Description:

A Chinese-language webtoon adaptation agent that turns web novel material into plot breakdowns, episode tags, and per-episode scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agents use this skill to adapt web novels into Chinese webtoon production drafts, including genre setup, plot breakdowns, episode tagging, revisions, and per-episode scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or run the third-party dLazy CLI, store an API key under the user's profile, and send prompts to api.dlazy.com.

Mitigation: Review the skill before installing, prefer the DLAZY_API_KEY environment variable on shared machines, and rotate or revoke dLazy keys when access changes.

Risk: Referenced local media files may be uploaded to files.dlazy.com for cloud generation.

Mitigation: Do not provide sensitive or restricted media, and confirm generation commands only when cloud processing is intended.

Risk: The security summary says the skill's scope and activation are not clearly described.

Mitigation: Use the skill only for webtoon adaptation and related dLazy generation workflows, and review prompts and commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown conversation output with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language adaptation drafts; image-generation commands are run one at a time after user confirmation.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
