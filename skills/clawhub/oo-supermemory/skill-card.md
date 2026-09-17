## Description:

Supermemory lets agents read, create, update, and delete Supermemory data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Supermemory from an agent for memory search, profile retrieval, document ingestion, memory updates, and deletion workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet-fetched installer commands that the scanner flagged for review.

Mitigation: Prefer a reviewed package-manager or manually verified installer path before first-time setup.

Risk: The skill can change or delete Supermemory data through write and destructive actions.

Mitigation: Confirm the exact payload, target, and intended effect with the user before write or delete actions.

Risk: Connector access can expose or change Supermemory data through OOMOL-managed credentials.

Mitigation: Install only when the publisher and connected OOMOL account are trusted for the intended Supermemory data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-supermemory)
- [Supermemory homepage](https://supermemory.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
