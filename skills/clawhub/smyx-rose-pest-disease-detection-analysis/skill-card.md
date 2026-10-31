## Description:

Analyzes images or videos of roses for common pests and diseases and returns likely findings, severity, and general care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External gardeners and rose growers use this skill to review rose leaf, shoot, and bud images or videos for likely pest or disease symptoms, assess severity, and get general care suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags possible cross-user report mixing, credential handling problems, and an export-only option that may not work as expected.

Mitigation: Wait for fixes before shared-workspace use; require sender-specific accounts, verify export-only behavior, restrict credential requests to trusted HTTPS destinations, and establish explicit registration and token-storage controls.

Risk: Images and videos are sent to Life Emergence for processing; remote retention and server-side authorization were not verified, and service charges may apply.

Mitigation: Avoid submitting sensitive media and confirm the service's retention and charge terms before use.

## Reference(s):

- [Skill page](https://clawhub.ai/18072937735/skills/smyx-rose-pest-disease-detection-analysis)
- [Rose analysis demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report in text or JSON, with Markdown report listings when querying history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports likely pest or disease type, severity, general care suggestions, and report links when available.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
