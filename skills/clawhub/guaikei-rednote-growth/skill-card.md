## Description:

Retrieves recent public Xiaohongshu/Rednote notes, note details, creator posts, and comments through Guaikei command-line tools for trend monitoring, content research, competitor analysis, KOL screening, and comment insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, content creators, operators, and analysts use this skill to collect structured public Xiaohongshu/Rednote data for topic discovery, competitor monitoring, creator research, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note URLs, creator URLs, and requested limits to guaikei.com.

Mitigation: Install and run it only when that data sharing is acceptable for the user's environment and authorization scope.

Risk: The skill can collect broad public datasets and save full returned results locally under logs/.

Mitigation: Use explicit, narrow limits, avoid collecting unnecessary comments or account histories, and review or delete local logs according to data-handling requirements.

Risk: GUAIKEI_API_TOKEN is required for all data calls.

Mitigation: Treat the token as a secret and avoid exposing it in prompts, command output, logs, or shared configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-growth)
- [Guaikei service website](https://www.guaikei.com)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Structured JSON printed to stdout, with matching JSON results saved under logs/ when commands succeed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command inputs include keywords, Xiaohongshu note or creator URLs, filters, sorting, time windows, and result limits.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
