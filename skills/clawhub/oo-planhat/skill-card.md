## Description:

Planhat is an agent skill for reading, creating, and updating Planhat data through the OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with an OOMOL-connected Planhat account use this skill to inspect live connector schemas and run read or write actions for Planhat companies and end users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on an OOMOL-connected Planhat workspace and may read or change company and end-user records.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions, and treat untagged get and list actions as read-only.

Risk: First-time setup includes remote installer commands that the security summary identifies as high impact.

Mitigation: Prefer a verified or package-manager-based oo CLI installation path, or inspect installer contents before running shell-based installers.

Risk: Connector input contracts can change over time.

Mitigation: Fetch the live action schema with the oo CLI before constructing each action payload.

## Reference(s):

- [ClawHub Planhat skill](https://clawhub.ai/oomol/skills/oo-planhat)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Planhat homepage](https://www.planhat.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
