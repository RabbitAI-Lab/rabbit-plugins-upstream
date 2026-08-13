## Description:

A Xiaohongshu operations data skill for searching public notes, retrieving note details and comments, and listing a creator's public posts for content research, competitor analysis, KOL screening, and trend insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, analysts, and agents use this skill to collect public Xiaohongshu search results, note details, comments, and creator post lists for downstream summarization, comparison, campaign planning, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu search terms, note links, profile links, and GUAIKEI_API_TOKEN are sent to the third-party guaikei.com API.

Mitigation: Use only approved tokens, avoid submitting sensitive targets, and confirm that third-party API use is acceptable for the intended workspace before running commands.

Risk: Command results are saved locally under logs and may include public content, interaction metrics, comments, and profile URLs.

Mitigation: Review log retention and sharing practices, and delete or restrict generated log files when they are no longer needed.

Risk: The skill is limited to public Xiaohongshu data and does not replace a compliance or marketing judgment review.

Mitigation: Use the returned JSON as source material for human-reviewed analysis, and do not use it to access private, hidden, or login-only data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-note-rank)
- [Guaikei API website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance, files]

**Output Format:** [JSON command output with concise text guidance and local JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and sends Xiaohongshu keywords or links to the third-party guaikei.com API.]

## Skill Version(s):

1.0.0 (source: server release evidence, skill frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
