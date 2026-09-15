## Description:

Activates on every task: coding (features, bugs, refactoring, scripts), documents (reports, proposals, DOCX, PDF), charts and visualizations, data processing, complex multi-step planning, or even simple questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to impose a six-phase workflow with traceability, review gates, and delivery reporting across coding, document, visualization, data-processing, and planning tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run setup, update, or install commands and contact ClawHub or GitHub during its workflow.

Mitigation: Install only when this workflow enforcement is intended, review update and install behavior before deployment, and scan each release before use.

Risk: The skill starts a localhost server and can keep a persistent development process running.

Mitigation: Run it in a controlled sandbox, verify localhost-only binding and server lifecycle behavior, and stop or isolate the process when it is no longer needed.

Risk: The workflow can touch GitHub credentials and persistent state across sessions.

Mitigation: Use no GitHub token unless required, or use a narrowly scoped token; review credential handling and clear persistent state when continuity is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [Workflow phases](artifact/procedure/phases.md)
- [Error resolution procedure](artifact/procedure/error-resolution.md)
- [Enforcement vectors](artifact/knowledge/enforcement-vectors.md)
- [Code standards](artifact/constraints/code-standards.md)
- [Type safety standards](artifact/constraints/type-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, code blocks, shell commands, configuration snippets, and structured workflow reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs vary by task tier and may include phase markers, scope commitments, verification reports, file paths, and worklog snapshots.]

## Skill Version(s):

9.18.0 (source: evidence release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
