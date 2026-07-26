## Description: <br>
亚马逊广告（Amazon Ads）店铺授权与管理技能，提供授权链接生成、已绑定账号和站点查询、profile 发现、令牌刷新与令牌读取能力。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon Ads operators and agent developers use this skill to start the Amazon Ads OAuth flow, discover authorized advertising profiles, select the right marketplace profile, and refresh or retrieve ad access tokens for downstream LinkFox advertising skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles API keys, Amazon Ads authorization URLs, access tokens, and refresh tokens. <br>
Mitigation: Run it only in a trusted local environment, do not disclose saved response files, and verify that token-bearing output remains masked before sharing logs. <br>
Risk: Gateway host environment variables can redirect requests to an untrusted endpoint. <br>
Mitigation: Keep LINKFOX_TOOL_GATEWAY and AMAZON_ADS_BASE_URL unset or set only to trusted LinkFox-controlled hosts. <br>
Risk: Authorization URLs may be copied to the clipboard or cache files and can remain available after the task. <br>
Mitigation: Clear clipboard contents, cached authorization URL files, and generated output folders after completing authorization work. <br>


## Reference(s): <br>
- [Artifact API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads-auth) <br>
- [Amazon Ads Console](https://advertising.amazon.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses saved by the scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Script outputs may include saved response-file paths, summarized JSON for large responses, masked tokens, and authorization URLs.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
