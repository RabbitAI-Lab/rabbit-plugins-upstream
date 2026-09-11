## Description:

Stellar Trails provides an opinionated agent workflow controller for coding, document, data, visualization, and planning tasks using phased gates, traceability IDs, scope commitments, and verification steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to impose a structured workflow on coding, document, data processing, visualization, and multi-step planning tasks. It is intended for users who want traceability, approval gates, and verification discipline across broad agent work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad workflow authority and can run shell setup, start a local server, write persistent state, perform web retrieval, and manage GitHub operations.

Mitigation: Review the skill before installation, use it only where an opinionated workflow controller is desired, and require explicit approval for sensitive operations.

Risk: GitHub credential handling may store or reuse credentials during git operations.

Mitigation: Use short-lived fine-grained credentials instead of a broad PAT, avoid using the skill in sensitive repositories, and check for stored credentials after git operations.

Risk: Persistent logs, worklogs, memory, local services, process behavior, and arbitrary URL fetching can expose workspace context or affect the local environment.

Mitigation: Use the skill in a non-sensitive workspace unless these behaviors are removed, sandboxed, or tightly approved by the user.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [Security Policy](artifact/references/SECURITY.md)
- [Workflow Phases](artifact/procedure/phases.md)
- [Architecture](artifact/knowledge/architecture.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured workflow reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include traceability IDs, phase markers, approval gates, verification reports, and command suggestions.]

## Skill Version(s):

9.17.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
