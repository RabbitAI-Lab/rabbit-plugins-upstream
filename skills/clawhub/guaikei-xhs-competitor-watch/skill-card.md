## Description:

Retrieves public Xiaohongshu search results, note details, comments, and creator posts as structured data for competitor monitoring, trend research, KOL screening, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, and analysts use this skill to collect public Xiaohongshu content data before summarizing, comparing, or reporting on competitors, topics, creators, and comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, links, and requested public-data targets are sent to guaikei.com using the configured API token.

Mitigation: Use the skill only when that data transfer is permitted for the user and task, and avoid sending sensitive or non-public targets.

Risk: Retrieved comments, profile data, competitor targets, or analysis outputs may remain on disk in the logs/ directory.

Mitigation: Review and delete logs/ when outputs should not be retained locally.

Risk: The skill depends on a valid GUAIKEI_API_TOKEN and external guaikei.com availability.

Mitigation: Confirm the token is configured and valid before use, and retry or defer work when the service returns transient errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-competitor-watch)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Configuration, Guidance]

**Output Format:** [Structured JSON data with concise Markdown guidance and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may save retrieved results under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
