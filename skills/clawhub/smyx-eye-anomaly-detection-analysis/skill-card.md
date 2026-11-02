## Description:

Analyzes close-up pet eye images or videos for visible signs of redness, abnormal tearing, and eye opacity, then returns alerts and guidance for veterinary follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers can use the skill to review close-up images or videos for visible eye changes and monitor reports over time. Treat its results as visual alerts, not a veterinary diagnosis, and consult a veterinarian about suspected abnormalities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and videos are sent to LifeEmergence for processing, and the skill automatically registers an account and stores login tokens locally.

Mitigation: Avoid sending private footage, review the service's retention and pricing terms, and use a separate workspace for sensitive accounts.

Risk: The --export-env-only and --api-url options do not reliably prevent processing or redirect requests.

Mitigation: Do not rely on these options to control processing or destination; use the service only after both controls are fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-eye-anomaly-detection-analysis)
- [Skill introduction](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Guidance]

**Output Format:** [Structured visual analysis report with alerts, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are visual indicators only and do not provide a veterinary diagnosis.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
