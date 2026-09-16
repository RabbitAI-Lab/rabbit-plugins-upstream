## Description:

Detects electric motorcycles and e-bikes in restricted areas from images or video streams, reports counts and violation severity, and returns safety-management alerts and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security operations teams, facility managers, and developers use this skill to analyze surveillance images or video streams for electric bikes and motorcycles in restricted areas. The skill supports violation counting, severity reporting, historical report lookup, and safety-management recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance media, report history, and credentials may be sent to remote services, including cleartext development HTTP endpoints if unsafe configuration is used.

Mitigation: Run only after replacing development endpoints with trusted HTTPS endpoints and confirming the destination service, retention policy, and access controls.

Risk: The skill can silently create or reuse identities and persist account tokens locally.

Mitigation: Use a controlled workspace with restricted filesystem permissions, inspect token storage before deployment, and rotate or revoke tokens after testing.

Risk: Computer-vision detections may be incomplete or incorrect and can affect safety-management decisions.

Mitigation: Treat reports as decision support and require human review before enforcement or operational action.

## Reference(s):

- [Electric Vehicle Detection API Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-electric-vehicle-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON reports with optional shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a result file when --output is supplied; supports basic, standard, and json detail levels.]

## Skill Version(s):

9.9.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
