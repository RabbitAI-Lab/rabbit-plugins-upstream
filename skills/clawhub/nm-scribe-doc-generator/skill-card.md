## Description: <br>
Generates or remediates documentation with human-quality writing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, and documentation maintainers use this skill to draft new documentation or remediate existing content with thesis-first structure, concrete claims, style constraints, and quality checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad writing-related triggers may cause the skill to activate for requests where a documentation workflow was not intended. <br>
Mitigation: Review when the skill is invoked and confirm that documentation generation or remediation is the intended task before allowing edits. <br>
Risk: Documentation remediation can change meaning when the original intent is unclear or when a rewrite restructures large sections. <br>
Mitigation: Preserve the stated meaning, ask for clarification when meaning is unclear, and require user approval before deleting sections, restructuring flow, or changing technical content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-doc-generator) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>
- [Generation Guidelines](artifact/modules/generation-guidelines.md) <br>
- [Quality Gates](artifact/modules/quality-gates.md) <br>
- [Remediation Workflow](artifact/modules/remediation-workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, prose edits, checklists, and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or apply documentation rewrites; major changes require user confirmation under the artifact workflow.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
