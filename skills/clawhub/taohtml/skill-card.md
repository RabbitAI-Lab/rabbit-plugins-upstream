## Description:

TaoHtml turns initial ideas, Word/PDF source material, existing slides, and HTML into polished 16:9 offline HTML reports and presentation-ready decks as a high-design alternative to PPT/PPTX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taogeo](https://clawhub.ai/user/taogeo)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and business teams use TaoHtml to turn source material or incomplete ideas into polished offline HTML reports and presentation-ready decks. The skill guides intake, material understanding, visual system selection, production authorization, local QA, and delivery handoff for portable 16:9 report artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent reusable corporate-template storage can retain brand assets across projects.

Mitigation: Review TAOHTML_HOME or ~/.taohtml before reuse and remove stale or unauthorized templates before running the skill.

Risk: The skill runs local Python tools on project files supplied for report production.

Mitigation: Use it only in an environment where local processing of those files is acceptable, and provide only files intended for the current task.

Risk: Dependency hygiene caveats may leave older allowed package versions in use.

Mitigation: Install patched dependency versions instead of the oldest versions accepted by requirements.

## Reference(s):

- [TaoHtml Skill Definition](SKILL.md)
- [Runtime Contract](references/runtime-contract.md)
- [Intake Workflow](references/intake-workflow.md)
- [Process Playbook](references/process-playbook.md)
- [Production Authorization](references/production-authorization.md)
- [Visual Systems](references/visual-systems.md)
- [Project Handoff](references/project-handoff.md)
- [Report IR v1](references/report-ir-v1.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with generated HTML/CSS/JavaScript files, JSON handoff records, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces offline 16:9 HTML reports or decks with local assets, QA checks, and a verification handoff.]

## Skill Version(s):

0.5.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
