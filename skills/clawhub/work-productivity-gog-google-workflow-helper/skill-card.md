## Description:

Helps agent users, skill authors, maintainers, and teams turn Gog-style Google Workspace workflow needs into practical plans, checklists, artifacts, analysis, or implementation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to adapt popular Gog-style work-productivity patterns into reliable workflows, bug-fix plans, setup hardening checklists, or adjacent skills. It is intended for practical local-friendly guidance rather than executing external tools itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad Google Workspace, CLI, or bug-fix wording.

Mitigation: Use explicit invocation or narrower trigger configuration when only Gog-style workflow planning is intended.

Risk: The skill produces planning, workflow, and implementation guidance that may be incomplete or unsuitable for a specific environment.

Mitigation: Review the generated artifact against the user's stated constraints and success criteria before applying changes.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper)
- [Gog demand signal](https://clawhub.ai/skills/gog)
- [Google Workspace adjacent issue signal](https://github.com/Expensify/App/issues/99500)
- [Community workflow demand signal](https://www.v2ex.com/t/1237284)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text guidance with optional code, shell command, checklist, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code is bundled; outputs should include assumptions, validation notes, and remaining risks when relevant.]

## Skill Version(s):

0.20260826.40329 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
