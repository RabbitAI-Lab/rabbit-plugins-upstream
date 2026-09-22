## Description:

Provides Chinese-language informational travel-insurance guidance, including scenario-based coverage recommendations, plain-language coverage explanations, and claim-process checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask for travel-insurance buying guidance, coverage-term explanations, Schengen and destination-specific coverage considerations, and claim preparation steps. The skill is informational only and directs users to verify final decisions with official insurance providers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake insurance recommendations or claim steps for individualized insurance advice or guaranteed claim outcomes.

Mitigation: Present the skill as informational guidance and direct users to verify coverage terms, eligibility, purchase choices, and claim decisions with official insurers or providers.

Risk: The artifact declares PROXY_TOKEN even though the skill describes itself as zero-configuration.

Mitigation: Ask the publisher to remove or document the environment variable before deployment, and avoid supplying credentials that are not needed for the intended guidance workflow.

Risk: The security guidance identifies Python syntax errors and quality issues that may make tool behavior unreliable.

Mitigation: Fix the source errors and re-scan before relying on executable tool behavior; treat the release as informational guidance until corrected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/travel-insurance-smart-buy)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style Chinese-language guidance with structured recommendations, checklists, links, and claim steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Informational guidance only; the artifact states it does not sell insurance, process payments, store user data, or transmit personal information to third parties.]

## Skill Version(s):

2.0.3 (source: server release metadata; artifact _meta.json reports 2.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
