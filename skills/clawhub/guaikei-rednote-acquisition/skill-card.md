## Description:

Fetches public Xiaohongshu/Rednote notes, note details, comments, and creator posts through Guaikei command-line tools for downstream analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, marketing analysts, and content teams use this skill to collect publicly accessible Xiaohongshu/Rednote data from keywords or profile/note URLs for content research, competitor monitoring, KOL screening, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, Xiaohongshu note/profile URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Install and run the skill only when that third-party data sharing is acceptable for the user's organization and task.

Risk: Retrieved public content and comments may be written to local logs and could include sensitive business research or personal comment data.

Mitigation: Review retention needs and delete or protect local logs when outputs contain sensitive research or personal data.

Risk: The skill is intended for lawfully accessible public Xiaohongshu data, not private, hidden, or login-only content.

Mitigation: Use only public keywords and public note/profile URLs, and decline requests for private or access-restricted data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-acquisition)
- [Guaikei service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; command results may also be saved to local logs.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact package metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
