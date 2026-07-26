## Description: <br>
Generates or remediates documentation with human-quality writing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, and documentation maintainers use this skill to draft new documentation or remediate existing documentation and comments so they lead with a clear thesis, avoid AI-writing markers, and preserve the intended meaning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad writing or polish requests. <br>
Mitigation: Confirm the target files, document type, audience, thesis, and requested mode before drafting or remediation. <br>
Risk: The skill can read a local .scribe style profile. <br>
Mitigation: Treat the style profile as local project context and avoid exposing sensitive profile content in generated documentation. <br>
Risk: The skill can edit documentation or comment text during remediation. <br>
Mitigation: Review diffs before accepting changes, preserve technical meaning, and limit code-file changes to docstrings or comments. <br>
Risk: Generated or remediated documentation may introduce inaccurate or misleading guidance. <br>
Mitigation: Run the documented slop detector and quality gates, verify commands, paths, versions, and links, and require user approval before finalization. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-doc-generator) <br>
- [Claude Night Market scribe plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>
- [Generation guidelines module](artifact/modules/generation-guidelines.md) <br>
- [Quality gates module](artifact/modules/quality-gates.md) <br>
- [Remediation workflow module](artifact/modules/remediation-workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown prose, checklists, inline shell commands, and documentation or comment edits.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can apply a local .scribe style profile when available and can propose or perform documentation and comment remediation when requested.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
