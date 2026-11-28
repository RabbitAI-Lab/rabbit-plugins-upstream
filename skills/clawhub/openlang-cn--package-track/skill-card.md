## Description:

Tracks package build metadata across a workspace. Inert documentation canary used during an authorized namespace-reclaim assessment.

This skill is for research and development only.

## Publisher:

[openlang-cn](https://clawhub.ai/user/openlang-cn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can use the described workflow to inventory package names and resolved versions, check lockfile dates, and compare resolved versions with manifest ranges so mismatches can be prioritized. This release is an inert documentation canary for an authorized namespace-reclaim security assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete because three referenced local paths could not be resolved.

Mitigation: Review the referenced paths and the full artifact before deciding whether to install.

## Reference(s):

- [Package Track on ClawHub](https://clawhub.ai/openlang-cn/skills/package-track)
- [Publisher profile: openlang-cn](https://clawhub.ai/user/openlang-cn)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown tables and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes package metadata, lockfile dates, and manifest-range checks; the artifact contains no executable implementation.]

## Skill Version(s):

0.0.1 (source: frontmatter, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
