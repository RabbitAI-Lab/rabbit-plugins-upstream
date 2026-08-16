## Description:

Auto-generate a professional, client-ready GEO service proposal from audit data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and GEO consulting teams use this skill to turn GEO audit findings into client-ready service proposals with tiered packages, pricing, timelines, and terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be invoked broadly by proposal-related phrases and may act on unintended audit or prospect data.

Mitigation: Invoke it explicitly with /geo proposal and review the selected domain, audit file, and target paths before allowing writes.

Risk: The skill may update local business prospect records without a separate confirmation step.

Mitigation: Review generated proposals and any prospect status changes before using them with real client or sales data.

## Reference(s):

- [geo-proposal on ClawHub](https://clawhub.ai/asale-ai/skills/geo-proposal)
- [asale-ai publisher profile](https://clawhub.ai/user/asale-ai)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown proposal document with confirmation text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes proposal files and may update local prospect status records under ~/.geo-prospects.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
