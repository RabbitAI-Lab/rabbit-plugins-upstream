## Description:

Install, run, recover, or explain the standalone ClawPatch queue supervisor for repair queues, stopped-finding recovery, and completion proof.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uncmatteth](https://clawhub.ai/user/uncmatteth)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to supervise a ClawPatch repair queue, resume exact stopped attempts, verify completion proof, and report the repository state after repair work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supervised workflow can commit and optionally push repair results in the target repository.

Mitigation: Review the branch and push policy before use, run it for one explicit repository path at a time, and verify the final proof file and Git state before treating a run as complete.

Risk: A stopped or uncertain repair can be mishandled if the exact checkpoint, finding, or source paths are not preserved.

Mitigation: Resume only an exact stopped attempt and fail closed when ownership, checkpoint, or source-path evidence is ambiguous.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/uncmatteth/skills/clawpatch-supervise)
- [Project and Install Instructions](https://github.com/uncmatteth/clawpatch-supervise)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured status details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include repository and branch, tool versions, run mode, current finding or COMPLETE status, stopped paths and exit class, proof path, Git state, local SHA, and remote SHA when relevant.]

## Skill Version(s):

0.1.16 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
