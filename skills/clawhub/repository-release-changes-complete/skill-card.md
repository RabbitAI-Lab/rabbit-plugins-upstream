## Description:

Summarizes repository changes into release notes, writes a local release-note entry, and optionally submits it to a configured delivery target.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release managers use this skill to turn a repository patch into a release note, save it locally, and optionally submit the entry to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository-derived release data may be sent to an external target through under-disclosed generic delivery environment variables.

Mitigation: Review delivery settings before installation; clear generic delivery variables unless using an intentionally configured, approved destination.

Risk: Local release-note files are written to the selected output directory.

Mitigation: Use a dedicated output directory for each run.

## Reference(s):

- [Release Change Analyzer on ClawHub](https://clawhub.ai/wxt-ai/skills/repository-release-changes-complete)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Local Markdown release note and JSON results with identification, release-note, and delivery receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes beneath the chosen output directory; delivery receipt reports sent, delivered, failed, or unconfigured.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
