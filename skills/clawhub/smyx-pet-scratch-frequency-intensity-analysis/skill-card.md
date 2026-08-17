## Description:

Analyzes cat scratch post video or image inputs through configured server APIs to identify scratching behavior, estimate frequency, session duration, and relative intensity, and return structured observations about stress level and claw health without diagnosing disease or prescribing behavior correction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and pet-care operators use this skill to analyze cat scratch post videos or image inputs for scratching frequency, duration, relative intensity, stress signals, claw-health observations, and historical cloud report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, local files, or video URLs may be sent to a configured backend service for analysis.

Mitigation: Use only non-sensitive media or trusted URLs, and confirm the backend endpoint and retention expectations before running the skill.

Risk: The skill creates or reuses local identity state and stores service tokens locally.

Mitigation: Review local identity and token storage before installation, restrict filesystem access where possible, and avoid running the skill in shared environments without cleanup controls.

Risk: Configuration includes development and private-IP endpoint settings.

Mitigation: Review endpoint configuration before execution and use only trusted production endpoints for normal releases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-scratch-frequency-intensity-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON structured analysis report, optionally written to a local output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and historical report tables returned by the configured backend.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
