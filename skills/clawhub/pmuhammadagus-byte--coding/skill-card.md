## Description:

The Coding skill helps an agent remember and apply a user's explicitly confirmed coding preferences through local preference files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to store, retrieve, and apply compact coding style, stack, structure, and workflow preferences that the user has explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive details could be saved if a user explicitly confirms them as preferences.

Mitigation: Do not confirm preferences that contain secrets, private client details, or sensitive project information.

Risk: Stored preferences can become stale or conflict with a project's current requirements.

Mitigation: Use the skill's forget and update workflows to remove outdated entries and resolve contradictions before applying them.

Risk: The included style checker is advisory and covers only a small set of Python conventions.

Mitigation: Treat lint output as guidance and rely on project tests, configured linters, and human review for final code quality decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/coding)
- [Criteria for Code Preferences](artifact/criteria.md)
- [Code Dimensions to Detect](artifact/dimensions.md)
- [Memory Templates](artifact/memory-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands, local file templates, and plain-text lint results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores confirmed preferences under ~/coding/ and includes an advisory Python style checker.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
