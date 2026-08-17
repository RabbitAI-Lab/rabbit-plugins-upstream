## Description:

Retrieves public Xiaohongshu content for keyword search, note details, comments, and creator post lists using the Guaikei data API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, and analysts use this skill to gather public Xiaohongshu content for topic research, comment analysis, creator monitoring, competitor monitoring, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu links, and the Guaikei API token are sent to Guaikei's service.

Mitigation: Use only approved public-platform research targets and confirm the organization permits sharing these inputs with Guaikei before running commands.

Risk: Command results are saved locally in logs, which may retain copies of public-platform data and research targets.

Mitigation: Periodically delete the local logs directory or apply local retention controls when saved copies are not needed.

Risk: The skill cannot access private, login-required, posting, liking, or cross-platform workflows.

Mitigation: Keep use to public Xiaohongshu search, note detail, comments, and creator-post retrieval; decline or redirect out-of-scope requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-content-radar)
- [Guaikei service](https://www.guaikei.com)
- [Parameter and invocation guide](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results may be saved to local logs.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
