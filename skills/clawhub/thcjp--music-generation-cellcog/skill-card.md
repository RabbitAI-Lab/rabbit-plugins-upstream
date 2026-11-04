## Description:

CellCog-powered AI music generation for original instrumental and vocal music from 5 seconds to 10 minutes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and workflow operators use this skill to generate music prompts and agent guidance for original instrumental tracks, vocals, podcast intros, game soundtracks, and background audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask the agent to read files, write outputs, and run commands.

Mitigation: Review proposed commands before allowing execution and run the skill in an appropriately restricted workspace.

Risk: Music or media inputs may be copyrighted or sensitive.

Mitigation: Use only media you are authorized to process and avoid sending sensitive material unless that processing is intended.

Risk: API keys may be required for downstream music generation services.

Mitigation: Keep keys in environment variables and do not commit credentials to version control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/music-generation-cellcog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with example prompts, JSON result structure, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide the agent to read inputs, write generated outputs, and run user-reviewed commands.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
