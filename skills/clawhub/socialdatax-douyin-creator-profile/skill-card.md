## Description:

用于抖音达人数据、抖音达人信息、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Douyin creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users can look up Douyin creator profiles by account ID, creator identifier, or profile URL. The skill returns available profile details such as account information and audience scale for the agent to summarize.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed through insecure local configuration or version control.

Mitigation: Use a dedicated API key, keep it in the execution environment’s secret configuration, and keep credential settings out of version control.

Risk: API lookups consume account credits.

Mitigation: Check expected credit use and account balance before making requests.

Risk: The external CLI package’s executable behavior has not been verified.

Mitigation: Review and pin the CLI package version before use.

## Reference(s):


## Skill Output:

**Output Type(s):** [API Calls, JSON, Text, Guidance]

**Output Format:** [Structured creator profile data with a concise textual summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile fields vary by availability; profile facts are kept separate from strategic interpretation.]

## Skill Version(s):

0.1.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
