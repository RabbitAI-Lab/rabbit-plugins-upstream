## Description:

Analyzes fixed-camera images or video of windows and balconies to identify child climbing, leaning, gripping, or other fall-risk behaviors and return alerts with structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, safety operators, and smart-camera integrators use this skill to analyze footage aimed at windows or balconies for child fall-risk behaviors and to retrieve cloud-hosted historical alert reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload sensitive home footage, child-related video, report metadata, and identity values to the publisher's cloud service.

Mitigation: Use only with appropriate consent, confirm that uploaded footage is expected for the deployment, and avoid real footage until privacy handling is approved.

Risk: Security evidence reports plaintext development endpoints and reusable local token storage.

Mitigation: Require HTTPS production endpoints, harden token storage, and review account and history-report access before deployment.

Risk: The skill is an auxiliary safety alerting tool and may not detect every hazardous event.

Mitigation: Keep adult supervision and operational safeguards in place, and treat alerts as support for monitoring rather than a replacement for supervision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-window-climbing-detection-analysis)
- [Skill usage demo](https://lifeemergence.com/sample.html)
- [Child climbing detection API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown or JSON analysis reports with alert fields, report links, and optional shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file when an output path is provided.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
