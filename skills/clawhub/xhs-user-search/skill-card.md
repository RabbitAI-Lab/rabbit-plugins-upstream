## Description:

xhs-user-search helps agents retrieve and structure public Xiaohongshu keyword results, note details, comments, and creator post activity for content research, competitive monitoring, and feedback analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, marketing teams, content operators, and analysts use this skill to collect public Xiaohongshu search, note, comment, and creator activity data for trend research, campaign planning, competitor review, KOL screening, and user feedback analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or URLs to the third-party Guaikei API using GUAIKEI_API_TOKEN.

Mitigation: Confirm the data-sharing scope and token authorization before use, and avoid submitting sensitive or non-public inputs.

Risk: Returned public data can be saved in the local logs directory.

Mitigation: Review, retain, or delete generated logs according to the user's data handling policy.

Risk: The documentation describes a broader Xiaohongshu data collection capability than the one-line summary alone.

Mitigation: Review the full skill behavior, required inputs, and supported commands before installing or invoking it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-user-search)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON results from the command-line scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results may be saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
