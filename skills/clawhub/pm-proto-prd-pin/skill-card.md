## Description:

A zero-dependency, plug-and-play tool that adds interactive PRD pinning, markdown specification editing, multi-version management, and configurable persistence to HTML, Vue, React, and Next.js prototypes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[barry0-0](https://clawhub.ai/user/barry0-0)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers, designers, and engineers use this skill to add a PRD annotation layer to prototypes so reviewers can pin UI elements, write structured specifications, manage versions, and export PRD documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Off-site PRD synchronization can expose confidential prototype requirements when remote storage is used.

Mitigation: Install only in prototypes where off-site sync is acceptable, and avoid confidential PRD content unless the storage endpoints are controlled.

Risk: Install and verify/test flows can make live remote or local changes.

Mitigation: Review or modify the injector before running it on important project trees, use narrowly scoped throwaway API keys or PATs, and treat verify/test actions as potentially mutating.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/barry0-0/skills/pm-proto-prd-pin)
- [JSONBin.io](https://jsonbin.io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code snippets and injected JavaScript/CSS assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May copy files, modify prototype HTML or application entry files, start a local server, and configure cloud or local PRD persistence depending on the target project.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
