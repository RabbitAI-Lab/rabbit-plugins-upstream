## Description: <br>
Budget Optimizer helps agents allocate influencer or paid-ad budgets across tiers, platforms, and content types, with ROI projections, scenario comparisons, and mid-campaign reallocation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams and agents use this skill to split campaign budgets across influencer tiers, platforms, content types, and paid-ad channels, compare budget scenarios, and document recommendations for execution or reallocation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Campaign budget inputs, chosen scenarios, tier mix, constraints, and planning outputs may be written to agent memory files for later reuse. <br>
Mitigation: Avoid confidential financial details unless the workspace memory handling is appropriate, and review saved memory before reuse. <br>
Risk: Benchmark-based cost, ROI, CPM, CPE, and reach projections may be mistaken for measured campaign performance. <br>
Mitigation: Label metrics as Measured, User-provided, or Estimated, and verify recommendations against current rates or analytics before making budget decisions. <br>


## Reference(s): <br>
- [Budget Optimizer ClawHub Page](https://clawhub.ai/aaron-he-zhu/skills/budget-optimizer) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Budget Optimizer Templates](references/templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Files] <br>
**Output Format:** [Markdown allocation tables, projections, scenario comparisons, and handoff summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save scoped planning outputs to memory paths when used by a compatible agent host.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
