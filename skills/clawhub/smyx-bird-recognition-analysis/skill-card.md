## Description:

Identifies bird species in images or videos of target areas, covering at least 500 common species and supporting customized model training for ecological observation, garden bird watching, and related scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to identify bird species from image or video inputs, receive structured recognition results, and retrieve historical bird-recognition reports from the configured cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user media or media URLs to a remote service for analysis.

Mitigation: Review endpoint configuration and data-handling terms before use, and only submit media that is appropriate for the configured third-party service.

Risk: Security evidence reports insecure plaintext development endpoints and locally persisted service tokens.

Mitigation: Use HTTPS-only production endpoints, remove private development defaults, and protect or avoid stored service tokens before normal use.

Risk: The skill creates or reuses an internal user identity and retrieves cloud report history.

Mitigation: Make identity and history behavior explicit to users and confirm that report access is scoped to the intended account before deployment.

## Reference(s):

- [Bird Recognition API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-bird-recognition-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration]

**Output Format:** [Markdown or JSON analysis output with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload media or pass media URLs to a remote API and can save analysis output to a local file when requested.]

## Skill Version(s):

1.0.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
