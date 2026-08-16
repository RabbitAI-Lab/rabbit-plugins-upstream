## Description:

Retrieves public Xiaohongshu note search results, note details, note comments, and creator post data through GUAIKEI command-line tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External content, marketing, and data-analysis teams use this skill to collect public Xiaohongshu notes, comments, and creator post data for trend research, competitive monitoring, KOL screening, and content planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note/profile links, request limits, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only with authorized public Xiaohongshu data, protect the API token, and avoid submitting sensitive searches or links.

Risk: Generated logs can retain research targets, URLs, and xsec_token query values locally.

Mitigation: Delete or protect local log files when searches, target accounts, URLs, or query tokens are sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-hot-list)
- [GUAIKEI API service](https://www.guaikei.com)
- [Options and command reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [CLI JSON responses with status, request, skill metadata, and results fields; local JSON log files may also be written.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command limits accept up to 10000 records depending on mode.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
