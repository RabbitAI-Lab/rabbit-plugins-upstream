## Description:

LYGO Ops Detector analyzes operator-supplied text with local discourse heuristics for evasion, half-truth certainty, saturation bait, coordination language, and policy-refusal signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

LYGO-Sovereign-v2.0

## Use Case:

Developers, analysts, and agents use this skill when a user explicitly requests AETHON D9, ops-detector, or evasion-index style analysis on text they provide. It produces discourse scores and review prompts, not identity conclusions or sole evidence for action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat heuristic discourse scores as proof about people or organizations.

Mitigation: Present scores as review prompts only and require human review before reputational, employment, legal, or social action.

Risk: Users may analyze private communications or local files without authority.

Mitigation: Prefer pasted user-provided text; require explicit consent for text-file or association-file inputs.

Risk: Users may publish or amplify detector outputs without context.

Mitigation: Do not auto-publish results, and require explicit human consent before external sharing.

Risk: Calibration metrics may be mistaken for production performance.

Mitigation: Use the 0.65 operational bar for strong-pattern language and label low-threshold calibration metrics as ranking-only.

## Reference(s):

- [AETHON D9 Blueprint](references/AETHON_D9_BLUEPRINT.md)
- [Security and Ethics](references/SECURITY.md)
- [SkillSpector / ClawHub Audit](references/SKILLSPECTOR_AUDIT.md)
- [Quickstart](examples/quickstart.md)
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-ops-detector)
- [ClawHub Package Page](https://clawhub.ai/deepseekoracle/lygo-ops-detector)
- [Project Homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/clawhub/mirrors/lygo-ops-detector)
- [Security Audit](https://clawhub.ai/deepseekoracle/skills/lygo-ops-detector/security-audit)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text report or JSON object, with Markdown quickstart guidance and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local stdlib CLI; file inputs require explicit consent; evaluation reports write under tests/ only.]

## Skill Version(s):

1.3.1 (source: frontmatter, claw.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
