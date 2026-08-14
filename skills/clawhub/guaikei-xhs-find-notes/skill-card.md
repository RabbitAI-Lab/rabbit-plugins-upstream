## Description:

Searches public Xiaohongshu notes, retrieves note details and comments, and collects public creator posts as structured data for content research, competitor analysis, KOL screening, and comment insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, content teams, and analysts use this skill to retrieve public Xiaohongshu note, comment, and creator-post data for downstream analysis and reporting. It does not support login, publishing, engagement actions, or private-content access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, links, and the GUAIKEI_API_TOKEN to the third-party guaikei.com API service.

Mitigation: Use only approved tokens and inputs, and install the skill only where third-party API disclosure is acceptable.

Risk: Successful commands save fetched notes, comments, account data, and analysis-ready JSON results to a local logs directory.

Mitigation: Review, retain, or delete local logs according to the user's data-handling and retention requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-find-notes)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Guidance]

**Output Format:** [Structured JSON written to stdout, with result logs saved locally when commands succeed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include status, error_code, message, request metadata, skill_metadata, and results or null.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
