## Description:

DataCite (datacite.org). Use this skill for ANY DataCite request - searching and reading data. Whenever a task involves DataCite, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve individual DOI metadata records and search, filter, sort, and paginate DataCite DOI metadata through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Review the installer source and prefer a verified, pinned, inspectable installation method before running setup commands.

Risk: Authenticated DataCite queries may access non-public metadata through the connected account.

Mitigation: Confirm that the user intends to use the connected account for the requested DOI metadata and avoid exposing non-public results unnecessarily.

## Reference(s):

- [DataCite homepage](https://datacite.org/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-datacite)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live connector schemas and run DataCite read actions with JSON responses.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
