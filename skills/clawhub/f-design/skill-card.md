## Description:

f-design orchestrates frontend design and production engineering workflows for agents, including project inventory, design depth selection, review artifacts, implementation contracts, accessible responsive UI work, and quality verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[grubbylee](https://clawhub.ai/user/grubbylee)

### License/Terms of Use:

MIT

## Use Case:

Developers and product engineers use f-design to guide agents through frontend design, redesign, UI review, implementation, and QA workflows across supported agent development environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The cross-AIDE synchronization script mirrors the source skill into target f-design folders and can remove files inside those targets.

Mitigation: Back up customized f-design copies before running synchronization, and use F_DESIGN_TARGET_HOME for a sandboxed test first.

## Reference(s):

- [f-design on ClawHub](https://clawhub.ai/grubbylee/skills/f-design)
- [Design Process](references/design-process.md)
- [Artifact Presentation](references/artifact-presentation.md)
- [Implementation Contract](references/implementation-contract.md)
- [State and Data Coverage](references/state-and-data.md)
- [Production Quality Gates](references/quality-gates.md)
- [Frontend Review Rubric](references/review-rubric.md)
- [Existing Product Design Review](references/product-design-review.md)
- [AIDE Integration](references/aide-integration.md)
- [Framework Adapters](references/framework-adapters.md)
- [Internationalization Contract](references/internationalization.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, configuration, shell command, JSON, and file-edit outputs as needed for frontend work.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify frontend project files and run local preview, synchronization, diagnostic, and verification commands when the user task calls for implementation or QA.]

## Skill Version(s):

0.1.1 (source: VERSION, f-design.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
