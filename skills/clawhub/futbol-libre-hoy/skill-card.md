## Description:

List today's football fixtures and live scores using the futbol-libre-hoy CLI/package.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nazzal5448](https://clawhub.ai/user/nazzal5448)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve football fixtures, live scores, date-specific match listings, JSON output, and match URLs for deeper match information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on external npm or PyPI packages and contacts verfutbollibre.net for public match data.

Mitigation: Install and run the package only when the package source and external data request are acceptable for the execution environment.

Risk: The returned football fixture and live score data may be incomplete, delayed, or unavailable if the external service changes or is unreachable.

Mitigation: Treat match data as public third-party information and verify important scores, stats, or lineups against the linked match page or another trusted source.

## Reference(s):

- [Futbol Libre Hoy homepage](https://verfutbollibre.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes match URLs when available; supports live, date-specific, and JSON modes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
