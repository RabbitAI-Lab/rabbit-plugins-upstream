## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification. v3.0 adds a dual-mode (the original iterate mode plus a defensive-programming mode via /iterate defensive) that performs normal incremental coding tasks with defensive discipline end-to-end.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill with an AI coding assistant to review and improve a codebase through repeated, multi-dimension review, fixes, and verification, or to complete incremental coding tasks with defensive checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Self-updates from editable checkouts may not verify the code that is actually installed.

Mitigation: Use a fixed, verified release and avoid editable-checkout self-updates until verification covers the installed code.

Risk: Some update and credential-handling paths exceed the stated security guarantees.

Mitigation: Select project and assistant targets explicitly, review validation commands, keep automatic merge and push disabled, and use publisher signing tools only when intentionally administering those repositories.

Risk: The security review was partial; future downloads and the separate harness and plugin remain unassessed.

Mitigation: Review those downloads and components separately before relying on them.

## Reference(s):

- [Iterate on ClawHub](https://clawhub.ai/jingzhao-l/skills/iterate-skill)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown summaries and reports, code and configuration changes, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project changes are made through the host coding assistant; review rounds can run in parallel across configured dimensions.]

## Skill Version(s):

3.10.0 (source: SKILL.md frontmatter, pyproject.toml, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
