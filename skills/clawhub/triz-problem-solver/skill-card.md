## Description:

Generate reviewable TRIZ innovation or TRIZ/DFMA cost-reduction concepts and expand a selected concept into a detailed solution by calling the PatSnap Solution Engine MCP endpoint over plain HTTP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwt1995](https://clawhub.ai/user/wwt1995)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and product teams use this skill to analyze engineering contradictions, product redesign goals, DFMA cost-reduction opportunities, and related manufacturing or assembly optimization problems through Eureka RD.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Problem descriptions and product information are sent to PatSnap/Eureka RD.

Mitigation: Use the skill only for content appropriate to share with that service, and redact confidential designs, personal data, NDA-covered information, export-controlled details, and other sensitive material before use.

Risk: Generated concepts and detailed solutions may be incomplete or unsuitable for direct implementation.

Mitigation: Treat outputs as reviewable proposals and validate them with engineering, legal, safety, and compliance reviewers before relying on them.

Risk: Long-running service calls can be duplicated if a task is restarted after timeout or transport failure.

Mitigation: Reuse the returned job identifier for stream and detail calls, and avoid creating a replacement task unless the user explicitly agrees.

## Reference(s):

- [Eureka RD TRIZ entry point](https://eureka.patsnap.com/rd/#/agentic?type=triz&start_from=hub&utm_source=clawhub&utm_medium=skill_listing&utm_campaign=triz_innovation)
- [ClawHub skill page](https://clawhub.ai/wwt1995/skills/triz-problem-solver)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with structured TRIZ candidate summaries, solution details, and inline shell command examples for HTTP mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include job identifiers, candidate idea identifiers, TRIZ principles, DFMA details, patent-backed references, and service-returned images when present.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
