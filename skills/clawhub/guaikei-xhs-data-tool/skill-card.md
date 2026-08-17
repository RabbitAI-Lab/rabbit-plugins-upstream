## Description:

Fetches public Xiaohongshu search results, note details, creator posts, and comments through guaikei.com so an agent can return structured data for content, competitor, KOL, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketing analysts, and agents use this skill to retrieve structured public Xiaohongshu data for topic research, competitor monitoring, creator screening, and comment analysis. It requires a GUAIKEI_API_TOKEN and should be used only for explicit Xiaohongshu data tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords and URLs to guaikei.com using a provider API token.

Mitigation: Use it only when the user has explicitly requested Xiaohongshu data retrieval and is comfortable sharing those inputs with the provider service.

Risk: The skill can collect large volumes of public social-media content and write results to local logs.

Mitigation: Keep collection limits aligned with the task, avoid personal or sensitive investigations, and review or delete generated logs after use.

Risk: Broad trigger language could cause the skill to run for social-media analysis requests that are not clearly Xiaohongshu-specific.

Mitigation: Confirm the platform and requested action before execution when the user has not provided a Xiaohongshu keyword, note URL, or creator profile URL.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-data-tool)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; executed CLI scripts return structured JSON and save local log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on public Xiaohongshu data availability, a valid GUAIKEI_API_TOKEN, network access to guaikei.com, and requested limits up to 10000 items.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
