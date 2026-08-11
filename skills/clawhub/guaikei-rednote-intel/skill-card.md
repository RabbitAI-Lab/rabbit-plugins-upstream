## Description:

Routes Xiaohongshu/Rednote keywords, note links, profile links, and short links to command-line API calls for public note search, note details, comments, and creator post lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, content operators, and analysts use this skill to retrieve structured public Xiaohongshu/Rednote data for content research, competitor monitoring, KOL screening, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, links, xsec_token-bearing URLs, and the GUAIKEI API token are sent to guaikei.com.

Mitigation: Use the skill only with data approved for that service, avoid private or sensitive links, and rotate the API token if exposure is suspected.

Risk: Successful outputs are saved locally under logs/.

Mitigation: Review log contents, restrict access to the workspace, and delete logs when results include sensitive business research.

Risk: Private, deleted, invalid, or unsupported Xiaohongshu targets can return empty or error results.

Mitigation: Check status and error_code before analysis, then request corrected public inputs instead of inferring missing data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-intel)
- [Guaikei Website](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI commands return structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful command outputs may also be saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
