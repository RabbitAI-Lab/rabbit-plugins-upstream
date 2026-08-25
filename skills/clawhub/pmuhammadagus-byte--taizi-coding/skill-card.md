## Description:

Gunakan saat membutuhuhkan kemampuan terkait taizi-coding (lihat When to Use di bawah).

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to remember explicitly confirmed coding preferences and apply them to future coding output. It supports local preference storage, querying, forgetting, and a small Python style checker guided by those preferences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may retain coding preferences that no longer reflect the user's current intent.

Mitigation: Store only explicitly confirmed preferences and support showing or forgetting stored preferences on request.

Risk: Local preference memory may include sensitive or personally identifying coding choices if the user confirms them.

Mitigation: Keep preference entries local under ~/coding/ and redact secrets or personal data before storing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/taizi-coding)
- [Publisher profile](https://clawhub.ai/user/pmuhammadagus-byte)
- [criteria.md](criteria.md)
- [dimensions.md](dimensions.md)
- [memory-template.md](memory-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline text, code, shell commands, and local file guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or write explicitly confirmed preference entries under ~/coding/ and may run a local Python style lint script.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
