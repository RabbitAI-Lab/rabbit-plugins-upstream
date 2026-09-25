## Description:

Analyzes close-up pet face images or videos to flag visual signs of eye abnormalities such as conjunctival redness, abnormal tearing or tear stains, and pupil or cornea opacity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, boarding center staff, animal hospital triage staff, and developers can use this skill to submit pet eye images or videos for visual anomaly alerts and report/history retrieval. The output is a visual screening aid and does not replace professional veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images or videos may be uploaded to cloud APIs and report history may be queried remotely.

Mitigation: Install only after confirming the destination endpoints, data retention expectations, and user consent requirements are acceptable.

Risk: The skill can silently create or reuse an identity and store reusable service tokens in the workspace.

Mitigation: Review identity handling and token storage before deployment, and restrict workspace access to trusted users.

Risk: Packaged default configuration includes plaintext HTTP development endpoints for some credential-bearing traffic.

Mitigation: Verify production configuration uses trusted HTTPS endpoints before running the skill with real media or credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-eye-anomaly-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON-like analysis content, report links, and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file or URL inputs, pet type selection, output detail selection, optional file output, and cloud history listing.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
