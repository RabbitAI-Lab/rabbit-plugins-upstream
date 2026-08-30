## Description:

AI通识课资深专家V8.2BNBU helps educators plan AI literacy courses, generate Markdown lessons, assessments, and interactive p5.js courseware, and tailor BNBU SAI 5+N student and teacher workflows with local/cloud coordination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linix-2026](https://clawhub.ai/user/linix-2026)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, curriculum designers, and education technology engineers use this skill to prepare AI literacy lessons, analyze course materials, select knowledge points, compose courseware, and support BNBU SAI 5+N student and teacher AI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Privacy and offline claims may be stronger than the implementation evidence supports.

Mitigation: Review and control network behavior before deployment, and require clear endpoint, provider, permission, and retention documentation.

Risk: Abstracted course metadata may be sent to a configured cloud endpoint.

Mitigation: Treat zero-upload as raw-files-local rather than no-data-leaves, and test cloud calls with de-identified or synthetic data first.

Risk: Use with real student identifiers, grades, answers, or sensitive family data could expose protected information.

Mitigation: Avoid sensitive student data until privacy documentation and operational controls are aligned with implementation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linix-2026/skills/ai-literacy-expert-v8-2-0-aipc)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)
- [Edge-cloud protocol](artifact/references/edge-cloud-protocol.md)
- [Edge-cloud protocol schema](artifact/references/edge-cloud-protocol-schema.json)
- [Zero-upload privacy](artifact/references/zero-upload-privacy.md)
- [Module H BNBU SAI overview](artifact/references/module-h-bnbu-sai.md)
- [Module H discipline AI map](artifact/references/module-h-s-discipline-ai.md)
- [Module H teacher toolbox](artifact/references/module-h-t-toolbox.md)
- [p5.js courseware guide](artifact/references/p5js-courseware-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON, HTML courseware, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce lesson plans, assessment JSON, p5.js courseware, local/cloud comparison reports, and setup or validation commands.]

## Skill Version(s):

8.2.0 (source: server release metadata; artifact version 8.2.0-aipc)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
