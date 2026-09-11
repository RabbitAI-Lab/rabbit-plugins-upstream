## Description:

Read sign-up sheets, slot reports, and groups on SignUpGenius, and add members to your groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to inspect their SignUpGenius profile, groups, sign-ups, public slots, and Pro reports, and to perform supported account actions such as adding group members, RSVPing, claiming slots, or releasing their own slots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags reliance on an unpinned external signupgenius-mcp npm package and fetchproxy extension that may access a SignUpGenius session or credentials.

Mitigation: Pin the package version, install only from trusted sources, and review the extension and package before connecting a SignUpGenius account.

Risk: The skill can handle SignUpGenius passwords, API keys, cookies, or session tokens depending on the selected authentication mode.

Mitigation: Prefer the least privileged authentication mode available, avoid storing credentials in project-level files, and rotate credentials if exposure is suspected.

Risk: Supported write actions can add group members, submit RSVPs, claim slots, or release the signed-in user's slots.

Mitigation: Manually confirm every write action and inspect dry-run previews where the tool provides them before allowing the action to proceed.

Risk: The artifact notes that scripted or automated SignUpGenius access may conflict with SignUpGenius terms when used outside personal-account, personal-scale workflows.

Mitigation: Use the skill only with accounts and sign-ups the user is authorized to access, and check SignUpGenius terms before scaled or organizational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [SignUpGenius](https://www.signupgenius.com)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or invoke SignUpGenius MCP tools depending on the user's configured authentication mode and account permissions.]

## Skill Version(s):

1.8.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
