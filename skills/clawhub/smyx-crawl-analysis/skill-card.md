## Description:

Analyzes uploaded or linked reptile and arachnid videos for visible health concerns and returns a structured report with potential risks and care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caretakers use the skill to request visual health screening of reptile or arachnid videos and retrieve prior analysis reports. Results are for health reference and do not replace diagnosis by a qualified veterinarian.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account handling may mix reports across different users.

Mitigation: Wait for account-isolation fixes before using the skill with multiple users.

Risk: Videos are sent to the lifeemergence.com service, and the export-only option may still upload them; service retention is not established by the evidence.

Mitigation: Confirm the service's retention policy before sending private footage, and do not treat export-only mode as local-only processing.

Risk: The service may register an account automatically and retain credentials locally.

Mitigation: Use the skill only in a trusted environment and protect the locally retained credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crawl-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Report links]

**Output Format:** [Structured health report with findings, risk notices, care suggestions, and report links; JSON output is supported.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can display a Markdown table of cloud history reports and optionally save output to a file.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
