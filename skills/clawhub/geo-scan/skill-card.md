## Description:

Audit one public website's readiness for AI answer engines and produce a prioritized list of fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aureliusclaw](https://clawhub.ai/user/aureliusclaw)

### License/Terms of Use:

MIT

## Use Case:

Website owners and developers use geo-scan to assess whether public pages are accessible, readable, and quotable by AI answer engines, then prioritize technical improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A scanned site may trigger internal connections or local file reads because of a verified safety flaw.

Mitigation: Review before installing; prefer a release that checks each fetched URL's scheme and removes unused FTP/file handlers. Until then, isolate network and filesystem access and keep private scanning disabled.

## Reference(s):

- [Project information](https://github.com/AureliusClaw/geo-scan)
- [ClawHub release page](https://clawhub.ai/aureliusclaw/skills/geo-scan)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Prioritized website audit report with scores, evidence, and recommended actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include evidence for each score and may be emitted as Markdown or JSON.]

## Skill Version(s):

1.2.5 (source: server-resolved release, plugin metadata, README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
