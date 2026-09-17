## Description:

Together AI (together.ai). Use this skill for ANY Together AI request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Together AI through an OOMOL-connected account, including non-streaming chat completions, embeddings, and model listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path recommends running a remote installer through a shell or PowerShell expression.

Mitigation: Use a pinned, verifiable installer or review the installer before running it.

Risk: Prompts, documents submitted for embeddings, and model request metadata pass through OOMOL as well as Together AI.

Mitigation: Install and use the skill only when that routing is acceptable for the data being submitted.

Risk: The skill can create chat completions and embeddings through a connected Together AI account.

Mitigation: Confirm write-action payloads and expected effects before executing connector calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-together-ai)
- [Together AI homepage](https://www.together.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses schema-first connector calls and returns JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
