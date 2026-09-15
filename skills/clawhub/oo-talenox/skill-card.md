## Description:

Talenox (talenox.com). Use this skill for ANY Talenox request — searching and reading data. Whenever a task involves Talenox, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business users use this skill to inspect Talenox connector schemas and retrieve branches, employees, company settings, working days, and working hours through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running a remote installer directly in a shell.

Mitigation: Review the setup path before installing, prefer a verified package manager or versioned release with checksums or signatures, and avoid running curl|bash or irm|iex from an elevated shell.

Risk: Connector actions access Talenox business and employee data through the connected account.

Mitigation: Use the live action schema before each request and rely on the connected account's scoped permissions; confirm payloads before any future action marked write or destructive.

## Reference(s):

- [ClawHub Talenox Skill](https://clawhub.ai/oomol/skills/oo-talenox)
- [Talenox homepage](https://www.talenox.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId; listed actions are read-only get and list operations.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
