## Description: <br>
Discover curated SaaS and AI-agent tools via the Tulimoa directory. Search by topic, category, pricing, MCP support, or EU hosting, pull full detail on any tool, and submit or edit your own listings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[florianbaraz](https://clawhub.ai/user/florianbaraz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill to search, compare, and retrieve details for curated SaaS and AI-agent tools in the Tulimoa directory. Authenticated Tulimoa users can submit or edit their own listings for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms and listing details are sent to Tulimoa's remote MCP service. <br>
Mitigation: Treat queries and submitted listing data as information shared with Tulimoa; avoid sending confidential data unless approved. <br>
Risk: Authorized write tools can create or edit directory listings that may later become public after review. <br>
Mitigation: Only grant Tulimoa OAuth write access when the user intends to submit or edit a listing. <br>


## Reference(s): <br>
- [Tulimoa homepage](https://tulimoa.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Guidance] <br>
**Output Format:** [Markdown or structured MCP tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read operations are anonymous; write operations require Tulimoa OAuth authorization.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
