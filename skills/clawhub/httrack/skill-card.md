## Description:

Offline website mirroring with HTTrack for snapshotting one page with assets or mirroring a bounded site to disk for offline reading, backup, or research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and knowledge workers use this skill to ask an agent to prepare safe HTTrack commands for one-page snapshots, bounded website mirrors, resumable crawls, and machine-readable mirror reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DNS resolution or redirects can still allow requests to private or internal network services.

Mitigation: Use trusted URLs and run the skill in an environment without access to sensitive internal services or metadata endpoints.

Risk: The skill has broad outbound network reach because it mirrors user-supplied websites.

Mitigation: Install and run it only where broad outbound HTTP and HTTPS access is acceptable.

Risk: Mirrored files are untrusted content and may include active or tracking content.

Mitigation: Treat mirrored output as untrusted and review files before opening or redistributing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/httrack)
- [HTTrack flag evidence](docs/evidence.md)
- [HTTrack recipes](docs/recipes.md)
- [Machine manifest](manifest.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON report expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to use the wrapper commands and consume httrack.doctor.v1 or httrack.report.v1 JSON output.]

## Skill Version(s):

2.0.2 (source: server release evidence; artifact files report 2.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
