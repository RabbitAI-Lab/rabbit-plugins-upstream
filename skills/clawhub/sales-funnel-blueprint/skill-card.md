## Description:

Turn an offer into a concrete multi-step sales funnel spec: page-by-page structure, price ladder, copy outline, and the metrics each step must hit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autonnel](https://clawhub.ai/user/autonnel)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, founders, and funnel builders use this skill to convert an offer and traffic context into a build-ready sales funnel plan with page structure, pricing, metrics, launch instrumentation, build order, and assumptions to confirm.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional self-hosted Docker setup path could expose services or mishandle secrets if run without review.

Mitigation: Before running Docker, review the repository, release tag, docker-compose.yml, images, exposed ports, and secret handling, preferably in a test environment without production credentials.

Risk: Generated funnel recommendations can be misleading if required offer, traffic, awareness, fulfillment, or existing-asset inputs are missing.

Mitigation: Ask for missing inputs, state assumptions explicitly, and treat benchmark conversion ranges as starting targets rather than promises.

## Reference(s):

- [Sales Funnel Blueprint on ClawHub](https://clawhub.ai/autonnel/skills/sales-funnel-blueprint)
- [Autonnel repository](https://github.com/autonnel/autonnel)

## Skill Output:

**Output Type(s):** [markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown document with structured funnel specifications and optional inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes chosen funnel shape, page-by-page specs, price ladder, instrumentation blockers, build order, and open assumptions.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
