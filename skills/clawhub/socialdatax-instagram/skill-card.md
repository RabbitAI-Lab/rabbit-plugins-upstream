## Description:

Provides Instagram content search, post details, comment and reply analysis, creator profiles, and creator post lists through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to research Instagram posts, comments, and creator profiles. It supports content discovery and creator research through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests use an API key, and submitted inputs are sent to SocialDataX.

Mitigation: Protect the API key and use only inputs you are comfortable sharing with SocialDataX.

Risk: Large requests may use API credits.

Mitigation: Review API-credit costs before making large requests.

Risk: The security review covers the bundled instructions but does not verify the external npm package or hosted service.

Mitigation: Prefer a reviewed, fixed CLI version and limit its access to unrelated files and secrets.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub release](https://clawhub.ai/devinchen2014/skills/socialdatax-instagram)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [JSON data and readable text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Instagram research; does not change accounts.]

## Skill Version(s):

0.1.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
