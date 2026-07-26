## Description: <br>
Manages the full lifecycle of training certificates, including template design, certificate generation, issuance, verification, renewal, upgrade, revocation, and reissue workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golngod](https://clawhub.ai/user/golngod) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Training administrators and credential program owners use this skill to plan certificate templates, track trainee certificate records, manage issuance and delivery, and document verification, renewal, revocation, and reissue workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Certificate workflows may handle trainee names, ID numbers, training records, certificate status, delivery tracking, and verification links. <br>
Mitigation: Limit inputs to necessary certificate fields, mask ID numbers where possible, restrict access to certificate records and verification links, and define retention and deletion rules before use with real trainees. <br>
Risk: Certificate issuance, revocation, and reissue decisions can affect learner credentials if applied without review. <br>
Mitigation: Treat generated workflow output as advisory and require the certificate program owner to approve final issuance, revocation, and reissue actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golngod/skills/training-certificate-mgmt) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown with structured certificate fields, workflow steps, and data model guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are advisory; final certificate issuance, revocation, and data-retention decisions require owner review.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, clawhub.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
