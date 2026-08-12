## Description:

Detects orchid shoots, flower spikes, and visible root condition from user-provided orchid images or videos, then returns a structured growth-status assessment and care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External orchid hobbyists, greenhouse operators, and horticulture studios use this skill to assess visible growth status from orchid media, including new shoot count, flower-spike development, and root color or condition. Agents can use the output to summarize plant vitality, surface care considerations, and retrieve prior analysis reports when supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload orchid media or media URLs to lifeemergence.com services.

Mitigation: Use only media or URLs approved for that service, and avoid inputs that should not be associated with the external analysis provider.

Risk: The skill may create or reuse a local identity and store account tokens locally for report history.

Mitigation: Review local data retention before use, including how to delete the local identity database and API key files when they are no longer needed.

Risk: Historical report lookup has limited user-facing control.

Mitigation: Use the skill only where the local identity and report-history behavior is acceptable, and restrict access to local data files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-orchid-growth-status-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown report or JSON analysis output with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud-hosted report links and historical report tables.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
