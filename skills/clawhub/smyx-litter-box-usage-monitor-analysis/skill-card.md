## Description:

Analyzes litter-box video to track each cat's visit frequency and duration, compare them with historical patterns, and flag behavioral changes without providing a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, catteries, veterinary teams, and boarding staff use litter-box video to review individual cats' visit patterns and receive behavioral alerts; the results are not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private pet-monitoring videos or URLs are sent to an external cloud service.

Mitigation: Confirm the provider's retention, deletion, account creation, and report-access terms before submitting real household, clinic, or boarding footage.

Risk: Automatically reused local identities and stored cloud tokens can expose private reports in shared workspaces.

Mitigation: Avoid shared or multi-user workspaces until identity isolation is fixed; protect workspace access and stored tokens.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-litter-box-usage-monitor-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Structured analysis report or Markdown history table, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavioral alerts, suggestions, and report links.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
