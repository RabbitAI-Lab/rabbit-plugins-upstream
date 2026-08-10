## Description:

xhs-content-scan helps agents search Xiaohongshu public notes by keyword, retrieve note details and comments, and monitor public author posts for competitive content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, brand marketers, market analysts, and agents use this skill to collect structured Xiaohongshu public-content data for topic research, competitor monitoring, comment review, KOL screening, and report preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note/profile URLs, and the GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only when that third-party data sharing is acceptable, store the token in environment variables, and rotate the token if exposure is suspected.

Risk: Retrieved public-content results may be saved in local log files.

Mitigation: Review and remove sensitive or unnecessary log files before sharing a workspace, report, or generated output.

Risk: Bulk public-content collection may be subject to platform and organizational data-use rules.

Mitigation: Check applicable Xiaohongshu terms and internal data-use policies before high-volume collection or redistribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-content-scan)
- [GUAIKEI API service](https://www.guaikei.com)
- [Options and invocation reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON results from command execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; results are saved locally in logs.]

## Skill Version(s):

1.0.0 (source: server release evidence, artifact metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
