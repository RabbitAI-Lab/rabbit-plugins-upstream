## Description:

Analyzes dog toilet-area or outdoor dog-walking images, videos, files, or URLs to identify pet stool color, shape, and visible blood or mucus, then returns structured observation results and abnormal-feature prompts without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to analyze pet stool media from dog toilets, outdoor walking paths, pet health monitoring setups, and multi-pet households for standardized visual observations and abnormal-feature prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media files or submitted URLs are sent to configured analysis services.

Mitigation: Use only with media and URLs the user is comfortable sharing with the configured service, and avoid private files or internal URLs.

Risk: The skill can silently create or reuse an account identity and store tokens or history state locally.

Mitigation: Review workspace data storage and account/session behavior before installation or execution in shared environments.

Risk: The configured service endpoints determine where analysis and history queries are sent.

Mitigation: Confirm endpoint configuration is intended for the deployment environment before use.

Risk: Health observations could be misunderstood as veterinary diagnosis or treatment advice.

Mitigation: Present results as visual stool observations and abnormal-feature prompts only, and refer diagnosis or treatment decisions to qualified veterinary professionals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-stool-morphology-recognition-analysis)
- [Skill API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Structured analysis report, Markdown history table, or JSON result depending on invocation mode and detail level.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include observation fields, abnormal-feature prompts, suggestions, cloud report links, and historical report listings.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata; artifact frontmatter states 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
