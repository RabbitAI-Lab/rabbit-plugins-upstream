## Description:

Turns a portrait and a short user-provided script into a generated clip of one person speaking those words to camera, using Ofox video generation through a required OFOX_API_KEY.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan and generate talking-head video clips from an authorized portrait plus exact script text. It is suited to short spokesperson-style clips where the model generates the voice, not to syncing an uploaded recording or creating scenes with multiple speakers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback installation guidance can use unpinned wildcard global commands that may change the user's agent environment.

Mitigation: Install only the required ofox-video-core dependency from a trusted, pinned source when possible, and review the installed skill before use.

Risk: Using the skill sends the portrait, script, and API-backed job data to Ofox for video generation.

Mitigation: Use only portraits and scripts the user is authorized to submit, and review the dry-run cost and prompt before any paid generation.

Risk: Generated clips can make a person's likeness appear to say words they did not say.

Mitigation: Confirm likeness rights, refuse identifiable public figures, quote the script verbatim for approval, and inspect the delivered clip for identity, lip-sync, and complete speech.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/talking-head)
- [talking-head source homepage](https://github.com/ofoxai/skills/tree/main/skills/talking-head)
- [Ofox API keys](https://app.ofox.ai)
- [ofox-video-core safety contract](../ofox-video-core/SKILL.md)
- [ofox-video-core prompt structure](../ofox-video-core/references/prompt-structure.md)
- [ofox-video-core creative brief](../ofox-video-core/references/creative-brief.md)
- [ofox-video-core approval gate](../ofox-video-core/references/approval-gate.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with bash command blocks, cost estimates, job status fields, and generated video file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY, curl, jq, and the sibling ofox-video-core skill; generated media is returned as an MP4 path with sidecar job metadata.]

## Skill Version(s):

1.1.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
