## Description:

Builds an interactive digital-human compliance course from supplied policies, regulatory summaries, and training materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

Compliance, HR, legal operations, and training teams use this skill to turn supplied policies and regulatory materials into an interactive digital-human course. The skill is intended for grounded training workflows, not for legal advice, certification, licensure, or proof of real-world compliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Learners or operators may mistake generated course content for legal compliance, certification, licensure, or professional advice.

Mitigation: Frame the output as training only, preserve obligations exactly from supplied materials, and route individual interpretations to the compliance owner named in those materials.

Risk: The workflow can upload selected source materials, use existing course credits, and change access or publication state when requested.

Mitigation: Use PersonWise only for intended compliance-course creation, upload only user-named or explicitly selected materials, avoid automatic credit purchases, and review publish or link-access actions before execution.

Risk: CLI or skill updates may be required before business commands can continue.

Mitigation: Review the exact update action before approval and keep the workflow bound to the official PersonWise market release declared by this skill.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/personwiseai/skills/personwise-compliance-training)
- [PersonWise publisher profile](https://clawhub.ai/user/personwiseai)
- [PersonWise service descriptor](artifact/assets/service-descriptor.signed.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command inputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create bounded JSON files for PersonWise course blueprints or updates and report course/run status, access mode, and URLs after CLI completion.]

## Skill Version(s):

2.1.9 (source: evidence.release.version and skill invocation attribution)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
