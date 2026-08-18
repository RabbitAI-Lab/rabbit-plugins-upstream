## Description:

Collects public Xiaohongshu keyword search results, note details, comments, and creator posts as structured JSON for downstream analysis and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content, marketing, and data-analysis teams use this skill to retrieve public Xiaohongshu content data for topic research, competitor monitoring, KOL screening, comment analysis, and internal reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a third-party Guaikei API token to retrieve Xiaohongshu public data.

Mitigation: Use a dedicated token stored in the environment, avoid exposing it in prompts or logs, and rotate or revoke it if it is shared accidentally.

Risk: Fetched Xiaohongshu results are saved to local log files, which may retain sensitive research or competitive-analysis context.

Mitigation: Run the skill in an appropriate workspace and clean the logs directory after sensitive research tasks, especially on shared machines.

Risk: The skill is intended for public Xiaohongshu data and internal analysis, not private content access, publishing, interaction, or redistribution.

Mitigation: Use it only with public links or keywords, do not use it for account actions, and confirm authorization before sharing exported results outside the team.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/engheng-art/skills/guaikei-xiaohongshu-multi-data-tool)
- [Guaikei API token support](https://www.guaikei.com)
- [Options and invocation reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Markdown, Guidance]

**Output Format:** [JSON results from Node.js CLI commands, with agent guidance for downstream summaries, comparisons, and reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful command results are also written to local logs.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
