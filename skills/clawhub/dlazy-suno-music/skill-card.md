## Description:

Generates Suno music from prompts in inspiration or custom mode, with or without vocals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and music creators use this skill to generate songs or instrumental tracks from prompts, with optional custom lyrics and style settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan found a mismatch between the music-generation description and a `dlazy login` command, and some referenced CLI material was unavailable for review.

Mitigation: Confirm the credential setup matches the intended task, then review the CLI package and its credential handling before installation.

Risk: Prompts and local media supplied for generation are sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive prompts or media, and review dLazy's service terms before use.

## Reference(s):

- [dLazy CLI project information](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON, Shell commands, Configuration instructions]

**Output Format:** [Generated audio file or hosted audio URL with JSON result metadata; Markdown usage guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio can be saved locally; asynchronous requests can return a task ID for polling.]

## Skill Version(s):

1.3.42 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
