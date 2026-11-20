## Description:

Creates or connects a workspace standards library, drafts proposals from supplied material, applies decisions to current rules, and checks standards and code for conflicts or outdated guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterflow-zh](https://clawhub.ai/user/peterflow-zh)

### License/Terms of Use:

MIT

## Use Case:

Developers and teams use the skill to establish or maintain workspace standards, turn review material into proposals, apply approved changes, and inspect rules for conflicts or staleness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and could not resolve some local references, so their contents were not assessed.

Mitigation: Check whether the unresolved references matter to your use and inspect them before relying on their guidance.

Risk: A proposed standards change could introduce incorrect or misleading guidance if applied without review.

Mitigation: Have the responsible owner review and decide on proposals before applying them; apply only decisions and write scopes that are clearly authorized.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/peterflow-zh/skills/maintain-standards)
- [Initialize or connect a standards library](references/init.md)
- [Draft a standards proposal](references/draft.md)
- [Apply an approved standards change](references/apply.md)
- [Check current standards](references/check.md)
- [Current standards template](assets/standard.md)
- [Proposal template](assets/candidate.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown standards, candidate proposals, and findings in the conversation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workspace file changes are limited to the authorized scope; checks are read-only.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
