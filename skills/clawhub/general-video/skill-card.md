## Description:

Author or edit a custom HyperFrames composition when no specialized workflow fits, or when BRIEF.md sets flow: companion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to plan, build, edit, validate, and render custom HyperFrames video compositions, including longer multi-scene pieces, brand reels, montages, static loops, title cards, footage remixes, and companion-led video builds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow asks the agent to run and update HyperFrames through unpinned online npx commands, which can change what code or instructions run later.

Mitigation: Install only after reviewing and trusting the HyperFrames package and registry path; prefer a pinned, reviewed local HyperFrames CLI and avoid automatic skill updates during normal work.

Risk: Media provider actions may involve sign-in, billing, or authenticated services.

Mitigation: Review provider sign-in status and any billing-related media action before continuing.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [Frame worker role delta](artifact/sub-agents/frame-worker.md)
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/general-video)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, project file edits, HTML composition code, and JSON motion sidecar files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a single agent workflow stream for HyperFrames projects and may create bounded frame packet files for delegated scene work.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
