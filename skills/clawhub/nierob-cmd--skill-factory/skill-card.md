## Description:

Design, build, evaluate, and optimize production-ready Agent Skills for ClawHub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nierob-cmd](https://clawhub.ai/user/nierob-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use Skill Factory to create, redesign, evaluate, and prepare reusable Agent Skills for publication. It guides architecture choice, trigger boundaries, portability review, security checks, and publication readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or revised skills may include scripts, network integrations, or credential-dependent workflows that change the security posture of the final package.

Mitigation: Review generated skills before publishing or installing them, and scan outputs for scripts, external integrations, credential handling, and portability issues.

Risk: Skill design guidance can produce incorrect trigger boundaries or misleading publication readiness claims if the requested capability is underspecified.

Mitigation: Use realistic positive, hard-negative, borderline, and adversarial trigger evaluations before marking a skill publish-ready.

## Reference(s):

- [Skill Mechanics](references/skill-mechanics.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with generated or revised skill package files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include an architecture decision, validation result, assumptions, limitations, changelog, and publication metadata.]

## Skill Version(s):

2.0.0 (source: release metadata and README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
