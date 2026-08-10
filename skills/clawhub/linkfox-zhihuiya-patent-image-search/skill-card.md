## Description:

Searches the Zhihuiya patent database by image URL or uploaded local image to find visually similar design patents for patent risk review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, product teams, and patent reviewers use this skill to search for visually similar design patents from product images, narrow results by country or Locarno classification, and review possible design patent risk. The results support triage and prior-art research, not legal conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image URLs, uploaded local images, API keys, session metadata, and phone-number-based onboarding data may be sent to LinkFox or Zhihuiya.

Mitigation: Use the skill only with user approval for those data transfers, and avoid confidential designs unless that sharing is acceptable.

Risk: Searches consume credits and the onboarding flow can initiate payment actions.

Mitigation: Confirm with the user before searches that incur credits and before any billing, purchase, or payment step.

Risk: Search responses and cache files can persist locally under linkfox session directories.

Mitigation: Review and delete generated linkfox data or cache files after searches involving sensitive product images or patent analysis.

Risk: Automatic feedback reporting may submit user sentiment or issue details to LinkFox.

Mitigation: Use explicit confirmation before feedback submission, especially when the feedback could reveal confidential context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-image-search)
- [Zhihuiya patent image search API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API parameters, shell commands, and saved JSON response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search responses are saved under linkfox session data; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
