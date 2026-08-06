## Description: <br>
Runs a three-tier codebase audit using git-history analysis, targeted area review, and gated full-codebase review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to audit codebase quality, branch changes, instability, churn, and pre-PR readiness with escalating levels of review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers such as "review" may invoke this workflow when a narrower review workflow was intended. <br>
Mitigation: Confirm the intended audit scope before running and use a narrower review workflow for single-file, architecture-only, or single-commit reviews. <br>
Risk: A full-codebase Tier 3 audit can consume significant compute and context if it is started without a strong reason. <br>
Mitigation: Require documented Tier 2 justification and explicit user approval before Tier 3, then process areas sequentially. <br>
Risk: Git-history evidence can be incomplete or misleading if the base branch or commit range is wrong. <br>
Mitigation: Verify the base resolves correctly and confirm each Tier 1 command produces expected output before escalating. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-tiered-audit) <br>
- [Project homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown findings files with evidence summaries and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local tiered audit findings under .coordination/agents; Tier 3 requires explicit approval.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
