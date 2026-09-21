## Description:

StealthGPT (stealthgpt.ai) supports StealthGPT requests, including reading, creating, and updating data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate StealthGPT through an OOMOL-connected account, including AI-text detection, text generation, text humanization, and balance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes a remote installer command for the oo CLI.

Mitigation: Review OOMOL's oo CLI installation method and run installer commands only when you trust the source.

Risk: Text generation and humanization actions can consume account resources or use write-capable service operations.

Mitigation: Confirm the exact payload and intended effect with the user before running actions tagged write.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-stealthgpt)
- [StealthGPT homepage](https://www.stealthgpt.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return StealthGPT connector JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
