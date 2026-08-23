## Description:

Stores and applies explicit coding style preferences, conventions, and patterns locally for consistent code output without inference or external access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to remember confirmed coding preferences and apply them to future code-related responses. It is intended for explicit user corrections and confirmations, not passive inference from projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores confirmed coding preferences in local files under ~/coding/.

Mitigation: Use it only when local preference memory is desired, and inspect, edit, or delete ~/coding/ when reviewing stored preferences.

Risk: Incorrectly remembered preferences could steer future code output.

Mitigation: Store preferences only after explicit confirmation, and use the skill's show or forget workflows to correct entries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/coding)
- [Publisher profile](https://clawhub.ai/user/pmuhammadagus-byte)
- [Coding skill homepage](https://clawic.com/skills/coding)
- [Preference criteria](criteria.md)
- [Code preference dimensions](dimensions.md)
- [Memory templates](memory-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or code snippets with optional shell commands and local preference entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write confirmed coding preferences under ~/coding/.]

## Skill Version(s):

1.0.0 (source: target metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
