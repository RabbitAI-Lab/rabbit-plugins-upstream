## Description: <br>
订阅摘要(免费版) helps an agent use the local feed CLI to fetch RSS/Atom entries, scan unread items, filter by keywords, generate concise reading digests, and mark selected entries as read. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage personal RSS reading workflows, reduce information overload, and produce lightweight summaries from unread subscription entries. It is suitable for routine reading assistance, not critical decisions requiring deterministic results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can fetch RSS content from the network through a local feed CLI. <br>
Mitigation: Install and run it only in environments where network RSS fetching is expected, and review the feed CLI source or Homebrew tap before use. <br>
Risk: The skill can read subscription entries and mark selected entries as read. <br>
Mitigation: Use it with feeds where exposing titles, content, and read state to the agent is acceptable, and review entry selections before marking items read. <br>
Risk: The free edition uses keyword-based filtering and lightweight summaries that may miss important items or over-rank irrelevant ones. <br>
Mitigation: Tune keyword lists, inspect the original entries, and avoid relying on the digest for decisions that require complete or deterministic review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feed-digest-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Detailed reference](references/detail.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, Python examples, and optional JSON-style result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on local feed CLI state, configured RSS sources, network access, and keyword filtering settings.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
