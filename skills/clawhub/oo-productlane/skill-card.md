## Description:

Productlane (productlane.com). Use this skill for Productlane requests, including reading, creating, updating, and deleting workspace data through the OOMOL-connected Productlane connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Productlane through an OOMOL-connected account. It supports workspace reads plus company and contact creation, updates, and soft deletion after inspecting the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions can execute local code.

Mitigation: Use a verified package or reviewed installer from the official source instead of automatically running pipe-to-shell or Invoke-Expression commands.

Risk: Write and destructive actions can change or soft-delete Productlane company and contact data.

Mitigation: Inspect the live action schema and confirm the exact target, payload, and expected effect with the user before running write or delete actions.

Risk: Productlane access is mediated through OOMOL-connected credentials.

Mitigation: Install only when the operator accepts OOMOL-mediated Productlane access and confirms the connected account has appropriate scopes.

## Reference(s):

- [Productlane homepage](https://productlane.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Productlane skill page](https://clawhub.ai/oomol/skills/oo-productlane)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
