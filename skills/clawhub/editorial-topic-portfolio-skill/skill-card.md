## Description: <br>
Evaluate a portfolio of technology, AI, data, cloud, or enterprise-software content topics. Normalizes Notion or Markdown/JSON/CSV inputs, applies factual, timeliness, originality, argument-capacity, positioning, and privacy gates, scores eligible topics, selects one primary and two backups, produces merge/watch/covered/abandon decisions, and prepares a confirmed Notion writeback preview. Never writes to Notion without two explicit confirmations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Editors, analysts, and content strategists use this skill to evaluate technology, AI, data, cloud, or enterprise-software topic portfolios, select one primary topic plus two backups, and prepare reviewed Notion change previews without drafting the article body. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access a configured Notion topic database and related credential environment variables. <br>
Mitigation: Use only the intended Notion database, keep tokens and private mappings outside the skill directory, and confirm that the access scope is acceptable before installation. <br>
Risk: Unreviewed writeback could change topic records before the user has accepted the portfolio decision. <br>
Mitigation: Review the generated change preview and enable live writeback only after both the portfolio confirmation and the writeback confirmation. <br>
Risk: Topic recommendations can be misleading when facts, dates, product status, policy status, or originality are not verified. <br>
Mitigation: Apply the G0-G5 gates, re-check source evidence, and exclude blocked or unresolved topics from the primary and backup selections. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/editorial-topic-portfolio-skill) <br>
- [Evaluation Gates](references/evaluation-gates.md) <br>
- [Scoring Model](references/scoring-model.md) <br>
- [Portfolio Rules](references/portfolio-rules.md) <br>
- [Notion Adapter Interface](references/notion-adapter-interface.md) <br>
- [Replay Evaluation](references/replay-evaluation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, JSON records and change sets, configuration examples, and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include gate results, scores, portfolio decisions, change previews, validation records, writeback results, and readback verification; live Notion writeback requires explicit confirmations.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
