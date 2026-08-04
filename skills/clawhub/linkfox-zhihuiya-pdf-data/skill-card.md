## Description: <br>
Downloads full-text patent PDF links from the Zhihuiya patent database by patent ID or publication number, with optional family-patent substitution when the original PDF is unavailable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, patent professionals, and developers use this skill to retrieve direct PDF links for one or more known patents from Zhihuiya/PatSnap-style identifiers. It is intended for patent PDF retrieval, not patent discovery, legal-status analysis, claim interpretation, or portfolio analytics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent PDF lookups use a LinkFox/Zhihuiya API key and may involve confidential patent identifiers. <br>
Mitigation: Confirm the user is comfortable sending the requested patent identifiers to the LinkFox/Zhihuiya API before use, especially for confidential patent work. <br>
Risk: Requests consume credits dynamically and bulk requests can incur larger charges. <br>
Mitigation: Warn the user before credit-consuming or bulk requests and avoid repeated automatic retries or exploratory parameter changes without consent. <br>
Risk: The skill saves complete API responses locally and can retain cached copies for reuse. <br>
Mitigation: Review saved response files and local cache contents before using the skill in sensitive workspaces. <br>
Risk: The artifact includes a separate feedback reporting endpoint for reactions, mismatches, or improvement notes. <br>
Mitigation: Do not include secrets or confidential patent details in feedback content, and confirm feedback reporting is acceptable for the workspace. <br>


## Reference(s): <br>
- [Skill release page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-pdf-data) <br>
- [智慧芽 PDF全文查询 API 参考](references/api.md) <br>
- [Zhihuiya PDF API endpoint](https://tool-gateway.linkfox.com/zhihuiya/pdfData) <br>
- [LinkFox Feedback API](https://skill-api.linkfox.com/api/v1/public/feedback) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Files, JSON, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries with patent PDF links, saved JSON API responses, and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes complete API responses under a local linkfox session data directory; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
