## Description:

Delete When Unzip helps agents guide users through streaming extraction of large ZIP and RAR archives while deleting processed archive data to reduce peak disk usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[auto-dog](https://clawhub.ai/user/auto-dog)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill when they need an agent to select the right extraction path for large local archives under limited disk space, build safe commands, and explain the destructive deletion tradeoff before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool is designed to delete or truncate the source archive during extraction, and interrupted extraction can leave the archive damaged.

Mitigation: Use it only on backed-up or expendable archives, and require clear user confirmation before any destructive extraction command is run.

Risk: Unsafe code paths could run code or write files outside the intended output folder.

Mitigation: Use trusted numeric chunk-size values and trusted archives only; contain output paths and replace eval-based parsing before broader deployment.

Risk: The bundled UnRAR workflow is platform-specific and may not be suitable outside Windows x64.

Mitigation: Verify the target platform and use a trusted UnRAR binary that matches the operating system before running RAR extraction commands.

## Reference(s):

- [Source repository (server-resolved provenance)](https://github.com/auto-Dog/delete_when_unzip)
- [ClawHub skill page](https://clawhub.ai/auto-dog/skills/delete-when-unzip)
- [RARLab UnRAR downloads](https://www.rarlab.com/download.htm)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Warns about destructive archive deletion, archive format selection, chunk-size tradeoffs, and platform-specific UnRAR requirements.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
