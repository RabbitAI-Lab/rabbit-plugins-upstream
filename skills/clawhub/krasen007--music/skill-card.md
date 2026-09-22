## Description:

Control AIMP music player via native command-line switches for play, pause, stop, next, and previous actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krasen007](https://clawhub.ai/user/krasen007)

### License/Terms of Use:

MIT-0

## Use Case:

Windows users and agents use this skill to control local AIMP playback from terminal commands when AIMP is installed and running.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change local audio playback immediately and silently.

Mitigation: Review requests before running playback commands, especially skip, stop, pause, and play actions.

Risk: Commands require AIMP to be installed and running on Windows.

Mitigation: Confirm AIMP is installed and check the running process before issuing playback switches.

## Reference(s):

- [AIMP homepage](https://aimp.ru)
- [ClawHub skill page](https://clawhub.ai/krasen007/skills/music)
- [Publisher profile](https://clawhub.ai/user/krasen007)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target a local Windows AIMP installation and execute immediately and silently.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
