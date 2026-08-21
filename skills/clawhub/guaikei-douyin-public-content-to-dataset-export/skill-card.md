## Description:

Collects public Douyin search results, creator posts, comments, and real-time hot rankings as structured JSON for content research, competitive analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to query Douyin public content, export JSON datasets, monitor competitors, review comments, and track real-time trends. It is not intended for publishing, editing, downloading, or redistributing video content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a GUAIKEI token to query Douyin public data and can save local JSON datasets that may include public personal metadata.

Mitigation: Install only when agents are expected to perform this collection, protect the token, and delete saved logs when they are no longer needed.

Risk: Ambiguous content-research requests could cause an agent to query Douyin when the user did not intend that platform.

Mitigation: Confirm Douyin as the target platform when a request is ambiguous before running the CLI commands.

Risk: Returned media URL fields could be misused for downloading or redistribution outside the skill's stated scope.

Mitigation: Use returned data for analysis only and do not use media URL fields to download or redistribute videos.

Risk: Server security evidence reports scope and disclosure mismatches users should review before installation.

Mitigation: Review the skill behavior and scanner summary before deployment, especially token handling, runtime disclosures, and local log retention.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-public-content-to-dataset-export)
- [Guaikei token and support site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI execution returns structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI commands write JSON to stdout and may save local JSON logs for later analysis.]

## Skill Version(s):

1.0.0 (source: artifact/SKILL.md metadata, artifact/package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
