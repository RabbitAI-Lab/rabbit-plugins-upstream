## Description: <br>
Helps agents create bid-data-informed company background-check reports covering business profile, customers and suppliers, bidding strength, competitors, public-risk signals, and optional two-company comparisons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business users and agents use this skill to assess a named company before cooperation, supplier review, customer verification, competitor research, or light due diligence. It produces a sourced narrative report and a shareable HTML report from public bidding data plus limited public web risk checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill calls a third-party company-intelligence API and may consume account credits. <br>
Mitigation: Tell users the expected credit cost before running the report and only use auto-registration after explicit user consent. <br>
Risk: The skill can save an API key locally and generate shareable reports or auto-login links containing sensitive access tokens. <br>
Mitigation: Treat API keys, generated report links, auto-login links, and saved report paths as sensitive, and avoid exposing credentials in conversation. <br>
Risk: Company background reports and public-risk sections can affect real-world business judgments. <br>
Mitigation: Use sourced factual statements, include links for public-risk claims, avoid unsupported conclusions, and state data boundaries and gaps. <br>
Risk: Contact details returned by the service may be privacy-sensitive or masked for trial accounts. <br>
Mitigation: Show contact details only as returned by the API, do not enrich masked phone numbers from other sources, and avoid bulk contact exports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/company-background-check) <br>
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun) <br>
- [Workflow guide](references/workflow.md) <br>
- [API quick reference](references/api-quick.md) <br>
- [Report template](references/report-template.md) <br>
- [Auto-registration flow](references/auto-register.md) <br>
- [Zhiliaobiaoxun company-intelligence API](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool}) <br>
- [Zhiliaobiaoxun business-intelligence portal](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown report in chat plus optional self-contained HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or gated auto-registration; reports may include signed share links and sourced public-risk references.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
