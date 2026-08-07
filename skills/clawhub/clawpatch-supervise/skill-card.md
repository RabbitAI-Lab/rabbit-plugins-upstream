## Description:

Guides agents through installing, running, resuming, and verifying the ClawPatch queue supervisor for repository repair workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uncmatteth](https://clawhub.ai/user/uncmatteth)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and repository maintainers use this skill to run a supervised ClawPatch repair queue, resume exact stopped attempts, and verify completion proof before treating a repository repair run as complete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can modify, commit, and optionally push changes in a selected repository.

Mitigation: Confirm the absolute target repository, branch policy, push policy, and clean or dirty Git state before use.

Risk: A stopped or uncertain repair run could be resumed from the wrong state if checkpoint details are ignored.

Mitigation: Resume only from the exact stopped checkpoint and preserve the printed finding, paths, source state, and exit class.

Risk: A queue could be treated as complete before the supervisor has produced verifiable proof.

Mitigation: Require the final COMPLETE result, proof file, clean Git state, and expected local and remote SHAs when pushes are enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/uncmatteth/skills/clawpatch-supervise)
- [Project and install instructions](https://github.com/uncmatteth/clawpatch-supervise)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with command examples and completion-proof details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes repository, branch, tool versions, run mode, current finding or COMPLETE result, stopped-path details when incomplete, and proof/Git state when complete.]

## Skill Version(s):

0.1.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
