## Description:

SocialDataX Douyin helps agents look up Douyin hot searches, works, comments, replies, creator profiles, creator posts, and creator series for social data research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public Douyin search, content, comment, reply, and creator data through SocialDataX for content research and social media analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin search terms, links, IDs, and API-key-authenticated requests are sent to SocialDataX.

Mitigation: Use the skill only when the user is comfortable sharing those request details with SocialDataX, and avoid sending sensitive or private inputs.

Risk: The direct CLI examples use a floating socialdatax-skills@latest package, so package behavior can change over time.

Mitigation: Review package behavior before deployment and consider pinning a package version in controlled environments.

Risk: The skill depends on SOCIALDATAX_API_KEY at runtime.

Mitigation: Store the API key in the environment, do not place it in skill files, and rotate it if it may have been exposed.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON responses from SocialDataX tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires node, npm, and SOCIALDATAX_API_KEY; uses SocialDataX-authenticated service calls for read-only Douyin lookups.]

## Skill Version(s):

0.1.16 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
