## Description:

Use this skill to operate Jina AI for reading, creating, and updating data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Jina AI through an OOMOL-connected account, inspect live action schemas, create embeddings, and rerank documents without handling raw API tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could execute unverified code.

Mitigation: Install the oo CLI only through a trusted, verifiable channel or inspect and verify the installer before running it; do not allow an agent to automatically run curl|bash or irm|iex commands.

Risk: Embedding and reranking inputs are sent outside the local environment through OOMOL and Jina AI.

Mitigation: Use the skill only when sharing the relevant input data with OOMOL and Jina AI is acceptable for the user's task and data policy.

## Reference(s):

- [Jina AI homepage](https://jina.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jina-ai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return Jina AI connector responses as JSON when actions are executed with --json.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
