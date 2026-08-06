## Description: <br>
Report Builder helps agents turn detailed plans or source material into decision-oriented executive briefings using BLUF structure, audience adaptation, templates, and local quality-check scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dabin0927](https://clawhub.ai/user/dabin0927) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external collaborators, and agents use this skill to create CEO, board, investor, and management briefings that put conclusions, evidence, risks, and recommended actions first. It is suited to one-page executive summaries, decision memos, board briefings, and investor one-pagers, not technical documentation, chart-heavy analysis, or slide layout. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad report and briefing triggers may activate the skill for requests that only loosely match executive-report work. <br>
Mitigation: Review whether the user is actually asking for an executive briefing, decision memo, board briefing, or one-pager before applying the workflow. <br>
Risk: A workflow may request external research through digital-research, which could expose sensitive internal report context if used carelessly. <br>
Mitigation: Confirm with the user before allowing external research for internal, confidential, or sensitive reports, and limit shared context to what is necessary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dabin0927/skills/executive-briefing) <br>
- [Collaboration Workflow](references/collaboration-workflow.md) <br>
- [Edge Cases](references/edge-cases.md) <br>
- [Narrative Methodology](references/narrative-methodology.md) <br>
- [Structure Validation](references/structure-validation.md) <br>
- [Style Guide](references/style-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports and HTML-ready Markdown, with optional JSON quality reports from validation scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces executive-summary, decision-memo, one-pager, and board-briefing templates; local scripts can initialize, validate, score density, renumber, and bump report versions.] <br>

## Skill Version(s): <br>
2.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
