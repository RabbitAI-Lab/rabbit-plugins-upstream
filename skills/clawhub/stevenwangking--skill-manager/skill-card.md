## Description:

Helps agents discover, compare, vet, install, update, remove, and troubleshoot agent skills across supported environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevenwangking](https://clawhub.ai/user/stevenwangking)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to find and evaluate skills, manage global installations, and diagnose visibility or linking problems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned remote skills CLI commands can change behavior between uses.

Mitigation: Use a pinned, reviewed CLI version and avoid recovery commands that fetch the latest release.

Risk: Global install, update, or removal can alter or delete installed skills, including custom local work.

Mitigation: Confirm each change, protect or back up local skills, and verify the affected installation and agent links afterward.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/stevenwangking/skills/skill-manager)
- [Evaluation framework](references/evaluation-framework.md)
- [Security vetting checklist](references/security-vetting.md)
- [Skills directory](https://skills.sh)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown reports and installation or diagnostic instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes candidate comparisons, safety assessments, and installation or link status when applicable.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
