## Description: <br>
Analyzes changesets with risk scoring, categorization by type and impact, and release note preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to analyze git diffs, configuration changes, API migrations, schema updates, and document revisions. It helps categorize change types, assess impact and risk, and prepare review summaries, release notes, or changelogs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger terms may load the skill during generic change-summary conversations. <br>
Mitigation: Use it when structured diff, risk, changelog, or release-note analysis is intended, and review the generated assessment before using it for release decisions. <br>
Risk: The markdown skill references separate Night Market or Claude Code plugin functionality that is outside the inspected artifact. <br>
Mitigation: Review and scan any separate plugin, agent, hook, or command package before enabling behavior beyond this markdown skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-diff-analysis) <br>
- [Night Market imbue plugin](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>
- [sem entity-level diff tool](https://github.com/Ataraxy-Labs/sem) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown analysis with optional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces categorized change summaries, risk assessments, and release-note-ready summaries.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
