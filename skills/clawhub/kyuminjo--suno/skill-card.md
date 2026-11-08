## Description:

Make full songs with vocals using Suno v6 (plus Mini and Wild) and MiniMax Music 3.0 via the PopNow API: from your lyrics or a short brief, any genre. Exact USD quote before every song.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyuminjo](https://clawhub.ai/user/kyuminjo)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent can turn rights-cleared lyrics or a short musical brief into a complete song, or request instrumental music, through Suno or MiniMax models. The workflow checks the model schema and provides an exact cost quote for approval before creating a paid song.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, lyrics, and reference media URLs are shared with PopNow and the generation providers; host or agent logs may retain command parameters.

Mitigation: Submit only rights-cleared material you are comfortable sharing, avoid sensitive personal data, and account for possible command logging.

Risk: Song generation can incur charges from the prepaid API balance.

Mitigation: Use a dedicated API key with spending and model limits, and approve each quoted cost before creating a song.

## Reference(s):

- [PopNow Suno v6 model page](https://popnow.ai/models/suno-v6)
- [PopNow API task documentation](https://popnow.ai/docs/tasks)

## Skill Output:

**Output Type(s):** [Audio, Text, Shell commands]

**Output Format:** [Generated audio links with text quotes and task status; shell commands for the workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Songs can use supplied lyrics or a brief, with genre, mood, tempo, and vocal preferences. Generation is paid from a separate PopNow API balance.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
