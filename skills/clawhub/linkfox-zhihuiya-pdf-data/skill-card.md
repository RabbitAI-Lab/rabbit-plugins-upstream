## Description: <br>
Retrieves patent PDF full-text download links from the Zhihuiya patent database by patent ID or publication number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patent researchers, developers, and agents use this skill to request a single patent PDF link from Zhihuiya using a patent ID or publication number, optionally falling back to a related family patent PDF when the original is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent identifiers and the LinkFox API key are sent to the configured LinkFox gateway. <br>
Mitigation: Use the skill only in controlled environments, review the configured gateway and environment variables, and avoid sensitive patent research unless that network path is acceptable. <br>
Risk: The service consumes paid tokens or credits for each patent PDF result. <br>
Mitigation: Confirm user intent before additional lookups, keep requests to one patent at a time, and rely on the built-in cache when repeating the same query. <br>
Risk: Full API responses are retained locally and may include patent research context. <br>
Mitigation: Review the linkfox session data and cache locations, limit access to the workspace, and clear stored responses when retention is not appropriate. <br>
Risk: The artifact describes automatic feedback reporting for skill behavior and user sentiment. <br>
Mitigation: Do not submit feedback automatically without user consent, especially when feedback could reveal research intent or proprietary context. <br>


## Reference(s): <br>
- [智慧芽 PDF全文查询 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-pdf-data) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, JSON, Files, Markdown] <br>
**Output Format:** [JSON responses saved to local files, with stdout JSON or summaries and Markdown tables for user-facing patent PDF links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Handles one patent per request, may cache responses for 24 hours, and records full API responses under a linkfox session data directory.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
