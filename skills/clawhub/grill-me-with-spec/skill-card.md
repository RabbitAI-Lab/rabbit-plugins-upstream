## Description:

Use when the user needs to create or refine a feature SPEC SDD before implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill before implementation to clarify ambiguous feature, bugfix, refactor, API, infrastructure, frontend, or documentation requests. It interviews the user in Portuguese, gathers repository facts, and produces an SDD-style SPEC for review and approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository fact gathering can expose secrets, credentials, private configuration, or unrelated files if the working scope is too broad.

Mitigation: Before use, define the repository scope and tell the agent to avoid secrets, credentials, private configs, and unrelated directories.

Risk: A draft SPEC can encode incomplete or incorrect requirements if the Portuguese interview or repository facts are not reviewed.

Mitigation: Review the generated SPEC, resolve open questions, and require explicit approval before implementation begins.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/afonsoft/skills/grill-me-with-spec)
- [Publisher Profile](https://clawhub.ai/user/afonsoft)
- [Source Repository Metadata](https://github.com/afonsoft/skills)
- [SPEC SDD Template](references/spec-sdd-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Portuguese interview prompts and a Markdown SPEC SDD file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes `.specs/SPEC-{YYYYMMDD}-{feature}.md` as a draft SPEC and requires user approval before implementation.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact metadata reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
