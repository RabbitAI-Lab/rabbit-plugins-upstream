## Description:

Retrieves patent description and specification data from the Zhihuiya patent database by patent ID or publication number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve full patent description text for one or more known patents, identified by internal Zhihuiya patent ID or publication number.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox API keys and can guide phone/SMS account login.

Mitigation: Review configured LINKFOX_* environment variables, use only trusted LinkFox endpoints, and avoid exposing API keys or verification codes in shared logs.

Risk: Patent lookup and onboarding flows can consume paid credits or create payment orders after user selection.

Mitigation: Confirm credit costs, plan selection, and payment method with the user before running paid lookup or order commands.

Risk: Full lookup responses are saved locally and may contain sensitive patent research data.

Mitigation: Run the skill from an appropriate workspace, review saved JSON files, and remove local session/cache data when retention is not desired.

Risk: The skill can report feedback to a separate LinkFox endpoint.

Mitigation: Review feedback content before submission and avoid including secrets, private patent strategy, or unnecessary personal data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-description-data)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and local JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full lookup responses are saved under a local linkfox session directory; large responses are summarized unless inline output is requested; repeated queries can use a 24-hour local cache.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
