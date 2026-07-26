## Description: <br>
一键同步 1688 店铺运营数据，并自动整合生成可视化运营数据分析日报。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[howerlin0329](https://clawhub.ai/user/howerlin0329) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
1688 sellers and operations teams use this skill to collect store, traffic, transaction, fulfillment, channel, and keyword data from 1688 seller pages, generate a daily Markdown operations report, and optionally send it to Feishu. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad browser-extension access can expose sensitive 1688 seller analytics. <br>
Mitigation: Restrict the extension to 1688 domains, replace wildcard external extension access with an allowlist, and clear stored data regularly. <br>
Risk: Feishu app credentials and chat IDs can expose reports or enable unintended sends if shared too widely. <br>
Mitigation: Keep credentials in local env files, limit Feishu bot permissions to the required send scope, and rotate credentials if they are exposed. <br>
Risk: Login QR codes and active seller sessions can be exposed in shared chats. <br>
Mitigation: Use the login flow only in trusted chats and keep the browser profile isolated from the user's daily browser profile. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/howerlin0329/skills/1688-alibaba-data-fetcher-1) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Plugin README](artifact/plugin/README.md) <br>
- [Agent guide](artifact/plugin/AGENT_GUIDE.md) <br>
- [Chrome extension manifest](artifact/plugin/manifest.json) <br>
- [Feishu message content API documentation](https://open.feishu.cn/document/server-docs/im-v1/message-content-description/create_json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance, image files] <br>
**Output Format:** [Markdown reports, JSON data files, shell command guidance, configuration values, and QR-code image files during login.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can push Markdown reports to Feishu when FEISHU_APP_ID, FEISHU_APP_SECRET, and FEISHU_CHAT_ID are configured.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
