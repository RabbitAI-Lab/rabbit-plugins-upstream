## Description: <br>
Updates documentation after code changes with quality gates, slop detection, and accuracy checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use this skill after code changes to update READMEs, plans, wikis, docstrings, ADRs, and capability documentation while checking style, consistency, and accuracy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger words may activate the skill during general documentation or writing tasks. <br>
Mitigation: Confirm the intended documentation-update scope before allowing the workflow to edit files. <br>
Risk: Consolidation steps can propose deletion, merging, splitting, or staging of documentation files. <br>
Mitigation: Review consolidation tables, use selective or dry-run mode for cleanup, and approve destructive actions explicitly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-doc-updates) <br>
- [Claude Night Market sanctum plugin](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with command snippets, review tables, and documentation edits] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose consolidation, deletion, or staging actions that require user review or approval.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
