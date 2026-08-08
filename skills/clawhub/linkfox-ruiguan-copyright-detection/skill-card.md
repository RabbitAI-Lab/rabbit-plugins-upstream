## Description:

Checks image URLs against Ruiguan copyright-detection data to surface similar registered works, rights-owner details, TRO indicators, and infringement-risk signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, designers, and e-commerce teams use this skill to check product or design images before publication. It returns similarity matches, rights-owner details, TRO flags, and factual risk signals for review, without replacing legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send image URLs or uploaded local images to LinkFox services for copyright analysis.

Mitigation: Use it only for images the user is comfortable sharing with LinkFox, and avoid private or pre-release assets unless a temporary public upload is acceptable.

Risk: Authentication, SMS login, API key generation, and payment flows can expose sensitive account or billing information.

Mitigation: Ask for explicit user authorization before account or payment steps, avoid displaying secrets unnecessarily, and direct users to official LinkFox account flows when possible.

Risk: Detection results and cache files may be stored locally under a linkfox session directory.

Mitigation: Tell users where result files are saved and remove generated result or cache files when they contain sensitive image URLs or analysis results.

Risk: Copyright similarity and TRO indicators can be mistaken for definitive legal conclusions.

Mitigation: Present results as factual detection signals and recommend legal counsel for final copyright or infringement decisions.

## Reference(s):

- [Ruiguan Copyright Detection API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-copyright-detection)
- [ClawHub publisher profile](https://clawhub.ai/user/linkfox-ai)

## Skill Output:

**Output Type(s):** [text, markdown, JSON files, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with JSON API responses and saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full detection responses to a local linkfox session data directory and may summarize large responses in stdout.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
