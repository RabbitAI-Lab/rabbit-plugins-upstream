## Description:

Retrieves public Xiaohongshu notes, comments, note details, and creator post lists through GUAIKEI for structured content research and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, analysts, and agents use this skill to collect public Xiaohongshu search results, note details, comments, and creator post lists for topic research, competitor analysis, KOL screening, trend monitoring, and follow-on reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided Xiaohongshu search terms, note or profile URLs, request parameters, and the GUAIKEI token are sent to a third-party API service.

Mitigation: Use the skill only for public, non-sensitive targets, confirm data-sharing approval before use, and store the GUAIKEI token securely.

Risk: Returned results are saved locally and may include public profile, note, comment, or interaction data.

Mitigation: Review or delete generated logs when the workspace is shared, synced, archived, or no longer needs the retrieved data.

Risk: The third-party API can return empty results, rate limits, authorization errors, or transient failures.

Mitigation: Branch on status and error_code, retry transient failures cautiously, and do not fabricate conclusions from empty or failed calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-insight-generate)
- [GuAIKEI service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance, configuration]

**Output Format:** [Markdown guidance with shell command examples; command execution returns structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; task results are saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: evidence.release.version and target metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
