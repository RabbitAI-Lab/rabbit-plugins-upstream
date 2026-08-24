## Description:

Retrieves public Xiaohongshu content through keyword search, note details, comments, and creator-post monitoring so agents can support marketing research and competitive analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content marketers, analysts, and operators use this skill to collect public Xiaohongshu search results, post details, comments, and creator activity for trend research, competitor monitoring, KOL screening, and campaign reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or links and the GUAIKEI_API_TOKEN to Guaikei's API.

Mitigation: Install and run it only where this data sharing is acceptable, and manage the token as a credential.

Risk: Saved logs may contain business research, comment data, or other sensitive analysis inputs.

Mitigation: Keep generated logs out of commits, shared backups, and public artifacts unless reviewed.

Risk: Public platform data collection can be misused or violate platform, legal, or organizational requirements.

Mitigation: Use the skill only for lawful, public, platform-compliant data collection and internal analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-data-for-marketing)
- [Guaikei API website](https://www.guaikei.com)
- [Parameter and option reference](artifact/references/options.md)
- [Skill changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files]

**Output Format:** [Markdown guidance with CLI commands; command execution returns structured JSON and may save local JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and Node.js 16.14.0 or newer.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
