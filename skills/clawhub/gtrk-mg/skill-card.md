## Description:

Adds approved HTML motion graphics to a finalized video project's beat track after the underlying footage and composition have been reviewed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitruck](https://clawhub.ai/user/gitruck)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and production agents use this skill to place column-produced motion graphics into a video project's beat track after the underlying footage and composition checks are complete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the workflow can replace footage that was already approved without a fresh approval checkpoint.

Mitigation: Require explicit approval before replacing approved footage and work from a backup project.

Risk: Rebuilding animations can overwrite manual adjustments to affected generated clips; cloud uploads and rendering can also incur costs.

Mitigation: Use a backup project, review cloud uploads, and check estimated rendering charges before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gitruck/skills/gtrk-mg)
- [Gitruck CLI project](https://github.com/Gitruck/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and project configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May add motion-graphic particle assets to a video project's beat track.]

## Skill Version(s):

1.3.9 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
