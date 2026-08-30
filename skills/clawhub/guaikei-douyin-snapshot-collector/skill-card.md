## Description:

Collects structured JSON snapshots from public Douyin search results, creator posts, video comments, and real-time hot lists for short-video research and trend analysis.

This skill is for research and development only.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and content research teams use this skill to turn natural-language Douyin research requests into CLI calls that return public search, creator-post, comment, or hot-list data. It is intended for lawful public-data research, competitor monitoring, public-opinion analysis, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may route unrelated short-video or research requests to a third-party service.

Mitigation: Activate only for clear Douyin or public short-video research tasks, and confirm with the user before sending ambiguous requests.

Risk: Requests are sent to guaikei.com with the configured API token and results are saved under logs/.

Mitigation: Tell users before execution that a third-party API will receive the request, keep tokens in GUAIKEI_API_TOKEN, and avoid sending sensitive or private data.

Risk: Server security guidance reports that token-error behavior may emit website or contact guidance despite the skill documentation requiring neutral runtime errors.

Mitigation: Review token-error output before deployment in multi-skill agents and prefer neutral error handling when credentials are missing or invalid.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-snapshot-collector)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Input and output JSON schemas](assets/*.schema.json)
- [Guaikei token and usage help](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance, Files]

**Output Format:** [JSON on stdout with operational logs on stderr and timestamped JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; commands support keyword, URL, ranking, time-window, content-type, duration, and result-limit parameters depending on mode.]

## Skill Version(s):

1.0.0 (source: package.json, references/changelog.md, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
