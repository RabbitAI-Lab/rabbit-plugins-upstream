## Description:

A Chinese-language agent skill for adapting web novels into webtoon dramas through genre intake, plot breakdown, episode tagging, per-episode script writing, and optional dLazy CLI image-generation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and developers use this skill to turn web-novel material into Chinese webtoon adaptation outputs, including plot breakdowns, episode tags, and per-episode scripts. When image generation is requested, it guides dLazy CLI usage for cloud-backed media generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media may be sent to dLazy cloud endpoints for inference and storage.

Mitigation: Install and use the skill only when the user intends to use dLazy's external CLI and cloud service; avoid submitting sensitive prompts or media unless that data handling is acceptable.

Risk: The skill requires a dLazy API key that may be stored in a local CLI configuration file or supplied through an environment variable.

Mitigation: Use normal credential hygiene: protect the local config, prefer scoped keys when available, and rotate or revoke keys from the dLazy dashboard when no longer needed.

Risk: Security evidence marks the release suspicious because it mixes webtoon-writing guidance with external CLI image generation, credential storage, network upload behavior, and inconsistent install/version metadata.

Mitigation: Review the skill and dLazy CLI before installation, verify install versions and endpoint behavior, and separate text adaptation from image generation before treating the release as low-risk.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown with structured adaptation sections and inline shell commands when generation is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for user confirmation before each dLazy generation command; generated media results may be returned as hosted dLazy file URLs.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
