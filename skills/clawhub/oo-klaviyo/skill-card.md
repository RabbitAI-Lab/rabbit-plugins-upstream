## Description:

Klaviyo connector skill for reading, creating, and updating Klaviyo data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Klaviyo through an OOMOL-connected account, including reading campaigns, profiles, events, and account metadata and creating profile events after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute remote installer scripts for the oo CLI.

Mitigation: Review the installer source and prefer a pinned, checksum-verified installer or package-manager installation before use.

Risk: The skill can perform write-capable Klaviyo actions through the OOMOL CLI.

Mitigation: Confirm the exact payload, target account, and expected account impact before allowing write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-klaviyo)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Klaviyo Homepage](https://www.klaviyo.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Klaviyo connector schemas before action execution.]

## Skill Version(s):

1.0.3 (source: evidence release.version and artifact metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
