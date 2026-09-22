## Description:

Analyzes pet images or videos for cat, dog, bird, or other pet health checks, producing structured health findings, care suggestions, and report links through a cloud API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit pet media for health-oriented analysis, receive a structured Pet Safety Guardian report, and query historical reports associated with the current internal user identity. The outputs are health references and are not a substitute for professional veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and report requests are sent to a cloud service, and retention or deletion behavior is not server-verified in the release evidence.

Mitigation: Use only media appropriate for third-party processing until the publisher documents retention, deletion, and data handling commitments.

Risk: The security summary reports that default configuration can send sensitive data over unencrypted HTTP despite documentation claiming HTTPS.

Mitigation: Require HTTPS-only production endpoints and verify the effective runtime configuration before installation or use.

Risk: The skill silently creates or reuses an internal cloud identity and can store reusable service tokens locally.

Mitigation: Run in an isolated workspace, avoid shared local storage, and require the publisher to remove or securely scope local token storage.

Risk: Health-analysis output may be mistaken for a professional veterinary diagnosis.

Mitigation: Present results as informational health references and route urgent or uncertain findings to a licensed veterinarian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis)
- [Pet health analysis API documentation](references/api_doc.md)
- [Common AI analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text containing structured JSON-like analysis results, status messages, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; history-list output is returned as structured text from the cloud API.]

## Skill Version(s):

999.999.1007 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
