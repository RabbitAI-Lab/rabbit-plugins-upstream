## Description:

Assesses frog skin moisture from high-resolution images or videos by evaluating glossiness, wrinkles, white film, species context, and image quality to produce hydration-risk reports and recommended keeper actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, keepers, amphibian farms, and animal-care teams use this skill to analyze frog skin images or videos for visual moisture indicators, dehydration-risk levels, and follow-up care guidance. It can also query account-linked historical analysis reports from the configured cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Frog images, videos, URLs, and report history may be sent to or queried from the configured cloud service.

Mitigation: Require explicit user consent before analysis or history lookup, disclose the configured service destination, and avoid submitting sensitive media unless the user accepts the data flow.

Risk: The skill can silently create or reuse account identity and read or store local identity tokens.

Mitigation: Use a managed secret store, avoid implicit reads from data/smyx-api-key.txt, scope credentials to the task, and clear local tokens according to retention policy.

Risk: Development or private endpoints in configuration could route data to unintended services.

Mitigation: Remove non-production endpoint files or block their use before deployment, and pin reviewed production endpoints in configuration.

Risk: Visual moisture assessment can be mistaken for veterinary diagnosis or treatment advice.

Mitigation: Keep outputs limited to visual hydration indicators and general keeper actions, include the stated disclaimer, and direct severe or repeated alerts to a professional amphibian veterinarian.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-frog-skin-moisture-assessment-analysis)
- [API Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports and tables, JSON analysis details, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include glossiness scores, wrinkle scores, white-film detection, alert levels, recommended actions, disclaimers, and cloud report links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter and changelog mention 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
