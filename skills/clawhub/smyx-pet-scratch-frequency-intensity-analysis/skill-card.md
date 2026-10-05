## Description:

Analyzes cat scratch-post videos to summarize scratching frequency, duration, and estimated intensity, with observational stress and paw-health indicators rather than a diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers use a scratch-post video or video URL to review scratching patterns, including frequency, session length, and relative intensity. Results support behavioral observation, not veterinary diagnosis or behavior-correction advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or video URLs are sent to lifeemergence.com services for analysis.

Mitigation: Obtain consent before sending videos and avoid submitting sensitive footage or private URLs.

Risk: The skill may create or reuse a service identity and store authentication tokens and report-history links locally.

Mitigation: Confirm account creation before use and protect or remove stored credentials and report data as appropriate.

Risk: Cloud report-history queries may retrieve previously submitted analyses without an explicit prompt.

Mitigation: Require explicit confirmation before history lookups.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-scratch-frequency-intensity-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured observation report or JSON, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide a history listing or save results to a file; estimates of intensity are relative to video conditions.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release; bundled frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
