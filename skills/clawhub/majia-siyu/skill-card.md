## Description:

A Chinese-language private-domain growth assistant for customer messaging, WeChat engagement, business diagnosis, and market research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT-0

## Use Case:

External growth and operations teams use this skill to create customer-facing messages, assess private-domain engagement needs, plan operational improvements, and organize follow-up work. It also supports vendor and market comparisons and customer-context documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vague requests may lead to saved client information being read or combined.

Mitigation: Require explicit client selection before accessing or combining archives; prefer redacted saves and protect the unencrypted ~/.siyu directory.

Risk: The updater may change skills across multiple agents.

Mitigation: Review a fixed release and limit installation to the intended skill and agent; avoid the global --all workflow.

Risk: The server release license and source skill license metadata differ.

Mitigation: Confirm the applicable license terms before reuse or redistribution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/maojiebc/skills/majia-siyu)
- [Project homepage (release metadata)](https://github.com/maojiebc/majia-siyu-team)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese natural-language responses, structured Markdown, and reusable message or planning templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content and recommendations are tailored to the user's stated business context.]

## Skill Version(s):

2.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
