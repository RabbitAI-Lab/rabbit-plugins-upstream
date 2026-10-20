## Description:

Reviews skills and other release candidates against publishing criteria and provides offline checks for sensitive information before release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and release reviewers use this skill to classify proposed public releases, review publishing criteria, and check for secrets, personal data, and internal information before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanners can miss files, including through a traversal bug and a filename-based skip.

Mitigation: Review and fix scanning coverage before using a pass to approve a release; consider an independent secret scan.

Risk: The declared entry point can omit the required secret scan.

Mitigation: Run both bundled scanners explicitly on the intended release directory and review their results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/skill-release-gate)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance and scanner results in terminal text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scanner exit codes indicate whether checks found matches; a pass does not establish release safety.]

## Skill Version(s):

1.0.0 (source: ClawHub release; bundled skill frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
