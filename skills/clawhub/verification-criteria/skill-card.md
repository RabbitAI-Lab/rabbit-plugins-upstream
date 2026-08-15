## Description:

Generate, audit, and trace verification criteria for functional system requirements across VC generation, quality audit, and coverage audit workflows aligned with ASPICE SYS.2 BP5, ISO/IEC 29148, and VC-First methodology.

This skill is ready for commercial/non-commercial use.

## Publisher:

[unknowcao](https://clawhub.ai/user/unknowcao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, systems engineers, and verification engineers use this skill to create measurable VCs, audit existing VCs with SMARTR-OC and checklist criteria, and check requirement-to-VC coverage for functional system requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes requirement and VC documents in the workspace and may create split, merge, and review artifacts.

Mitigation: Review prompts before allowing overwrite or regeneration of existing VC files, and inspect generated outputs before using them.

Risk: Generated verification criteria or audit findings may be incorrect or incomplete for the user's engineering context.

Mitigation: Review source labels, SMARTR-OC scores, coverage reports, and blocked assumptions before adopting the artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/unknowcao/skills/verification-criteria)
- [Server-resolved GitHub provenance](https://github.com/UnknowCao/autoskill-hub/tree/main/skills/verification-criteria)
- [Publisher profile](https://clawhub.ai/user/unknowcao)
- [VC definition framework](artifact/references/vc-framework.md)
- [VC output format specification](artifact/references/vc-output-format.md)
- [SMARTR-OC scoring rubric](artifact/references/vc-smartr-oc.md)
- [Source Depth tagging reference](artifact/references/vc-source-depth.md)
- [VC checklist](artifact/assets/vc-checklist.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown reports and tables, with optional generated files and JSON statistics from split/merge tooling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces VC tables, SMARTR-OC scores, Source Depth labels, coverage matrices, uncovered/orphan lists, and review guidance.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
