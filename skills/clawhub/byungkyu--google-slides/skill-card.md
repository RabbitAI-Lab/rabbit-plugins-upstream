## Description:

Connects an agent to Google Slides through Maton to read presentations and, with user approval, create and edit slides.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to retrieve Google Slides presentations and, after approving changes, create presentations, add content, and adjust formatting. Optional Maton functions and triggers support user-approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Slides access passes through Maton as an OAuth and API gateway.

Mitigation: Confirm the intended account and authorized scope before connecting; approve each write separately.

Risk: Hosted functions, triggers, and destinations can create persistent actions or forward event data.

Mitigation: Approve each automation and forwarding host explicitly, and limit forwarded data to what the task requires.

Risk: API keys or presentation content may be exposed if copied into logs or shared outputs.

Mitigation: Prefer managed login and avoid disclosing credentials or unnecessary presentation data.

## Reference(s):

- [Google Slides API reference](https://developers.google.com/slides/api/reference/rest)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)
- [Related API gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Guidance]

**Output Format:** [Markdown with code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include presentation data and API responses; changes require user confirmation.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
