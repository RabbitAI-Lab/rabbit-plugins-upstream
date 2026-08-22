## Description:

This skill helps agents collect public Douyin trend, search, creator-post, and comment data through Node.js CLI commands and return structured JSON for content research, competitor analysis, and hotspot monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content analysts use this skill to research Douyin public trends, benchmark creators, gather comment feedback, and prepare ranking or marketing reports from structured public-data results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Douyin URLs, result data, comments, user IDs, and IP-region labels may be sent to guaikei.com and saved locally in JSON logs.

Mitigation: Use the skill only for intentional Douyin public-data collection, keep limits small, protect GUAIKEI_API_TOKEN, and store or share collected data only for lawful and appropriate uses.

Risk: Broad activation guidance may cause the skill to run for general trend or competitor-analysis prompts that do not explicitly mention Douyin.

Mitigation: Confirm that the user wants Douyin public-data collection before running search, post, comment, or hot-ranking commands.

Risk: Large public comment or account datasets could be collected and redistributed inappropriately.

Mitigation: Avoid collecting or redistributing comment and account datasets unless the use is lawful, appropriate, and limited to the minimum data needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-trending-to-ranking-report)
- [Publisher Profile](https://clawhub.ai/user/engheng-art)
- [Options Reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [CLI JSON Schemas](artifact/assets/)
- [Guaikei Token and Help Site](https://www.guaikei.com)
- [Repository Listed In Skill Metadata](https://github.com/um-why/douyin-search-openclaw)

## Skill Output:

**Output Type(s):** [JSON, shell commands, configuration, guidance]

**Output Format:** [Structured JSON on stdout with status messages on stderr]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; result logs are saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: release evidence, package.json, changelog, and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
