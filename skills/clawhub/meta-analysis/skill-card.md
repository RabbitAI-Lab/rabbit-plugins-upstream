## Description: <br>
Meta Analysis Strip V180 is a bilingual, R-based agent skill that helps clinical researchers and analysts plan meta-analyses and systematic-review workflows while producing reproducible R code, figures, tables, and Markdown summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[medstatstar](https://clawhub.ai/user/medstatstar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, clinical researchers, and statistical analysts use this skill in chat to select appropriate meta-analysis workflows, preview or run local R analyses after confirmation, and generate reproducible outputs for review. It is intended to support evidence synthesis work, not to replace clinical or regulatory judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can propose or run local R code and create analysis files in the current project. <br>
Mitigation: Review generated R code and expected output paths before confirming execution. <br>
Risk: The security review notes conflicting treatment of patient-level or regulated clinical data. <br>
Mitigation: Do not provide regulated clinical data unless data-handling controls, generated code, and output locations have been reviewed. <br>
Risk: The skill asks to read ~/.workbuddy/MEMORY.md, which may contain unrelated sensitive information. <br>
Mitigation: Inspect or restrict that memory file before allowing the skill to read it. <br>
Risk: Package installation and PDF downloads may use the network. <br>
Mitigation: Keep package installs and PDF downloads manual and explicit, using trusted sources and only user-approved DOI or PMID lists. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/meta-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/medstatstar) <br>
- [Project homepage](https://github.com/medstatstar/meta-analysis) <br>
- [Interactive menu reference](references/interactive_menu.md) <br>
- [Reusable API reference](references/advanced_api.md) <br>
- [R package reference](references/r_packages.md) <br>
- [Data templates](references/data_templates.md) <br>
- [Systematic review workflow](references/review_workflow.md) <br>
- [Citation reference](references/citations.md) <br>
- [Language policy](references/language_policy.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with R code blocks and generated local analysis artifacts such as scripts, figures, CSV tables, and summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Safe preview is the default posture; local execution occurs only after user confirmation and may create project-local analysis files.] <br>

## Skill Version(s): <br>
1.8.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
