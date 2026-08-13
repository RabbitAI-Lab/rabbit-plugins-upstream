## Description:

Searches public Xiaohongshu notes, retrieves note details and comments, and fetches public creator posts as structured data for trend research, competitor analysis, KOL screening, and comment insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, content teams, analysts, and agent operators use this skill to collect structured public Xiaohongshu data from keywords, note links, or creator profile links before summarizing trends, competitors, KOL candidates, or comment themes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, and token-authenticated requests are sent to the guaikei.com API.

Mitigation: Confirm the user is comfortable with this data flow and avoid submitting confidential research targets or private links.

Risk: Generated local JSON logs may contain business analysis, searched keywords, URLs, and returned public data.

Mitigation: Store logs only in approved workspaces and delete or protect them on shared machines.

Risk: The skill only supports public Xiaohongshu data and depends on a valid GUAIKEI_API_TOKEN and third-party API availability.

Mitigation: Check token configuration, URL type, and API errors before treating empty or failed responses as analytical evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-blogger-track)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; command executions return JSON result objects and may write local JSON logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; results should be checked for status, error_code, and empty responses before analysis.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter and package metadata report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
