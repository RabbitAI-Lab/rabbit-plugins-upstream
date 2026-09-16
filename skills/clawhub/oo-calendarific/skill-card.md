## Description:

Calendarific (calendarific.com) helps an agent search and read Calendarific holiday, country, and language data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Calendarific holidays by country and year, list supported countries, and list supported languages from an OOMOL-connected Calendarific account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running remote installer scripts directly in a shell.

Mitigation: Review the install path first, prefer a verified and version-pinned oo CLI package or official documentation with checksum or signature checks, and avoid running the installer from an elevated shell.

Risk: Calendarific access depends on provisioned OOMOL credentials and a connected Calendarific account.

Mitigation: Use the skill's first-time setup steps only after an auth or connection failure, and rely on server-injected credentials rather than handling API tokens directly.

## Reference(s):

- [Calendarific homepage](https://calendarific.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calendarific action responses are returned as JSON with data and execution metadata when the oo CLI is available and connected.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
