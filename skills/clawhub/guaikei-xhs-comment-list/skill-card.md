## Description:

Retrieves structured public Xiaohongshu search results, note details, note comments, and creator posts for downstream analysis, comparison, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketing teams, data analysts, and agents assisting them use this skill to retrieve public Xiaohongshu content data for trend research, competitor monitoring, KOL screening, comment analysis, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu URLs, and GUAIKEI_API_TOKEN are sent to the third-party guaikei.com service.

Mitigation: Use the skill only when this data transfer is authorized, keep GUAIKEI_API_TOKEN secret, and rotate or revoke the token if it may have been exposed.

Risk: Command results are written to a local logs directory and may contain collected public content or business-sensitive research.

Mitigation: Review retention expectations before use and periodically delete or protect the logs directory when results are sensitive.

Risk: The skill can request large batches of public Xiaohongshu data, up to 10,000 items per command.

Mitigation: Confirm the collection scope is permitted for the user's environment, reduce limits when unnecessary, and follow platform and organizational data-use rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-comment-list)
- [Guaikei API service entry](https://www.guaikei.com)
- [Options and command reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; command execution returns JSON status, request metadata, and results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; retrieved results are saved under a local logs directory by the command scripts.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
