## Description:

Detect, fix, and prevent WCAG 2.2 violations in web pages. Use when: (1) auditing for accessibility, (2) fixing axe/pa11y/W3C/QualWeb failures, (3) writing accessible HTML/CSS, (4) running the AI-WCAG-Gauntlet benchmark loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[turbolego](https://clawhub.ai/user/turbolego)

### License/Terms of Use:

MIT

## Use Case:

Developers, accessibility auditors, and benchmark maintainers use this skill to audit web pages for WCAG 2.2 issues, fix HTML/CSS accessibility failures, and build accessible pages from the start.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install and run Node, Python, browser automation, global npm packages, and local HTTP servers during accessibility audits.

Mitigation: Review commands before execution, run them in a scoped workspace, and inspect generated reports and page edits before relying on the results.

Risk: The bundled passing template can invalidate AI-WCAG-Gauntlet benchmark results if copied as a submission.

Mitigation: Use bundled templates as reference material only, and build benchmark pages from scratch in the run folder.

Risk: Automated validators can disagree or surface cascading failures after malformed HTML.

Mitigation: Triage W3C structure issues first, review the union of validator reports, fix iteratively, and rerun validators after each repair pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/turbolego/skills/wcag-skill)
- [Skill homepage](https://github.com/turbolego/wcag-skill)
- [AI-WCAG-Gauntlet benchmark harness](https://github.com/turbolego/AI-WCAG-Gauntlet)
- [AI-WCAG-Gauntlet iteration log](references/ai-wcag-gauntlet-iteration-log.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce validator commands, report triage steps, accessibility fixes, benchmark-loop guidance, and HTML/CSS/JavaScript snippets.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
