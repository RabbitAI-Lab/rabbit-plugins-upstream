## Description:

Helps agents research WeChat Channels trends, posts, comments, and creators, and retrieve WeChat Official Account article details and engagement statistics through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and content teams use this skill to explore WeChat Channels topics, inspect posts and comments, review creator activity, and check WeChat Official Account article statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the latest npm package can execute code that changed after review with access to the SocialDataX API key.

Mitigation: Review and pin the package version or use a locked installation; run it in a restricted environment with a revocable API key.

Risk: Interrupted pagination can leave comment or post results incomplete.

Mitigation: Report partial results clearly and resume from the appropriate remaining page token rather than restarting or presenting them as complete.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-wechat-channels)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with retrieved data and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries; paginated results may be incomplete if interrupted.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
