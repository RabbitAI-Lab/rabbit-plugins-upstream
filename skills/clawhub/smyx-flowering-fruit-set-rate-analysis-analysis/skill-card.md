## Description:

AI-powered flowering and fruit-set rate analysis for tomato and chili plant images or videos that counts open flowers and young fruits, computes fruit-set rate, and returns a structured report with cultivation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, greenhouse operators, and smart grow-box users use this skill to analyze tomato or chili flowering and fruit clusters, estimate fruit-set rate, and review pollination or environment-adjustment guidance. Developers and agents can also use it to query historical cloud reports for the same analysis workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or URLs are sent to the Life Emergence cloud service for analysis.

Mitigation: Use the skill only with media approved for cloud processing, avoid sensitive background content, and disclose the remote analysis step to users.

Risk: Reports are tied to an internally resolved identity and the security evidence notes local token or profile persistence.

Mitigation: Review account-linking behavior before deployment, keep credentials out of user-visible output, and clear or rotate locally persisted tokens according to environment policy.

Risk: The security evidence reports development-network defaults and mismatched pet/video documentation.

Mitigation: Verify production endpoint configuration before installation and update user-facing documentation so supported media, service endpoints, and plant-analysis scope are consistent.

Risk: Automated fruit-set analysis may produce incorrect counts or misleading cultivation guidance.

Mitigation: Treat results as decision support, review unclear images manually, and avoid relying on the skill for precise fertilizer or pesticide dosing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-flowering-fruit-set-rate-analysis-analysis)
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON analysis report with flower counts, young-fruit counts, fruit-set rate, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file or URL inputs and can save analysis output to a local file when requested.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
