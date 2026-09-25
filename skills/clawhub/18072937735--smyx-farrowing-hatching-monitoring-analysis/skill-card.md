## Description:

Monitors farrowing and poultry hatching videos to detect events such as water breaking, straining, piglet delivery, egg pipping, and chick emergence, then returns event reminders and structured results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to monitor fixed-camera video from farrowing pens or poultry hatching areas, identify key reproduction events, and retrieve current or historical cloud reports. Results are intended for monitoring support and do not provide farrowing, hatching, or veterinary operating advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monitoring media is sent to the Life Emergence cloud service for analysis.

Mitigation: Use only with media approved for third-party cloud processing, and review the service's data handling requirements before production deployment.

Risk: The skill may silently create or reuse an internal account and persist reusable access tokens locally.

Mitigation: Review token storage before installation, rotate or remove stored tokens when no longer needed, and avoid sharing the workspace with untrusted skills.

Risk: Credential persistence and authenticated request destination checks were identified as areas that need hardening.

Mitigation: Deploy in an isolated workspace until credential handling and request destination controls have been reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-farrowing-hatching-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json]

**Output Format:** [Structured text or JSON; historical report lists may be formatted as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event types, event times, priority or reminder levels, report links, and optional saved output files.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
