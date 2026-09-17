## Description:

Google Ads (ads.google.com) skill for reading, creating, updating, and deleting Google Ads data through the OOMOL Google Ads connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing teams use this skill to inspect and manage Google Ads accounts through an OOMOL-connected account, including customer lists, campaigns, ad groups, and GAQL search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI, and the security summary flags direct execution of unverified installer scripts as risky.

Mitigation: Install the oo CLI only from a verified, versioned, signed, or checksum-validated source, and avoid running pasted installer commands from a privileged shell.

Risk: Write and destructive actions can change Google Ads account data, including campaign, ad group, and Customer Match list membership changes.

Mitigation: Confirm the exact customer account, action payload, target resources, and expected effect with the user before running any write or destructive action.

Risk: Action schemas can change, so stale payload assumptions can lead to failed or unintended Google Ads operations.

Mitigation: Fetch the live connector schema for the selected action before constructing or running a payload.

## Reference(s):

- [ClawHub Google Ads skill page](https://clawhub.ai/oomol/skills/oo-googleads)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Google Ads](https://ads.google.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data with execution metadata when run through the oo CLI.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
