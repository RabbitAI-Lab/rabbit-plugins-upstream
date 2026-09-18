## Description:

Pinecone (pinecone.io) routes Pinecone read, create, update, and delete requests through the OOMOL oo CLI connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Pinecone indexes and vector records through an authenticated OOMOL connection, including read, write, and destructive maintenance workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may encourage blind execution of remote installer scripts.

Mitigation: Use a verified, pinned, or package-manager installation path for the oo CLI before running Pinecone connector actions.

Risk: The skill can run write and destructive Pinecone actions that change or delete indexes and vectors.

Mitigation: Inspect the live action schema and confirm the exact payload, target, and expected effect before executing write or destructive commands.

Risk: The oo CLI operates with access to the user's Pinecone account through OOMOL.

Mitigation: Install and use the skill only when the user accepts OOMOL-mediated access, and verify the connected account and scopes before sensitive operations.

## Reference(s):

- [ClawHub Pinecone skill page](https://clawhub.ai/oomol/skills/oo-pinecone)
- [Pinecone homepage](https://www.pinecone.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can emit JSON responses from the oo CLI connector.]

## Skill Version(s):

1.0.4 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
