## Description:

Cohere (cohere.com). Use this skill for Cohere requests such as chat generation, text embeddings, and document reranking through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Cohere through an OOMOL-connected account for chat responses, text embeddings, and document reranking without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented first-time setup can execute remote installer scripts directly in a local shell.

Mitigation: Install the oo CLI from a verified, versioned source and review the installation path before using curl-to-bash or PowerShell iex commands.

## Reference(s):

- [Cohere homepage](https://cohere.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cohere)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Text]

**Output Format:** [Markdown guidance with shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions inspect the live connector schema before payload construction; setup steps are used only after command or authentication failures.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
