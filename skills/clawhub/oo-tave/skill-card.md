## Description:

Táve lets an agent search and read contact and studio data through an OOMOL-connected Táve account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Táve through an OOMOL-connected account, including fetching a contact, reading studio profile information, and listing contacts with supported filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Verify the installer source, integrity, and permissions before running curl|bash or irm|iex, and prefer reviewing the official install guide first.

Risk: Read-only connector actions can still access Táve contact and studio information from the connected account.

Mitigation: Run actions only for authorized connected accounts and avoid sharing returned contact or studio data beyond the user-approved scope.

## Reference(s):

- [ClawHub Táve skill](https://clawhub.ai/oomol/skills/oo-tave)
- [Táve homepage](https://www.vsco.co/workspace)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
