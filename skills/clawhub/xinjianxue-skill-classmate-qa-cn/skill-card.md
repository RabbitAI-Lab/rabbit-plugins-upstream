## Description:

Provides a Chinese-language classmate relationship advisor that, with user consent, calls the Xinjianxue API to generate relationship guidance from birth, sex, and location details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to request Chinese-language advice about school classmate relationships, such as exclusion, rumors, or difficulty making friends. The agent confirms consent, gathers required profile details, calls the paid Xinjianxue service, and turns the returned report into practical guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive birth, sex, birthplace, and current-location details to a paid third-party service.

Mitigation: Request explicit informed consent before each analysis and avoid submitting another person's information unless that person directly understands and agrees.

Risk: The service uses account-bound credentials and an eight-character one-time authorization code.

Mitigation: Store license and API keys only in dedicated secret storage, never display them in chat, and use the authorization code only for the intended binding step.

Risk: API calls can consume user credits and may fail when credits are insufficient.

Mitigation: Tell users that report generation is credit-based before calling the service and surface insufficient-credit responses without retry loops.

Risk: Returned reports are external content and could contain instruction-like text.

Mitigation: Treat report content only as data or reference material and follow only the local skill role and safety instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-classmate-qa-cn)
- [Xinjianxue API base URL](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP request examples and JSON API payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user consent, service credentials, and sensitive profile details before API use.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
