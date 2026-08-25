## Description:

Map incident severity and service context to an accountable response owner and queue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Incident response and service operations teams use this skill to turn a supplied service_profile into accountable alert-routing guidance. It identifies the response lead, service queue, triage fallback, and operating-hours condition without creating alerts or pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect or incomplete service_profile data can produce misleading assignment guidance.

Mitigation: Verify severity scale, service owner, response lead, operating hours, and fallback queue before relying on the generated policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/alert-escalation-guidance-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [String]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns assignment_guidance as a single readable policy string.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
