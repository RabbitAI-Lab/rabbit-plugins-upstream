## Description:

Derive severity assignments and record incident owner decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Incident response teams and service operators use this skill to turn service profiles and severity guidance into accountable routing guidance and incident owner assignment results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incident owner assignments can be incorrect when severity, service ownership, operating hours, or fallback queue details are incomplete.

Mitigation: Review assignment guidance and results against the current incident context before treating them as operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/incident-routing-desk)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Readable policy string or concise assignment result object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces assignment_guidance and assignment_result from user-supplied incident routing context.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
