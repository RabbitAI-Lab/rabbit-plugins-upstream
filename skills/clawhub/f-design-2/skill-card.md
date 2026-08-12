## Description:

Frontend design and production engineering orchestrator that inventories projects, scales design depth, presents review artifacts, locks executable contracts, implements accessible responsive interfaces, and verifies interactions, visual regressions, and performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[grubbylee](https://clawhub.ai/user/grubbylee)

### License/Terms of Use:

MIT

## Use Case:

Developers and product engineers use this skill to guide agents through frontend design, implementation, preview, and QA workflows for web apps, dashboards, landing pages, redesigns, responsive UI, and design reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Preview and browser QA helpers can run local project commands and inspect local applications.

Mitigation: Run preview and QA commands only in trusted projects and review generated reports before acting on them.

Risk: The cross-AIDE sync helper replaces managed design-guide directories under local AIDE skill folders.

Mitigation: Use cross-AIDE sync only when those managed copies are intended to be overwritten, and keep private preferences outside the skill folder.

## Reference(s):

- [Server-resolved source repository](https://github.com/GrubbyLee/f-design)
- [ClawHub skill page](https://clawhub.ai/grubbylee/skills/f-design-2)
- [Design process](references/design-process.md)
- [Artifact presentation](references/artifact-presentation.md)
- [Implementation contract](references/implementation-contract.md)
- [Product design review](references/product-design-review.md)
- [Quality gates](references/quality-gates.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code blocks, JSON contracts, shell commands, and generated or modified project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local preview sessions, .codex design artifacts, design contracts, QA reports, screenshots, and visual diffs when the host environment permits.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence; artifact VERSION and design-guide.json declare 0.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
