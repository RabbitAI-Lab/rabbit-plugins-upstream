## Description:

Uydi Voice enables an AI agent to design custom voices, clone authorized voice samples, synthesize narration, and produce multi-voice Voice Canvas projects with the Uydi voice platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lvyinchao](https://clawhub.ai/user/lvyinchao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to manage Uydi voice workflows: design or clone permitted voices, synthesize narration, assemble multi-speaker Voice Canvas projects, check credits, and retrieve WAV outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on the authenticated user's Uydi account after OAuth approval.

Mitigation: Require user-completed OAuth login, run account checks before use, and log out or revoke access on shared or untrusted machines.

Risk: Voice design, cloning, synthesis, and changed Voice Canvas nodes can consume real Uydi credits.

Mitigation: Check credits and estimates before paid work, confirm large or batch operations, and inspect history or render status before retrying uncertain paid requests.

Risk: Voice cloning can misuse a voice sample without proper rights.

Mitigation: Clone only voices the user owns or has explicit permission to use.

Risk: Local OAuth credentials are stored on the user's machine.

Mitigation: Use logout or site-side revocation when access is no longer needed, especially on shared systems.

## Reference(s):

- [Uydi](https://uydi.com)
- [Voice Canvas reference](references/voice-canvas.md)
- [ClawHub listing](https://clawhub.ai/lvyinchao/skills/uydi-voice)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with CLI commands, JSON Canvas configuration, and WAV audio output paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+ and user-approved OAuth access; paid operations can consume Uydi credits.]

## Skill Version(s):

1.1.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
