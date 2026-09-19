## Description:

Queries Douyin public content through command-line tools for keyword-ranked videos and posts, real-time hot lists, creator posts, and video comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and content operations teams use this skill to retrieve structured Douyin public-content data for trend discovery, competitor monitoring, topic research, and comment analysis. It requires Node.js and a GUAIKEI_API_TOKEN before API-backed commands can run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin queries, URLs or IDs, and the GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use only when that external API use is approved, keep the token in a protected environment variable, and rotate it if exposure is suspected.

Risk: Fetched public content can be saved locally in plaintext logs.

Mitigation: Run in a protected workspace, avoid shared or synced directories for sensitive analyses, and clean up generated logs after use.

Risk: The claimed seven-day like-surge TOP1000 ranking is not fully substantiated in the security evidence.

Mitigation: Treat ranking results as API-provided operational data and verify the calculation method with the publisher before making high-impact decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-keyword-surge)
- [Server-resolved GitHub repository](https://github.com/why20261/douyin-keyword-surge)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [GUAIKEI API provider](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples; runtime commands return JSON on stdout and may write local JSON logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; stderr is used for logs and status messages.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact changelog and package metadata contain different internal versions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
