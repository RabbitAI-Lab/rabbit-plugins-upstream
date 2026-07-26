## Description: <br>
Updates documentation after code changes with quality gates, slop detection, and accuracy checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical writers use this skill to update README files, plans, wikis, ADRs, and docstrings after code changes. It helps identify documentation targets, apply grounded edits, run style and accuracy checks, and preview the resulting changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documentation edits or consolidation steps may remove or change useful content. <br>
Mitigation: Review proposed deletions, merges, staged changes, and previews before accepting the workflow output. <br>
Risk: Broad activation triggers such as writing may invoke the workflow outside focused documentation tasks. <br>
Mitigation: Invoke the skill explicitly or narrow activation to documentation update work when broad triggers are inconvenient. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-doc-updates) <br>
- [Declared homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>
- [Accuracy scanning module](modules/accuracy-scanning.md) <br>
- [Capabilities sync module](modules/capabilities-sync.md) <br>
- [Directory style rules module](modules/directory-style-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and file-edit guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose documentation edits, validation warnings, consolidation actions, and change previews.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
