## Description:

Remembers and applies explicit coding style preferences from local storage to help an agent produce consistent code output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to store explicitly confirmed coding preferences, retrieve them at session start, and apply them to code generation. It is intended for local preference memory, not automatic observation of project files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill retains coding preferences in local files under ~/coding/.

Mitigation: Store only explicitly confirmed preferences and review or delete ~/coding/memory.md when the retained preferences are no longer wanted.

Risk: Incorrect or stale preferences may influence future code output.

Mitigation: Use the documented query and forget workflows to inspect, correct, or remove stored preferences.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/taizi-coding)
- [Coding Skill Homepage](https://clawic.com/skills/coding)
- [Preference Criteria](criteria.md)
- [Code Dimensions](dimensions.md)
- [Memory Templates](memory-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with concise preference entries, code-oriented recommendations, and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores confirmed preferences locally in ~/coding/memory.md with a documented 100-line limit.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
