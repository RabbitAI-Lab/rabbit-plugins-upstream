## Description: <br>
Detect, fix, and prevent WCAG 2.2 violations in web pages through accessibility audits, validator triage, repair guidance, accessible markup practices, and the AI-WCAG-Gauntlet benchmark loop. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[turbolego](https://clawhub.ai/user/turbolego) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, QA engineers, and accessibility reviewers use this skill to audit web pages, interpret axe, pa11y, W3C, and QualWeb results, repair HTML/CSS accessibility issues, and run the AI-WCAG-Gauntlet benchmark workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill recommends global npm installs and browser setup commands that may affect managed development machines. <br>
Mitigation: Review installation commands with local machine policy before execution, and use an isolated environment when appropriate. <br>
Risk: Accessibility repair guidance can be incomplete if validator reports are skipped or interpreted manually from large JSON output. <br>
Mitigation: Run the documented validators over HTTP, read reports programmatically, and rerun validators after each fix cycle. <br>


## Reference(s): <br>
- [wcag-skill homepage](https://github.com/turbolego/wcag-skill) <br>
- [AI-WCAG-Gauntlet](https://github.com/turbolego/AI-WCAG-Gauntlet) <br>
- [AI-WCAG-Gauntlet Iteration Log](references/ai-wcag-gauntlet-iteration-log.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, configuration snippets, and file-oriented repair instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce validator command sequences, accessibility triage notes, HTML/CSS repair guidance, and benchmark template copy steps.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata; artifact frontmatter states 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
