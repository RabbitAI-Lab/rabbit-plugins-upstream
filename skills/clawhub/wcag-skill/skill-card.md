## Description: <br>
Detect, fix, and prevent WCAG 2.2 violations in web pages. Use when: (1) auditing for accessibility, (2) fixing axe/pa11y/W3C/QualWeb failures, (3) writing accessible HTML/CSS, (4) running the AI-WCAG-Gauntlet benchmark loop. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[turbolego](https://clawhub.ai/user/turbolego) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to audit web pages for WCAG 2.2 issues, triage validator findings, apply accessible HTML/CSS fixes, and verify results. It also supports the AI-WCAG-Gauntlet benchmark loop with a reusable known-good template and tag-coverage helper. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on global Node-based accessibility validators and browser testing dependencies. <br>
Mitigation: Install and run the tools in a controlled agent environment, and confirm the expected binaries before using the workflow on target pages. <br>
Risk: Automated accessibility validators can produce incomplete, stale, or conflicting findings. <br>
Mitigation: Review axe, pa11y, W3C, QualWeb, and tag-coverage outputs together before applying fixes, then rerun the validators after changes. <br>
Risk: The workflow can audit local or served web pages and generate reports from their contents. <br>
Mitigation: Use it only on pages or benchmark folders intended for accessibility review, and inspect generated reports before sharing or applying remediation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/turbolego/skills/wcag-skill) <br>
- [wcag-skill repository](https://github.com/turbolego/wcag-skill) <br>
- [AI-WCAG-Gauntlet](https://github.com/turbolego/AI-WCAG-Gauntlet) <br>
- [AI-WCAG-Gauntlet Iteration Log](references/ai-wcag-gauntlet-iteration-log.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code snippets, configuration notes, and report-review steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or update HTML, CSS, JavaScript, JSON validator reports, and benchmark log content when used by an agent.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
