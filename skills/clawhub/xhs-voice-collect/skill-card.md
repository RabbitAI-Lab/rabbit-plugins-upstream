## Description:

xhs-voice-collect helps agents retrieve public Xiaohongshu notes, note details, comments, and creator post lists for content research, competitive analysis, KOL screening, and trend insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Content creators, marketers, analysts, and agents use this skill to collect structured public Xiaohongshu data for topic research, competitor monitoring, comment analysis, KOL screening, and report preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, URLs, and returned public-platform data are sent to a third-party API service.

Mitigation: Use the skill only after confirming that this data sharing is acceptable for the task and organization.

Risk: Collected Xiaohongshu results may be written to local logs and can include sensitive research intent or campaign context.

Mitigation: Keep logs local, review them before sharing, and delete them when queries or results are sensitive.

Risk: The required GUAIKEI_API_TOKEN can enable access to the API service if exposed.

Mitigation: Store the token in the environment, avoid committing or pasting it into outputs, and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-voice-collect)
- [GUAIKEI API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and returns public Xiaohongshu data suitable for downstream summaries, comparisons, clustering, and reports.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact package metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
