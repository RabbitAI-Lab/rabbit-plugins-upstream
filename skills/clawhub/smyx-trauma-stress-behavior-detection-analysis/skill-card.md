## Description:

Analyzes fixed-camera video in emergency shelters for behaviors associated with acute stress and produces alerts for on-site psychological-rescue teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized emergency response teams and shelter operators can use the skill to review shelter video for observable behavior patterns and produce location-based alerts, response suggestions, and psychological first aid guidance. Deployment requires authorization and qualified on-site psychological-rescue staff; high-risk alerts should receive human review before dispatch.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: ClawScan marked the release suspicious and recommended against installing, citing gaps in its understanding of the remote service, account creation, credential storage, and video handling. The scan was partial because a referenced local path was missing.

Mitigation: Before deployment, resolve how the remote service works, what accounts and credentials are created or stored, when footage is uploaded, and whether export-only requests can start analysis; review behavior not covered by the partial scan.

Risk: Shelter footage can contain sensitive, identifiable people, and the security review did not establish the exact data-handling behavior.

Mitigation: Confirm video destinations and retention before use; limit footage to authorized rescue work, blur faces on command-center displays, and follow the documented short-retention limits.

Risk: The bundled skill frontmatter reports version 1.0.23 while the target release metadata reports version 1.0.18.

Mitigation: Confirm that the bundled files are the intended contents for release 1.0.18 before deployment.

Risk: Behavioral alerts in a crisis setting may be mistaken for a clinical diagnosis or trigger an inappropriate dispatch.

Mitigation: Treat results as behavioral observations only, require qualified on-site psychological-rescue staff, and have a human review high-risk alerts before dispatch.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Guidance]

**Output Format:** [Structured text or JSON report with behavior observations, alerts, response suggestions, and psychological first aid guidance; history lists may be presented as Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video or image path or URL as input. Outputs are behavior observations and alerts, not clinical diagnoses; high-risk alerts require human review.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
