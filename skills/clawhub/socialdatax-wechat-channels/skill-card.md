## Description:

This skill helps agents retrieve read-only WeChat Channels and WeChat Official Account article data through SocialDataX for hot lists, content research, post details, comments, creator profiles, and creator content lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SocialDataX for WeChat Channels trend, content, comment, creator, and article data from an agent workflow. It is intended for read-only research and operational data lookup using the user's SocialDataX API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls may consume SocialDataX account credits and send requested WeChat keywords, URLs, IDs, and attribution parameters to SocialDataX.

Mitigation: Use the intended SocialDataX account key, check request parameters before running commands, and stop retrying when insufficient balance is reported.

Risk: The direct CLI path depends on npm/npx execution of the SocialDataX package.

Mitigation: Install only when comfortable using SocialDataX through npm/npx and providing SOCIALDATAX_API_KEY in the runtime environment.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-wechat-channels)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and SocialDataX data responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and Node.js/npm for direct CLI use.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
