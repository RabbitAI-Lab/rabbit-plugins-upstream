## Description:

Sweeping Monk provides research and academic strategy guidance for methodology, study design, critical thinking, stuck-point diagnosis, scholarly communication, and cross-disciplinary research-method selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, students, reviewers, and academic writers use this skill to diagnose research-design problems, select suitable methods, critique arguments, shape literature-review or manuscript structure, and decide when to delegate literature search or citation verification to other tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill defaults to local signal logging and anonymous cloud upload.

Mitigation: Review telemetry expectations before installation and use the documented opt-out phrases before normal use if logging or upload is not acceptable.

Risk: The skill can maintain persistent cross-session profile notes.

Mitigation: Review stored profile notes and clear or disable them where privacy or data-minimization requirements apply.

Risk: The proposal workflow can use local credentials and edit skill files.

Mitigation: Inspect proposal contents, affected files, and diffs before applying updates, and keep creator tokens outside the packaged skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/j-levee/skills/sweeping-monk)
- [Research Playbook](references/research-playbook.md)
- [Method Matrix](references/method-matrix.md)
- [Cognitive Apprenticeship](references/cognitive-apprenticeship.md)
- [Double-Loop Learning](references/double-loop.md)
- [Researcher Reasoning Biases](references/reasoning-biases.md)
- [Signals Specification](references/signals.md)
- [Security Audit](references/security-audit.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code, shell commands, configuration]

**Output Format:** [Markdown and plain text guidance with optional code, shell command, or configuration snippets when the user asks for implementation work.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory-first output; literature retrieval and citation verification are delegated to recommended specialist skills.]

## Skill Version(s):

1.9.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
