## Description:

AI Gen Guard locally evaluates Chinese generative AI service compliance scenarios and returns risk levels, compliance check results, and suggested actions across filing, training data, content safety, user rights, and labeling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, compliance teams, and agents use this skill as an informational self-check for generative AI services offered by Chinese enterprises before launch or review. It does not replace professional legal advice or formal compliance review.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Compliance assessments may be incomplete or outdated as laws, standards, and enforcement expectations change.

Mitigation: Treat outputs as informational self-checks and confirm requirements against current regulations and qualified legal counsel.

Risk: Users could mistake the generated risk level or checklist for legal advice, compliance proof, or a regulatory submission artifact.

Mitigation: Use the result to identify review items only; do not use it as legal evidence or as a substitute for formal compliance review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/ai-gen-guard)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON compliance assessment with risk level, scenario indicators, per-dimension checks, and suggested actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Python standard library only; no external dependencies are declared.]

## Skill Version(s):

1.0.2 (source: release evidence, package.json, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
