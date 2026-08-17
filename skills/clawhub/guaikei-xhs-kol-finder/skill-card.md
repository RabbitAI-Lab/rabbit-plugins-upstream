## Description:

Searches public Xiaohongshu notes, note details, comments, and creator posts through the Guaikei API and returns structured data for trend research, competitor analysis, KOL filtering, and comment insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, content operators, analysts, and agents use this skill to retrieve public Xiaohongshu data for content research, campaign planning, creator screening, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, target Xiaohongshu links, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only where sending those inputs to the Guaikei API is approved, and manage the token as a credential.

Risk: Collected public content, query history, and research targets may remain in local logs.

Mitigation: Review and delete generated logs when the collected content or research targets should not persist on disk.

Risk: The skill is intended for public Xiaohongshu data and should not be used for private, hidden, or unauthorized content.

Mitigation: Limit use to public data retrieval and keep downstream distribution within the user's authorized scope.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-kol-finder)
- [Guaikei API Website](https://www.guaikei.com)
- [Options Reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes result logs locally.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
