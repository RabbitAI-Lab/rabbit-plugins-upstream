## Description:

Analyzes fixed-camera video from emergency shelters or temporary resettlement sites to identify visual behavior signals associated with acute stress, such as stupor, tremor, unresponsiveness, and hypervigilance, and returns crisis alerts for human responder review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Emergency command-center teams and authorized psychological-rescue responders use this skill to review shelter video, locate people showing potential acute stress behaviors, and prioritize follow-up support. Outputs are behavior observations and response guidance, not clinical diagnoses.

### Deployment Geography for Use:

China; adapt legal, privacy, and emergency-response procedures before use in other jurisdictions.

## Known Risks and Mitigations:

Risk: Sensitive shelter video and mental-health-related behavior inferences may affect vulnerable disaster survivors.

Mitigation: Use only in an authorized emergency-response setting with a documented consent or legal basis, privacy safeguards, face blurring for shared displays, and human review.

Risk: Submitted media, video URLs, and report history queries are sent to configured remote services.

Mitigation: Submit only approved emergency-scene media, document the remote endpoints in deployment review, and avoid embedding secrets or private identifiers in URLs.

Risk: The skill may create or reuse an internal user identity and store service tokens locally.

Mitigation: Run in a controlled workspace, restrict local file access, rotate any service tokens, and clear stored identity or token files after the response workflow when policy requires it.

Risk: False positives or overconfident interpretation could cause inappropriate escalation in an emergency scene.

Mitigation: Treat outputs as visual behavior observations only; require qualified human review before dispatch escalation, diagnosis, or intervention.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON structured report with alert details, response guidance, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save report output to a local file when requested; analysis and report history queries use configured remote services.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
