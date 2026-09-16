## Description:

OpenAI helps agents operate OpenAI through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live OpenAI connector schemas and run supported OpenAI actions through an OOMOL-connected account. It covers common OpenAI workflows including responses, embeddings, image generation, audio, moderation, token counting, model lookup, stored response retrieval, and batch management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes OpenAI requests and payloads through OOMOL.

Mitigation: Install and use it only when that routing is intended for the task and acceptable for the data being sent.

Risk: The first-time setup guidance includes pipe-to-shell installer commands.

Mitigation: Use a verified installation method, or inspect and verify the installer before running it.

Risk: Write actions can change OpenAI state or submit sensitive payloads.

Mitigation: Review payloads carefully and require explicit user confirmation before file uploads, write actions, or other state-changing operations.

## Reference(s):

- [ClawHub OpenAI skill page](https://clawhub.ai/oomol/skills/oo-openai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OpenAI API](https://openai.com/api/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON when commands are run with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
