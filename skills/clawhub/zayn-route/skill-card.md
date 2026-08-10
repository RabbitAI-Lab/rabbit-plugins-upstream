## Description:

Routes complex workplace requests to the right WorkFn skill or skill sequence, including inputs, handoffs, stop conditions, and the final output skill for customer, quotation, order, support, internal collaboration, market, and business-intelligence scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zaynpeng](https://clawhub.ai/user/zaynpeng)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and business workflow operators use this skill when a request may require one or more WorkFn skills and they need a clear routing decision, parameter handoff plan, stop condition, and final output skill. It is especially useful when incomplete subject, source, time, market, or research-boundary evidence should stop downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Routing output could recommend too many skills, duplicate responsibilities, or make a simple request unnecessarily complex.

Mitigation: Apply the skill's single-skill-first rule, cap normal chains at five skills, and review each recommended step for a real dependency before acting on it.

Risk: Incomplete or weak evidence could be passed downstream as confirmed business facts.

Mitigation: Stop when required subject, source, jurisdiction, market, time range, or research-boundary details are missing, and preserve unverified or conflicting information as unverified.

Risk: The recommended WorkFn skill names may not exist or may differ in a target agent environment.

Mitigation: Map the recommended skill names to installed local skills before relying on the route, especially because the security review notes that the artifact provides recommendations rather than automatic execution.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown with parameter status tables, routing decisions, skill-chain tables, handoff notes, stop conditions, and final-skill guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operates primarily in Chinese and produces routing recommendations rather than executing the underlying business skills.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact documents ROUTE v0.1.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
