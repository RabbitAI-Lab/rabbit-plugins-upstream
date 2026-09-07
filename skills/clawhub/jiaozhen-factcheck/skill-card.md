## Description:

Fact-checking skill that uses Tencent News Jiaozhen CLI capabilities to assess the truthfulness, accuracy, and credibility of user-provided claims, events, common-knowledge questions, images, or suspicious information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencentnewsteam](https://clawhub.ai/user/tencentnewsteam)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to check whether claims, news items, rumors, screenshots, or other user-provided factual assertions are true, false, or uncertain. The skill guides the agent through local CLI readiness checks and returns the Tencent Jiaozhen CLI's Markdown verification result as the response body.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the skill asks agents or users to install or update a local Tencent CLI through remote shell scripts without integrity verification.

Mitigation: Review the skill before installation, prefer manually downloading and verifying installers, and avoid piping remote setup scripts directly into a shell in sensitive environments.

Risk: The skill depends on a locally configured Tencent News API key.

Mitigation: Have the user enter the API key locally, do not ask the user to share the real key in chat, and avoid logging or echoing key values in responses or reports.

Risk: Fact-checking output depends on the availability, behavior, and quota limits of the Tencent CLI service.

Mitigation: When the CLI fails or quota is exhausted, report the CLI condition and do not substitute independent web research as if it were the same verification result.

## Reference(s):

- [tencent-news-cli Manual Installation Guide](references/installation-guide.md)
- [tencent-news-cli API Key Configuration Guide](references/env-setup-guide.md)
- [tencent-news-cli Manual Update Guide](references/update-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/tencentnewsteam/skills/jiaozhen-factcheck)
- [API Key Request Page](https://news.qq.com/exchange?scene=appkey)
- [Jiaozhen AI Web Entry](https://view.inews.qq.com/ai/agent/UTR2025041800262600?no-redirect=1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown fact-check results with setup or troubleshooting guidance when the local CLI or API key is not ready]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill preserves the CLI's returned Markdown structure and source links, and uses wrapper scripts for CLI state checks and command execution.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
