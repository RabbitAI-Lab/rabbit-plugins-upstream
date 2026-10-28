## Description:

Guides agents through turning recorded footage into a documentary-style vlog, from reviewing material and shaping a story to assembling a user-reviewed edit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitruck](https://clawhub.ai/user/gitruck)

### License/Terms of Use:

MIT-0

## Use Case:

External video creators use this skill to turn their recorded footage into a documentary-style vlog, with an editable audiovisual script and an organized gtrk project workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud analysis may process a low-resolution video proxy and, for highlight analysis, low-bitrate mono audio by default.

Mitigation: Confirm cloud processing, estimated costs, and preferred language before running; use --no-audio when audio should be excluded from highlight analysis, and review the script before production.

## Reference(s):

- [Gitruck CLI](https://github.com/Gitruck/cli)
- [ClawHub skill release](https://clawhub.ai/gitruck/skills/gtrk-vlog-docu)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown scripts, shell commands, JSON segment manifests, and editable project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The script and source intervals are reviewed before composition.]

## Skill Version(s):

1.3.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
