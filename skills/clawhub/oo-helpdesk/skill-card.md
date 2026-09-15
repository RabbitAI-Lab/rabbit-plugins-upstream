## Description:

HelpDesk lets an agent read, create, update, search, move, and delete HelpDesk tickets through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support operators use this skill to manage HelpDesk tickets through an authenticated OOMOL connector. It supports ticket reads, searches, assignment support data, updates, moves, creation, and deletion with confirmation guidance for write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote shell installer commands that run local code.

Mitigation: Review the installation path before use, prefer a pinned and verifiable oo CLI release or official package manager, and avoid running the remote installer from an elevated terminal.

Risk: Write and destructive HelpDesk actions can change, move, or delete tickets.

Mitigation: Verify ticket IDs and payloads carefully, and require explicit user confirmation before approving write or delete operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-helpdesk)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [HelpDesk Homepage](https://www.helpdesk.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before calls and expects JSON responses from the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
