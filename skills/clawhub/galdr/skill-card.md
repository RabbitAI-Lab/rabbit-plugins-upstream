## Description:

OpenClaw skill for using galdr's ARC workflow to turn YouTube URLs or local audio files into grounded, time-ordered listening-experience prompts backed by listener-state traces: pattern, attention, pulse, heard pressure, surface balance/evidence, harmony, melody, overtones, and silence/re-entry structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sellemain](https://clawhub.ai/user/sellemain)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw agent operators use this skill to analyze songs, music videos, or local audio into grounded listener-state evidence and listening-experience prompts. It helps agents extract structural moments, assemble ARC prompts, and avoid unsupported emotional or lyrical claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a separate galdr CLI and media/model integrations that may process local audio, lyrics, background context, or prompts outside the skill artifact.

Mitigation: Install the CLI only from trusted sources, understand configured data flows before using private audio, and review assembled prompts before sending them to another model.

Risk: Generated listening-experience prose can overstate emotional intent or treat structural metrics as proof of private meaning.

Mitigation: Use the metrics as evidence, walk the track through time, and keep claims bounded to audible structure rather than inferred intent.

Risk: Fetching or analyzing online music can raise rights and policy issues for copyrighted media.

Mitigation: Use downloads and analysis only when the operator has appropriate rights or context, and prefer local or authorized media when rights are unclear.

## Reference(s):

- [Galdr ClawHub release](https://clawhub.ai/sellemain/skills/galdr)
- [Galdr metric reference](references/metrics.md)
- [Galdr PyPI package](https://pypi.org/project/galdr/)
- [Galdr source repository](https://github.com/sellemain/galdr)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and references to generated JSON analysis files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary outputs guide the agent to run galdr, inspect time-ordered listener-state traces, and assemble or review ARC prompts before optional model handoff.]

## Skill Version(s):

0.7.0 (source: server release metadata; artifact frontmatter says 0.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
