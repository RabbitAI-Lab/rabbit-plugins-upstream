## Description:

Analyzes crib camera images or videos to estimate infant blanket coverage, detect kicking or blanket-slip events, and return alert-oriented monitoring results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to analyze infant crib monitoring media for blanket coverage status, kicking or blanket-slip events, alert level, and report links. It is intended as auxiliary monitoring output and does not replace adult supervision or medical judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports that sensitive child footage and authentication tokens can be sent through default plaintext HTTP endpoints.

Mitigation: Install only after the publisher removes default development HTTP endpoints and requires HTTPS for uploads, authentication, and report APIs.

Risk: The security evidence reports remote processing of infant footage without sufficient documented retention or privacy handling.

Mitigation: Require clear documentation of remote processing, retention, guardian consent, and protection of infant video before deployment.

Risk: The security evidence reports silent creation and storage of account credentials.

Mitigation: Require explicit user control over identity/account association and protect stored tokens with a credential store or encryption.

Risk: The security evidence flags a yaml/PyYAML dependency issue.

Mitigation: Confirm the dependency is corrected and installable before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Infant blanket kick detection API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON-like structured analysis report with alert status and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local media or submit a remote media URL to external analysis APIs; history queries return cloud-resolved report records.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
