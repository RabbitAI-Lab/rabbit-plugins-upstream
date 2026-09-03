## Description:

Provides Vue 3 SPA state-management guidance for choosing and implementing component refs, props/emit, v-model, provide/inject, and Pinia stores by state scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[libo-123](https://clawhub.ai/user/libo-123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Vue 3 SPAs use this skill to decide where state should live and to apply Pinia, provide/inject, and component-state templates consistently.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying the guidance broadly without review could create unsuitable conventions for login state, tokens, or persistence.

Mitigation: Review the conventions against the Vue project's authentication and persistence requirements before adopting them across the codebase.

Risk: Generated state-management changes may be incorrect for an application's existing Pinia structure or component ownership boundaries.

Mitigation: Review proposed changes before merging and verify that state ownership, store dependencies, and persistence match the target application.

## Reference(s):

- [examples.md](examples.md)
- [ClawHub skill page](https://clawhub.ai/libo-123/skills/vue-spa-state)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code]

**Output Format:** [Markdown guidance with TypeScript and Vue code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
