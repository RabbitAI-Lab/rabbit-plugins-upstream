## Description:

AI通识课资深专家V8.1AIPC helps teachers, curriculum designers, and education technologists plan AI literacy lessons, analyze course materials, compose Markdown and HTML courseware, and check p5.js interactive controls with an edge-cloud teaching workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linix-2026](https://clawhub.ai/user/linix-2026)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, curriculum designers, and education technology engineers use this skill to prepare AI literacy courses, select knowledge points, generate lesson artifacts, and validate interactive p5.js courseware. Developers can also use its scripts and references to run the local inference, edge-cloud request, cost monitoring, and privacy workflow around those teaching tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Privacy claims may overstate the guarantee that no data leaves the machine when edge-cloud workflows are configured.

Mitigation: Review cloud endpoint configuration and API-key handling before use; treat raw teaching materials as local-only and verify what minimized or derived metadata may be sent.

Risk: Student or classroom data could be exposed if PII redaction and cloud dispatch settings are not reviewed for the deployment context.

Mitigation: Run the PII controls on representative data, inspect the generated request payloads, and require human review before using the skill with student data.

Risk: Model and ffmpeg setup steps may download external resources during installation.

Mitigation: Review the deployment guide and install scripts, pin approved sources, and perform installation in a controlled environment.

## Reference(s):

- [Skill page](https://clawhub.ai/linix-2026/skills/ai-literacy-expert-v8-1-0-aipc)
- [README.md](README.md)
- [CHANGELOG.md](CHANGELOG.md)
- [Edge-cloud protocol](references/edge-cloud-protocol.md)
- [Edge-cloud protocol schema](references/edge-cloud-protocol-schema.json)
- [Zero-upload privacy guide](references/zero-upload-privacy.md)
- [p5.js courseware guide](references/p5js-courseware-guide.md)
- [p5.js game design guide](references/p5js-game-design-guide.md)
- [Local AI quality gate](references/local-ai-quality-gate.md)
- [Deployment guide](references/deployment-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown, JSON, HTML courseware, Python and shell command guidance, and generated local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create lesson plans, assessment JSON, HTML courseware, local-vs-cloud work summaries, and validation reports depending on the selected workflow stage.]

## Skill Version(s):

8.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
