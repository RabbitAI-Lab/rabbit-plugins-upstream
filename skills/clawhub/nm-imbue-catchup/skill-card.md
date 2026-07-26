## Description: <br>
Summarizes recent git changes for context recovery after session breaks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and team members use this skill to get up to speed after time away, handoffs, or session breaks by summarizing recent repository, document, meeting, sprint, or log changes into key changes, follow-ups, and open questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on generic status or progress requests and inspect private repositories or sensitive logs. <br>
Mitigation: Confirm the catch-up scope first and review the files, repositories, or logs the agent plans to inspect before analysis. <br>
Risk: Summaries of changes, logs, or documents may omit important details or produce misleading follow-up guidance. <br>
Mitigation: Require concise source references and review the summary before using it for planning, review, or handoff decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-catchup) <br>
- [Claude Night Market Imbue plugin](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown summary with optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses concise summaries, referenced paths or lines, and explicit follow-up items.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
