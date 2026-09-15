## Description:

Jibble lets an agent read Jibble organizations, members, and work locations, and create, update, archive, or permanently delete work locations through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting Jibble workspace administrators use this skill to inspect organization, member, and work location data, then manage work locations when the user has confirmed the intended state change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes direct remote script execution for installing the oo CLI.

Mitigation: Review the installer path first and prefer a signed, version-pinned, checksum-verified package manager or installer flow.

Risk: Write and destructive actions can change or permanently delete Jibble work locations.

Mitigation: Fetch the live action schema before building payloads and require explicit user confirmation of the target, payload, and expected effect before execution.

Risk: Actions run against the connected Jibble account or organization.

Mitigation: Connect only the intended Jibble account or organization and verify the target organization before state-changing actions.

## Reference(s):

- [ClawHub Jibble skill](https://clawhub.ai/oomol/skills/oo-jibble)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Jibble homepage](https://www.jibble.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema lookup before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
