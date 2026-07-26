## Description: <br>
Generates company intelligence reports from bidding and tendering data, covering company profile, business focus, customers and suppliers, bidding strength, competitors, geographic footprint, and public-risk references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business analysts use this skill to investigate one company or compare two companies through public bidding activity, contract relationships, competitor overlap, and public-risk references. It is intended for company background research and commercial due diligence support, not for project bid/no-bid decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends company queries to a third-party vendor service. <br>
Mitigation: Install only when that vendor data flow is acceptable, and avoid submitting sensitive or confidential company research terms. <br>
Risk: The skill stores a vendor API key and generated company reports on disk. <br>
Mitigation: Prefer a manually supplied API key, restrict access to the local configuration and report directory, and remove generated reports when they are no longer needed. <br>
Risk: Auto-registration uses a device-derived identifier for free-trial deduplication. <br>
Mitigation: Use a preconfigured ZLBX_API_KEY to bypass auto-registration if device fingerprinting is a concern. <br>
Risk: Generated reports may preserve login-bypassing signed links and contact details. <br>
Mitigation: Do not forward HTML or Markdown reports unless the signed links and any contact information are acceptable to share. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/company-intel-qichamao) <br>
- [Workflow guide](artifact/references/workflow.md) <br>
- [API quick reference](artifact/references/api-quick.md) <br>
- [Report template](artifact/references/report-template.md) <br>
- [Automatic registration flow](artifact/references/auto-register.md) <br>
- [Vendor API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool}) <br>
- [Vendor account and recharge portal](https://ai.zhiliaobiaoxun.com/?ch=s116) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, API Calls, Guidance] <br>
**Output Format:** [Markdown report plus optional generated HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include signed vendor links, absolute local report paths, cited public-risk links, and data-boundary disclaimers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
