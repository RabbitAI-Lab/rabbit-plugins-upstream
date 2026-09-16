## Description:

Google Docs (workspace.google.com) enables an agent to read, search, create, update, export, copy, and delete Google Docs content through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate Google Docs for document search, retrieval, export, creation, formatting, and controlled updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include executing an unverified remote installer.

Mitigation: Avoid running the pipe-to-shell installer as written; use a verified or inspected installation method before installing.

Risk: The skill can modify Google Docs state through write actions.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

Risk: Destructive actions can remove or overwrite document content.

Mitigation: Confirm the target document and operation, then obtain explicit user approval before destructive changes.

Risk: The connector path relies on access to the user's Google Docs account.

Mitigation: Install only if the user trusts OOMOL's connector path and intends to connect the relevant Google Docs account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-googledocs)
- [Google Docs](https://workspace.google.com/products/docs/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector actions may return JSON, text, or exported PDF data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require confirmation, and destructive actions require explicit approval before execution.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
