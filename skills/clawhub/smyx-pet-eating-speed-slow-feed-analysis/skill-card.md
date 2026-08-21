## Description:

Analyzes pet food-bowl videos or video URLs to estimate eating start and end times, feeding duration, eating speed, and slow-feed intervention recommendations without providing disease diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet eating behavior from bowl-area videos, generate structured reports, and decide whether slow-feed reminders or device-side interventions should be considered. It is intended for pet health management and smart slow-feeder workflows, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos and report history are processed through cloud APIs, which may expose sensitive household or account-linked media.

Mitigation: Use only videos appropriate for cloud processing and require the publisher to disclose media retention, processing location, and access controls before broad deployment.

Risk: The skill silently creates or reuses account identity and stores access tokens locally.

Mitigation: Run in an isolated workspace, review local token storage behavior, and ensure users know how account identity is provisioned and revoked.

Risk: Development or internal API endpoint configuration can route analysis or history queries to unintended services.

Mitigation: Replace dev/internal endpoints with production HTTPS endpoints and verify authorization on history-report queries before commercial use.

Risk: Eating-speed analysis could be mistaken for medical advice.

Mitigation: Present results as behavioral observations and slow-feeding suggestions only, and direct medical concerns to a veterinarian.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-eating-speed-slow-feed-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Pet Eating Speed API Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with timestamps, speed estimates, risk notes, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud-hosted analysis and history-report APIs; local file or URL video inputs are supported.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
