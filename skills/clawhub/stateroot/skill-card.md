## Description:

StateRoot installs and sets up a local-first CLI that connects supported AI agent harnesses so personality, plans, tools, skills, memories, learnings, and project context can carry across sessions and agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[usama04](https://clawhub.ai/user/usama04)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use this bootstrap skill to install the StateRoot CLI, run machine-level setup, and optionally initialize a project so supported agent harnesses can share local continuity state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run remote installer commands and can persistently change multiple agent harness environments.

Mitigation: Review installer commands before execution, prefer interactive setup, use `stateroot setup --dry-run` to inspect planned writes, and avoid non-interactive setup unless defaults are acceptable.

Risk: Release builds may send anonymous product telemetry to stateroot.dev.

Mitigation: Set `STATEROOT_NO_PING=1` before use if anonymous telemetry is not acceptable.

Risk: The skill becomes inappropriate after setup because StateRoot's built-in skill should own daily workflow.

Mitigation: Expire this bootstrap skill once setup has completed and follow the installed built-in skill for resume, checkpoint, handoff, memory, and daily workflow.

## Reference(s):

- [StateRoot homepage](https://stateroot.dev)
- [Installation documentation](https://stateroot.dev/docs/getting-started/installation)
- [Setup documentation](https://stateroot.dev/docs/getting-started/setup)
- [Privacy guide](https://stateroot.dev/docs/guides/privacy)
- [FAQ](https://stateroot.dev/docs/reference/faq)
- [Platform install details](references/install.md)
- [Disclosure](references/disclosure.md)
- [Bootstrap failures](references/failures.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide the user through install, setup, and project initialization commands; it does not itself produce artifact files.]

## Skill Version(s):

1.1.4 (source: release evidence and skill manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
