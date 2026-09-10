## Description:

Veritier lets agents extract and verify falsifiable claims in text, documents, and planned actions against web evidence, private references, or systems of record, returning verdicts, confidence, sources, and optional action credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[salomonhenao](https://clawhub.ai/user/salomonhenao)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and agent builders use this skill to fact-check draft answers, user-provided text, URLs, PDFs, images, and tool-call claims before acting on them. It is especially useful for hallucination audits, document authenticity checks, private-reference verification, and fail-closed action attestation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected text, URLs, documents, and private references to Veritier for checking.

Mitigation: Use it only for material you are comfortable submitting to Veritier, and avoid sending confidential information unless that sharing is permitted.

Risk: Credentialed checks can create public workpapers retained for 400 days.

Mitigation: Avoid putting confidential or sensitive material into credentialed checks unless public reconstruction during the retention period is acceptable.

Risk: The JavaScript integration test can use an environment-controlled API_URL while sending an API credential.

Mitigation: Run integration tests with a vt_test_ key, keep API_URL fixed to https://api.veritier.ai, and do not run tests from an untrusted environment.

Risk: Example dependencies may not match an organization's production security requirements over time.

Mitigation: Review and pin dependency versions before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/salomonhenao/skills/veritier-fact-checking)
- [Veritier website](https://veritier.ai)
- [Veritier documentation](https://veritier.ai/docs)
- [Veritier skill source](https://veritier.ai/skill.md)
- [Veritier examples README](https://veritier.ai/README.md)
- [Veritier MCP endpoint](https://api.veritier.ai/mcp/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration, code examples, and structured API result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include extracted claims, verdicts, confidence scores, source URLs, allow/block/escalate decisions, and credential verification URLs.]

## Skill Version(s):

3.4.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
