## Description:

Mobile Text Alerts helps agents read, create, update, and delete subscriber data through an OOMOL-connected Mobile Text Alerts account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations teams use this skill to manage Mobile Text Alerts subscribers, including listing, searching, creating, updating, and deleting records. The skill is intended for agent-mediated use where write and destructive actions require user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may ask users to run unverified remote installer scripts.

Mitigation: Review setup instructions before installing and prefer a version-pinned, checksum-verified, or manually inspected oo CLI installation method.

Risk: Write and destructive actions can create, update, or delete Mobile Text Alerts subscriber records.

Mitigation: Approve write or delete actions only after checking the exact subscriber target and JSON payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mobile-text-alerts)
- [Mobile Text Alerts homepage](https://mobile-text-alerts.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON payloads for connector actions and confirmation prompts before write or destructive subscriber actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
