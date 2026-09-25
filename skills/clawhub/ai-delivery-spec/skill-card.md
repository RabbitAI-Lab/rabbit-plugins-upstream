## Description:

Clarify, create, review or change product, service and office workflow requirements, PRDs and interactive prototypes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

Apache-2.0

## Use Case:

Product, business, design, engineering, QA and agent users use this skill to turn vague goals, existing materials or change requests into clear requirements, PRDs, interactive prototypes, acceptance criteria and handoff guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Python validation commands inspect local requirement and prototype files.

Mitigation: Install from a versioned release when possible, review commands before running them, and run validators only on files intended for inspection.

Risk: Requirement artifacts can contain private business material or credentials if users include them.

Mitigation: Avoid placing real credentials in requirement artifacts or environment variables, and keep private project inputs out of public examples or releases.

Risk: Generated PRDs, prototypes and acceptance guidance can be wrong when source authority, decisions or unknowns are unresolved.

Mitigation: Review source authority, unresolved decisions and validation scope before using outputs for implementation, deployment or customer acceptance.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/franklinxkk/skills/ai-delivery-spec)
- [Version 5.5.1 release](https://github.com/franklinxkk/ai-delivery-spec/releases/tag/v5.5.1)
- [README](README.md)
- [Discovery guide](references/discover.md)
- [Specification guide](references/specify.md)
- [Prototype guide](references/prototype.md)
- [Review workspace guide](references/review-workspace.md)
- [Change and acceptance guide](references/change-acceptance.md)
- [Validation record](maintainer/evals/evidence/v551-validation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, structured requirement artifacts, prototype files, shell commands and configuration snippets as needed by the task]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include requirement cards, PRDs, review notes, interactive prototype HTML, acceptance criteria, handoff manifests or validator command suggestions.]

## Skill Version(s):

5.5.1 (source: server release metadata, README, SKILL.md H1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
