## Description:

Workable helps agents search and read Workable candidate and job data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting teams and agents use this skill to inspect Workable candidates and jobs through an authenticated, connected Workable account. It supports read-only list and detail retrieval workflows with optional filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute arbitrary code.

Mitigation: Install the oo CLI only from a trusted and verified source, preferably through a pinned, signed, or checksum-verified package path.

Risk: The skill queries data from a connected Workable account.

Mitigation: Use it only when the user intends to read Workable data from that connected account, and inspect the action schema before sending filters or identifiers.

## Reference(s):

- [Workable homepage](https://www.workable.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-workable)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from executed actions are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
