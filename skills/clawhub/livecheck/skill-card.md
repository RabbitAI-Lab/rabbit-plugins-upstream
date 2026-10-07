## Description:

Checks specific job postings, product listings, and other pages for current availability, with optional condition checks and 30-day change alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[moyecj-snap](https://clawhub.ai/user/moyecj-snap)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers and their agents can screen posting lists before applying or contacting employers. Shopping assistants can check listing availability, monitor page changes, and check confirmation pages after user-authorized actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned npm CLI may execute an unreviewed version.

Mitigation: Review and pin the CLI version before installation or use.

Risk: Paid checks, 30-day watches, and confirmation requests can incur charges.

Mitigation: Get explicit user approval before paid calls and limit the number of checks.

Risk: Target URLs, callback URLs, and confirmation-page URLs are shared with an external service.

Mitigation: Obtain approval before sending URLs, and avoid sharing sensitive links or tokens.

Risk: Pages requiring login or JavaScript may not yield a reliable availability result.

Mitigation: Report unknown results as uncertain rather than treating them as live or closed.

## Reference(s):

- [Livecheck on ClawHub](https://clawhub.ai/moyecj-snap/skills/livecheck)
- [Getting Started](artifact/rules/getting-started.md)
- [Livecheck service](https://livecheck.fly.dev)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown guidance and structured status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability is reported as live, closed, or unknown, with page title and supporting signals.]

## Skill Version(s):

3.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
