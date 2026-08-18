## Description:

Searches public Xiaohongshu notes by keyword, supports sorting and time filters, and retrieves note lists, interaction data, note details, comments, and creator posts for content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External content creators, brand marketers, market researchers, and data analysts use this skill to collect public Xiaohongshu content signals for topic research, trend discovery, KOL evaluation, comment review, and competitive analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note links, creator profile links, and related public-content results to guaikei.com using GUAIKEI_API_TOKEN.

Mitigation: Use the skill only when that third-party API use is authorized, confirm ambiguous requests are about Xiaohongshu public data, and avoid submitting private or sensitive targets.

Risk: GUAIKEI_API_TOKEN is required for API access and should be treated as a secret.

Mitigation: Store the token in the environment, avoid sharing logs or screenshots that expose it, and rotate the token if it may have been disclosed.

Risk: Command outputs may be retained in local logs, including research targets, public comments, or creator profile results.

Mitigation: Review and periodically delete local artifacts or logs when retained research targets or comments should not remain on disk.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-look-note-guaikei)
- [Guaikei website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results may be saved to local logs.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
