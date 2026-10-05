## Description:

Creates a separate short talking clip for each authorized still, using only the insurance policy clauses supplied by the user.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Insurance advisors and wealth educators use their supplied policy clauses and authorized images to plan and produce individual narrated clause-explanation clips, without stitching the clips together.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra device credential grants broad media and wallet access across installed Beatra skills.

Mitigation: Install only if this access is acceptable; protect the local credential and revoke the device in the Beatra console when no longer needed.

Risk: Package code updates silently by default, potentially changing behavior between uses.

Mitigation: Disable automatic updates with the documented update --auto off command if changes must be reviewed before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/insurance-clause-talking)
- [Beatra skill page](https://beatra.ai/skills/insurance-clause-talking)
- [Clause talking-clip workflow](artifact/references/workflow.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Audio, Video clips]

**Output Format:** [Labeled clause-and-still plan followed by individual narrated clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 2–8 separate clips of 2–15 seconds each; reports available media details and net credits charged.]

## Skill Version(s):

0.1.9 (source: ClawHub release and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
