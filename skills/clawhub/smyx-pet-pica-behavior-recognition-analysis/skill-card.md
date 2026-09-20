## Description:

Pet Pica Behavior Recognition analyzes indoor camera videos or video URLs through remote APIs to detect pets contacting non-food hazardous items such as electric wires, plastic bags, socks, tissues, and toy fragments, and outputs warning-oriented safety guidance without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and smart-home or pet-safety operators use this skill to analyze indoor pet video, identify possible chewing or pica contact with hazardous non-food objects, and receive structured warnings, recommendations, and report links. The output is safety-monitoring support only and should not be treated as veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private indoor-camera videos or video URLs may be uploaded to a remote service with unclear retention and deletion terms.

Mitigation: Avoid sensitive household footage unless the publisher documents data handling, retention, deletion, and secure transport guarantees.

Risk: The skill can silently create or reuse an account identity and store reusable tokens locally.

Mitigation: Run in an isolated workspace, review local credential storage before reuse, and clear stored identity or token files when the skill is no longer needed.

Risk: Configuration evidence includes insecure HTTP defaults for some service endpoints.

Mitigation: Use only HTTPS service endpoints and verify the configured API URL before executing analysis or report-history queries.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-pica-behavior-recognition-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Pet Pica API Documentation](references/api_doc.md)
- [Analysis API Error Reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Structured text or JSON with warning status, risk descriptions, recommendations, report history, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local mp4, avi, and mov video files up to 10 MB or remote video URLs; report history is retrieved from the remote service.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
