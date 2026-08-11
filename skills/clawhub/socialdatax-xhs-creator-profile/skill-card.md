## Description:

Looks up public Xiaohongshu / XHS / RedNote creator profile data, including account basics, audience scale, and profile fields, through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve read-only Xiaohongshu / XHS / RedNote creator profile information from SocialDataX by creator ID, profile URL, short link, or profile share text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SocialDataX API key with an npm-based CLI to query creator profile data.

Mitigation: Install and run it only when comfortable providing SOCIALDATAX_API_KEY to the SocialDataX CLI, and keep the key in the runtime environment rather than in skill files.

Risk: Returned creator profile fields are third-party data and may be incomplete, outdated, or unsuitable for unsupported conclusions.

Mitigation: Report profile facts separately from strategic interpretation and verify important claims against appropriate sources before acting on them.

Risk: Insufficient-balance or recharge flows may include payment or account-management URLs.

Mitigation: Review any recharge URL or API-key setup flow before entering payment or account information, and use the official SocialDataX API access page from the skill metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-creator-profile)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile facts should be separated from strategic interpretation.]

## Skill Version(s):

0.1.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
