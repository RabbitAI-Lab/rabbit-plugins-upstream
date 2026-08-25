## Description:

A unified Tradebee Website Builder Open API skill for explicit operations on blogs, FAQs, custom pages, news, news groups, website navigation, products, inquiries, analytics, and tenant HTML rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tradebee](https://clawhub.ai/user/tradebee)

### License/Terms of Use:

MIT-0

## Use Case:

External site operators and digital marketing teams use this skill to manage Tradebee Website Builder content, navigation, inquiries, visitor activity, keyword rankings, and tenant HTML rules through explicit read, create, update, and delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete Tradebee website content and navigation.

Mitigation: Install only for authorized Tradebee operators and review every create, update, or delete confirmation before execution.

Risk: Update backups and inquiry or visitor results may contain business or personal data.

Mitigation: Keep BEE_API_KEY protected, request only the fields needed for the task, and periodically delete or secure local backup files.

## Reference(s):

- [Tradebee Open API homepage](https://open.tradew.com)
- [ClawHub skill page](https://clawhub.ai/tradebee/skills/tradebee)
- [Publisher profile](https://clawhub.ai/user/tradebee)

## Skill Output:

**Output Type(s):** [JSON, Files, Guidance]

**Output Format:** [JSON API responses, local JSON backup files for update actions, and concise status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Update actions return backup metadata and may write local backup files; HTML content generation must follow tenant rules returned by rule-get.]

## Skill Version(s):

26.8.24 (source: server release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
