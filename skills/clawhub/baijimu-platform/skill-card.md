## Description:

The Baijimu Platform skill guides an agent through using the local `baijimu` CLI to authenticate, inspect capabilities, manage workspaces and projects, operate agent sessions, develop and publish bundles, configure services, and call documented Partner API endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[momoplan](https://clawhub.ai/user/momoplan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform operators use this skill to let an agent operate Baijimu through the installed CLI while confirming local command availability, resource identifiers, permissions, and side effects before changes are made.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad platform-management actions through the Baijimu CLI, including create, update, publish, delete, rollback, uninstall, paid, or externally messaging operations.

Mitigation: Require explicit user approval for destructive, paid, rollback, uninstall, publishing, or externally messaging actions, and verify the resulting state with read-back commands.

Risk: Commands may involve authentication state, model credentials, service tokens, cookies, or full authorization responses.

Mitigation: Do not print secrets or full authentication responses; use documented login and status commands instead of editing credential files or management tokens directly.

Risk: Using mismatched documentation or guessing unavailable commands could cause incorrect Baijimu operations.

Mitigation: Confirm the installed CLI version and command help first, then use the fixed documentation URLs returned by local capability output when detailed command structure is needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/momoplan/skills/baijimu-platform)
- [Skill Homepage](https://github.com/momoplan/baijimu-platform-skill)
- [Baijimu Documentation](https://docs.baijimu.com/)
- [Baijimu CLI Documentation](https://docs.baijimu.com/cli/)
- [Baijimu Bundle Development](https://docs.baijimu.com/development/bundle-development/)
- [Baijimu Partner API](https://docs.baijimu.com/integration/api/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline CLI commands and JSON examples when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses locally installed CLI help and capability output as the execution source of truth.]

## Skill Version(s):

1.4.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
