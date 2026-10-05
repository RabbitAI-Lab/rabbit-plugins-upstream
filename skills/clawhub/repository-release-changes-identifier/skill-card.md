## Description:

Summarize repository changes for a release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release coordinators and developers use this skill to turn a supplied repository patch into structured release-change metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patches without a diff --git header or REPO-style change ID cannot be processed.

Mitigation: Supply a unified diff with both a diff --git header and a REPO-style change ID.

Risk: Structured change counts and file lists may not capture the full meaning of a release.

Mitigation: Review the output against the supplied patch before using it in release communications.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/repository-release-changes-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Structured data]

**Output Format:** [JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [release_change_set contains a change ID, changed files, components, and addition and deletion counts.]

## Skill Version(s):

1.1.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
