## Description:

Identifies bird species in images and videos, with support for more than 500 common species and customized model training for ecological observation and birdwatching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as birdwatchers and ecological observers can submit an image or video of a target area to identify bird species and receive a structured report with recognition results, confidence, recommendations, and report links. They can also request a list of previous analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence flags credential and identity handling, broad request behavior, and actions that are not clearly explained; one scan was partial, so the evidence is incomplete.

Mitigation: Clarify account and credential handling and check request destinations before installation; follow the security guidance to avoid installation until these points are resolved.

Risk: The security guidance says video-upload disclosure and export-only behavior need clarification.

Mitigation: Confirm what media is sent to the service and what export-only mode does before using the skill.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured analysis text or JSON with recognition results, confidence, recommendations, and report links; report lists can be presented as Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, or JSON detail levels and optional saving of results to a file.]

## Skill Version(s):

1.0.26 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
