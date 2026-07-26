## Description: <br>
Refreshes README structure and content using repo context and exemplar research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use this skill to restructure a README after meaningful project changes, using repository context, language detection, exemplar research, and review steps to guide edits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad documentation and research triggers may activate the workflow for requests that are not intended to update a README. <br>
Mitigation: Confirm the target file and README scope before allowing edits. <br>
Risk: README restructuring can introduce inaccurate claims, stale links, or misleading guidance. <br>
Mitigation: Review the README diff, verify links and citations, and keep claims grounded in repository evidence before relying on the output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-update-readme) <br>
- [Sanctum plugin homepage from metadata](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>
- [Language Audit Patterns](modules/language-audit.md) <br>
- [Exemplar Research Patterns](modules/exemplar-research.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown prose, README edits, command snippets, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May edit README.md or a specified documentation file and may include citations from exemplar research.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
