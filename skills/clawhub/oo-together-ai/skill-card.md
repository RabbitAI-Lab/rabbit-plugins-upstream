## Description:

Together AI connector for creating chat completions, generating embeddings, and listing models through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Together AI chat completion, embedding, and model-listing actions via the oo CLI with credentials managed by OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users to run remote installer commands that can execute code on the machine.

Mitigation: Avoid running remote install commands blindly; prefer a verified package, pinned release, or reviewed installer before connecting an account.

Risk: Together AI actions are operated through OOMOL as an intermediary.

Mitigation: Install only if using OOMOL as an intermediary for Together AI actions is acceptable for the deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-together-ai)
- [Together AI homepage](https://www.together.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions can create non-streaming chat completions, generate embeddings, or list models available to the connected API key.]

## Skill Version(s):

1.0.3 (source: server evidence release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
