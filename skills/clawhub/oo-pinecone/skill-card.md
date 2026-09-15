## Description:

Pinecone (pinecone.io). Use this skill for Pinecone requests including reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Pinecone indexes and vector data through the OOMOL oo CLI connector. It supports index lifecycle, vector query and retrieval, and state-changing vector or index operations with explicit safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can ask an agent to execute remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation path first and prefer a verified official release or package-manager installation before allowing any remote installer command.

Risk: Write and destructive Pinecone actions can change or delete indexes and vector data.

Mitigation: Require explicit user approval for the exact target, payload, and expected effect before running any action marked write or destructive.

Risk: Incorrect action payloads can send malformed or unintended Pinecone operations.

Mitigation: Inspect the live oo connector schema before each action and build payloads only from the returned contract.

## Reference(s):

- [Pinecone homepage](https://www.pinecone.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pinecone)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
