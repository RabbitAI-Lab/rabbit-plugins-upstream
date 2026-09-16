## Description:

Provides OOMOL-backed access to Stability AI through the oo CLI, including schema inspection and text-to-audio generation with uploaded results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect Stability AI connector schemas and run Stability AI actions through an OOMOL-connected account, including text-to-audio generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can generate and upload audio, so treating it as read-only may lead to unintended content creation or storage.

Mitigation: Review the live action schema and confirm the text-to-audio payload and expected upload behavior before running the action.

Risk: The setup guidance includes remote installer pipe commands.

Mitigation: Verify the OOMOL installer source through a safer method before executing installation commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-stabilityai)
- [ClawHub Publisher Profile](https://clawhub.ai/user/oomol)
- [Stability AI Homepage](https://stability.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce uploaded audio files through connector transit storage.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
