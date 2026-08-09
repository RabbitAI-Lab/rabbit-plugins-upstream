## Description: <br>
Aggregates configured RSS feeds, removes previously delivered items, and produces concise, information-dense Markdown briefings without emoji. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and automation users use this skill to collect reports from RSS feed lists, deduplicate against history, and generate Markdown briefings for information monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad read and command-execution capability for RSS aggregation. <br>
Mitigation: Install it only in an agent environment where read and command execution can be approved or restricted, and use it only for explicit RSS feed aggregation tasks. <br>
Risk: The scanner verdict is suspicious because the activation wording is broader than RSS use. <br>
Mitigation: Review the skill before installation and keep use scoped to configured RSS sources, deduplication, and briefing generation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/rss-aggregator) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown briefing, with optional HTML or JSON output when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [RSS feed URLs may be supplied directly or drawn from configuration; output is intended to be concise and emoji-free.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
