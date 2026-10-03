## Description:

Reviews SnapVisor visual regression builds, summarizes screenshot changes, and approves or rejects a build only after the user confirms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review screenshot diffs for a SnapVisor build on a branch or commit and, after explicit confirmation, approve or reject that build.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approving a build updates the team's visual baseline.

Mitigation: Check the account, project, build number, and screenshot diffs, and obtain explicit user confirmation before approving or rejecting.

## Reference(s):

- [SnapVisor: Reviewing Visual Builds on ClawHub](https://clawhub.ai/bsalaeddin/skills/snapvisor-reviewing-visual-builds)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summary with screenshot comparison links and review status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Screenshot links expire; review decisions require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
