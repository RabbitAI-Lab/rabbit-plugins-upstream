## Description: <br>
Scores backlog items with RICE/WSJF/Kano and files GitHub issues for top candidates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to inventory roadmap features, score backlog candidates, analyze tradeoffs, and prepare GitHub issues for accepted suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can instruct the agent to run a local deferred-capture script automatically after planning decisions. <br>
Mitigation: Use it only in repositories where the local deferred_capture.py behavior is trusted, or disable deferred capture and require explicit confirmation before any local write. <br>
Risk: Roadmap scores and suggested issues may be incomplete or misleading if feature inventory, confidence, or research inputs are weak. <br>
Mitigation: Review generated priorities and issue drafts before acting on them, especially low-confidence scores or changes that affect API surfaces. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/athola/skills/nm-imbue-feature-review) <br>
- [Source Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>
- [Classification System](modules/classification-system.md) <br>
- [Configuration](modules/configuration.md) <br>
- [Multi-Metric Evaluation Methodology](modules/multi-metric-evaluation-methodology.md) <br>
- [Research Enrichment](modules/research-enrichment.md) <br>
- [Scoring Framework](modules/scoring-framework.md) <br>
- [Tradeoff Dimensions](modules/tradeoff-dimensions.md) <br>
- [External Multi-Metric Evaluation Methodology](https://claude-night-market/plugins/abstract/skills/skills-eval/modules/multi-metric-evaluation-methodology.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, tables, issue drafts, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create GitHub issue content when explicitly requested and may trigger deferred local capture for skipped high-priority suggestions.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
