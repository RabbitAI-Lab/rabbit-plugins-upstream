## Description: <br>
Scores backlog items with RICE/WSJF/Kano and files GitHub issues for top candidates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product teams use this skill to inventory implemented features, score roadmap or backlog items with RICE, WSJF, and Kano criteria, identify gaps, and prepare prioritized suggestions or GitHub issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run a local deferred-capture script for skipped high-scoring suggestions without a separate prompt. <br>
Mitigation: Install it only in repositories where the deferred-capture script is understood, and review or disable deferred capture before using suggestion workflows. <br>
Risk: The issue creation workflow can publish recommendations to GitHub when --create-issues is used. <br>
Mitigation: Use --create-issues only after reviewing accepted suggestions, labels, target repository permissions, and any local backlog persistence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-feature-review) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>
- [Classification System](modules/classification-system.md) <br>
- [Configuration](modules/configuration.md) <br>
- [Multi-Metric Evaluation Methodology](modules/multi-metric-evaluation-methodology.md) <br>
- [Research Enrichment](modules/research-enrichment.md) <br>
- [Scoring Framework](modules/scoring-framework.md) <br>
- [Tradeoff Dimensions](modules/tradeoff-dimensions.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables, suggestion reports, GitHub issue drafts, shell commands, and YAML configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can optionally enrich scores with research evidence and can create GitHub issues when the user selects that workflow.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
