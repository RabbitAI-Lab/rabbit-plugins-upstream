## Description:

Analyzes aquarium pet images, videos, or URLs for visible health indicators, calls a server-side health analysis API, and returns a structured fish and aquatic pet health report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and aquarium enthusiasts use this skill to review uploaded aquatic pet media for visible disease, activity, color, scale, and fin indicators. Agents can also use it to retrieve cloud-hosted historical analysis reports for the same skill account context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media, account linkage data, or credentials may be sent to plaintext development endpoints.

Mitigation: Require a production HTTPS configuration before installation or execution, and verify that development endpoints are removed or disabled.

Risk: The skill links users to cloud accounts and stores tokens locally.

Mitigation: Document identity handling and token storage, rotate any tokens used with earlier configurations, and give users clear control over uploads and history lookup.

Risk: Aquatic health analysis can be incomplete or incorrect.

Mitigation: Present reports as reference guidance only and direct users to professional veterinary care for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, files, shell commands, guidance]

**Output Format:** [Markdown or JSON health report, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, historical report tables, and health guidance; results are for reference and do not replace professional veterinary diagnosis.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
