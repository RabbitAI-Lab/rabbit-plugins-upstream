## Description:

Analyzes fixed-camera medication-area video to detect pick-up, to-mouth, and swallow steps, then reports whether an elderly person appears to have completed the medication action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, elder-care operators, and developers use this skill to analyze medication-area video or history records for visual compliance signals. It reports observed action steps, compliance status, missed-step indicators, confidence, alerts, snapshots, and report links without providing medical treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive home medication video and health-related observations.

Mitigation: Use it only with explicit consent, clear retention and deletion rules, protected storage, and appropriate access controls.

Risk: The skill may upload media, retrieve cloud history reports, reuse or create an account identity, and store tokens locally.

Mitigation: Confirm the publisher, backend service, deployment model, scoped authorization, and token handling before handling real elderly-care footage.

Risk: Plaintext development endpoints or non-production service configuration can expose sensitive inputs.

Mitigation: Configure HTTPS-only production endpoints before deployment.

Risk: Visual compliance detection may be incomplete or uncertain and is not medical advice.

Mitigation: Use outputs as assistive signals, manually verify missed or uncertain medication events, and do not adjust medication plans from this skill output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-medication-compliance-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-style structured analysis report with compliance fields, alert text, report links, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload image or video inputs to a backend service and may query cloud history reports for the resolved account identity.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
