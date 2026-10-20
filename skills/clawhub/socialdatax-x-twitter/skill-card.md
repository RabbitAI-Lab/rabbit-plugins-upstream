## Description:

Supports read-only X/Twitter research across post search and details, discussion replies, creator profiles, and creator posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can research X/Twitter posts, discussions, creator profiles, posts, and replies through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, identifiers, URLs, and pasted share text are sent to SocialDataX and requests may consume API credits.

Mitigation: Avoid confidential inputs and monitor API credit use.

Risk: The API key and package dependency require care; the referenced npm release was not independently verified.

Mitigation: Protect the API key, review and pin the package version, and limit its access to unrelated files and secrets.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-x-twitter)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Pretty-printed JSON data from X/Twitter search, post, discussion, and creator queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research results; available data depends on the query and service response.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
