## Description: <br>
Analyzes changesets with risk scoring, categorization by type and impact, and release note preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to analyze git diffs, configuration changes, API migrations, schema updates, or document revisions, then categorize changes, assess risk, and prepare review or release-note summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad change or impact-analysis requests. <br>
Mitigation: Narrow trigger phrases before deployment if broad activation would disrupt normal agent workflows. <br>
Risk: Risk scoring and release-note summaries may be incomplete or misleading if the compared baseline or diff scope is wrong. <br>
Mitigation: Confirm the baseline, changed-file scope, and relevant test coverage before relying on the generated analysis. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-imbue-diff-analysis) <br>
- [Configured Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>
- [sem Entity Diff Tool](https://github.com/Ataraxy-Labs/sem) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or structured text with optional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes semantic change categories, risk levels, mitigation suggestions, review focus areas, and release-note or changelog-ready summaries.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
