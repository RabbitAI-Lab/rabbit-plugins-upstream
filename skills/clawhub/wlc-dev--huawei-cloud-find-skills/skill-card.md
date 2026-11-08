## Description:

Searches the Huawei Cloud skills catalog, browses categories, retrieves skill details, and provides installation commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud users use this skill to find Huawei Cloud agent skills by keyword or category, review what a skill does, and obtain installation options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow directs agents to install and follow discovered skills without clear user approval.

Mitigation: Review the selected skill and obtain explicit approval before installing or following it; prefer reviewed installer versions and immutable source revisions.

Risk: A bundled guide includes commands that print cloud credential values.

Mitigation: Remove the credential-printing checks; rotate any secret that has already been printed.

Risk: Installation reports the selected skill identifier to Huawei.

Mitigation: Tell the user about this report and obtain approval before installation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-find-skills)
- [Huawei Cloud skills index repository](https://gitcode.com/2501_91318609/skills-for-index)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with installation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results and guidance depend on the current online catalog.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
