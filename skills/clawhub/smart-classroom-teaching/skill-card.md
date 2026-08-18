## Description:

Smart Classroom Teaching helps agents plan and run AI-assisted classroom workflows, including visual explanations, Socratic dialogue, classroom-record analysis, personalized tutoring, lesson-resource generation, and content and privacy checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

External educators, instructional designers, and classroom-support agents use this skill to generate lesson plans, visual explanations, Socratic prompts, classroom diagnostics, personalized tutoring flows, and reusable classroom workbench states.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Imported or pushed HTML/SVG classroom content may expose sensitive data when rendered in the workbench.

Mitigation: Use only trusted JSON histories and classroom content; avoid importing files from others and review or sanitize any SVG/HTML before use.

Risk: Exported histories and state.json can contain sensitive student records or classroom observations.

Mitigation: Treat these files as sensitive records, apply the skill's privacy-redaction workflow before sharing, and delete temporary state files when no longer needed.

Risk: The local workbench server accepts state updates and should not be exposed while browsing untrusted sites.

Mitigation: Run the server only on localhost for trusted classroom sessions and stop it when the session ends.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wangjiaocheng/skills/smart-classroom-teaching)
- [Smart classroom task catalog](references/smart-classroom-catalog.md)
- [Smart classroom requirements](references/smart-classroom-requirements.md)
- [Smart classroom exemplars index](references/smart-classroom-exemplars.md)
- [Smart classroom workbench](assets/smart-classroom-workbench.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown, JSON classroom state, optional SVG/HTML snippets, and shell commands for the local workbench server]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can degrade to read-only text outputs when file I/O, script execution, or external resources are unavailable.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
