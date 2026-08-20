## Description:

This skill helps agents retrieve public Xiaohongshu note, comment, and creator-post data for trend tracking, content research, competitive analysis, and KOL review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, marketers, and analysts use this skill to search Xiaohongshu public notes, inspect note details and comments, and monitor public creator posts. Agents use it when a workflow needs recent Xiaohongshu topic signals, competitor content review, comment analysis, or candidate KOL screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note links, profile links, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use the skill only when third-party API submission is acceptable, configure the token through the environment, and avoid submitting non-public or sensitive links.

Risk: Returned comments, profile data, and interaction results may be saved locally under logs/.

Mitigation: Treat generated logs as potentially personal data and delete or restrict access to them when local retention is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-pick-hot)
- [engheng-art publisher profile](https://clawhub.ai/user/engheng-art)
- [GUAIKEI API service](https://www.guaikei.com)
- [Usage options](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful runs may also write JSON result logs under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and package metadata report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
