## Description:

DeepSeek lets agents operate DeepSeek through an OOMOL-connected account using the oo CLI for chat completions, messages, balance checks, and model listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect DeepSeek connector schemas and run approved DeepSeek actions through OOMOL-managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that execute directly in a shell.

Mitigation: Review installer steps before use, prefer official versioned and checksum-verified installation instructions, and do not let an agent run remote shell installers automatically.

Risk: Write actions may spend DeepSeek account credits or create messages on behalf of the user.

Mitigation: Limit connector actions to user-approved DeepSeek requests and confirm exact payloads before running write actions.

## Reference(s):

- [DeepSeek homepage](https://platform.deepseek.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub DeepSeek skill](https://clawhub.ai/oomol/skills/oo-deepseek)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include JSON data and an execution id under meta.executionId.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
