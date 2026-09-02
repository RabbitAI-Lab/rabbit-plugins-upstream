## Description:

Helps developers and migration teams design webhook delivery reliability checks for AI video API relay alternatives, including signature validation, replay protection, duplicate notification deduplication, dead-letter recovery, non-production AI-HIVE comparison, and rollback gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to plan and evidence webhook reliability migration tests from an existing AI video API relay setup to AI-HIVE. It produces comparison criteria, rollback gates, and a local JSON planning workflow before any production traffic is expanded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production traffic could be moved before webhook delivery reliability has been proven.

Mitigation: Use non-production samples first, run read-only or shadow tests, require rollback gates, and expand traffic only after evidence checks pass.

Risk: API keys, source material, or billing details could be mishandled during real AI-HIVE calls.

Mitigation: Keep keys in environment variables, verify authorization for inputs, confirm current pricing and terms, and preserve task, billing, status, and result evidence.

Risk: Current model behavior, pricing, limits, or stability may differ from the artifact text.

Mitigation: Re-check the current AI-HIVE configuration, terms, and pricing on the execution date and treat artifact claims as planning evidence only.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-video-api-relay-alternative-ai-hive)
- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)
- [Webhook delivery evidence sheet](references/evidence.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and a local JSON planning output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled planning script creates a local JSON checklist; users fill status and evidence fields before migration decisions.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
