## Description:

Coordinates same-account agent sessions with passphrase-style handoffs so another session can read a specified file, relay conclusions, or report parallel-session activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to coordinate same-machine, same-account agent sessions when they need another window to read a named file, transfer a conclusion, or summarize what a parallel session did.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent cross-session passphrases can trigger broad automatic file-reading or data relay behavior later.

Mitigation: Use narrow passphrase mappings, require the receiving session to confirm the exact file or data before reading, and remove memory mappings after the handoff is complete.

Risk: Same-account session handoffs can disclose stale or unintended context when mappings are left active.

Mitigation: Register only intentional handoffs, avoid broad trigger phrases, and review stored mappings before relying on automatic disclosure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/cross-session-passphrase)
- [Publisher profile: zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional command snippets and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve persistent same-account memory mappings for cross-session handoff behavior]

## Skill Version(s):

1.2.0 (source: frontmatter, manifest, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
