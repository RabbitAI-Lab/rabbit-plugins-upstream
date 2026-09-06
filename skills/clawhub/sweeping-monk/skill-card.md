## Description:

Sweeping Monk is an academic research advisor skill that helps users diagnose research-methodology problems, improve study design, apply critical thinking, unblock academic writing, and route literature search or citation verification to specialist skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, graduate students, academic writers, and research-support agents use this skill for methodology selection, research design critique, root-cause diagnosis, reviewer-response planning, and disciplined reasoning about scholarly work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill keeps local usage or profile state and may upload method-level telemetry to the configured cloud service.

Mitigation: Review the local and cloud opt-in settings before use, disable local recording or cloud upload when inappropriate, and avoid using the skill in contexts where even method-level telemetry is not acceptable.

Risk: The bundled upload and proposal tooling can communicate with configured cloud endpoints and support proposal-driven edits.

Mitigation: Do not run upload, registration, proposal review, or proposal approval commands unless you intend to use those workflows; review proposed changes and diffs before applying them.

Risk: Creator workflows may use local creator tokens outside the published package.

Mitigation: Keep creator tokens in private local development storage, avoid shared workspaces for creator operations, and confirm tokens are not packaged with the skill.

## Reference(s):

- [Skill overview](references/intro.md)
- [Research methodology playbook](references/research-playbook.md)
- [Method matrix](references/method-matrix.md)
- [Cognitive apprenticeship](references/cognitive-apprenticeship.md)
- [Double-loop learning](references/double-loop.md)
- [Researcher reasoning biases](references/reasoning-biases.md)
- [Signal specification](references/signals.md)
- [ClawHub skill page](https://clawhub.ai/j-levee/skills/sweeping-monk)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional code, shell commands, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory-first; uses implementation tools only when the user explicitly asks for hands-on work.]

## Skill Version(s):

1.12.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
