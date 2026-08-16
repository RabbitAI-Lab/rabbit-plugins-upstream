## Description:

This skill helps an agent search Xiaohongshu notes, retrieve note details and comments, and collect public creator posts through guaikei.com command-line tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, content operators, and analysts use this skill to gather Xiaohongshu public note, comment, and creator-post data for content research, competitor monitoring, KOL screening, and trend analysis. It is not intended for login-required actions, private data access, posting, liking, commenting, or following.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, and the GUAIKEI API token are sent to guaikei.com.

Mitigation: Use only approved research inputs and an authorized token, and avoid sensitive topics when data sharing with the third-party service is not acceptable.

Risk: Successful results are saved locally under logs/.

Mitigation: Restrict access to shared machines and periodically delete saved logs when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-search-results)
- [Guaikei service](https://www.guaikei.com)
- [Parameter and calling guide](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [Shell commands that return structured JSON and may save JSON logs locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful results are saved under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
