## Description:

WaiverForever helps an agent operate a user's OOMOL-connected WaiverForever account for reading, creating, and updating waiver data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate WaiverForever through an OOMOL-connected account, including reading account, template, waiver, and request data and creating template signing links or waiver request groups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions such as create_template_signing_link and create_waiver_request can change WaiverForever state.

Mitigation: Review the exact payload and intended effect with the user before approving or running state-changing actions.

Risk: Read actions may expose signed waiver data from the connected WaiverForever account.

Mitigation: Install and use the skill only for accounts the user intends Codex to access, and treat returned waiver data as sensitive.

Risk: Payload fields may drift from the connector contract over time.

Mitigation: Inspect the live action schema before building a payload so requests match the current connector contract.

## Reference(s):

- [ClawHub WaiverForever Skill](https://clawhub.ai/oomol/skills/oo-waiverforever)
- [WaiverForever Homepage](https://www.waiverforever.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas and JSON responses returned by the oo CLI.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
