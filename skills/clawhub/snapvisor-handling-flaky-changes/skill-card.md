## Description:

Helps manage flaky visual changes in SnapVisor by finding flaky tests, listing ignored changes, and ignoring or restoring individual changes after confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and visual-test reviewers use this skill to identify flaky tests and manage specific noisy screenshot changes without ignoring other build diffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ignoring a visual change can affect whether its diff blocks a build.

Mitigation: Verify the change is known-noisy or flaky, show its flakiness metrics when available, and confirm each change before ignoring it.

Risk: The skill relies on the SnapVisor connector to read and change project state.

Mitigation: Confirm the connector is trusted before installing or using the skill.

## Reference(s):

- [SnapVisor: Handling Flaky Changes on ClawHub](https://clawhub.ai/bsalaeddin/skills/snapvisor-handling-flaky-changes)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports available flakiness metrics and confirms each individual ignore or un-ignore action.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
