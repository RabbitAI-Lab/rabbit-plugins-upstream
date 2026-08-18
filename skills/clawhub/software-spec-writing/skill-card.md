## Description:

Helps agents create and maintain software project specifications with a strict spec-first workflow, coverage tracking, dependency checks, and safeguards against unsupported assumptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jivecheng](https://clawhub.ai/user/jivecheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product managers, and engineering teams use this skill to write or update software requirements, PRDs, architecture notes, ADRs, API specs, acceptance criteria, and related project specifications. It is especially suited to spec-first workflows that need auditable coverage status and controlled follow-up when information is missing or unconfirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can strongly shape project documentation and development flow by enforcing a strict spec-first process.

Mitigation: Use it only for teams that want this workflow, and review generated or updated specifications before treating them as implementation guidance.

Risk: The skill expects teams to work with Traditional Chinese specification materials.

Mitigation: Confirm reviewers can read the generated documents or adapt the language expectations before relying on the skill.

Risk: Long-lived specification files can become misleading if coverage status and affected sections are not maintained with each change.

Mitigation: Require agents to update the coverage file, preserve missing or TBD states, and report affected sections after each documentation change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jivecheng/skills/software-spec-writing)
- [Consideration item list](artifact/references/chapters.md)
- [Writing conventions](artifact/references/conventions.md)
- [Coverage file guidance](artifact/references/coverage.md)
- [Glossary](artifact/references/glossary.md)
- [Coverage template](artifact/assets/spec-coverage.template.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown specification documents, YAML coverage/configuration files, and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains project specifications incrementally and reports changed, affected, and still-missing specification areas.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
