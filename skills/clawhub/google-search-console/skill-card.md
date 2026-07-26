## Description: <br>
Google Search Console API integration with managed OAuth for querying search analytics, managing sitemaps, and monitoring site performance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to access Google Search Console data through Maton-managed OAuth, including search analytics, site listings, URL inspection-oriented workflows, and sitemap management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Maton API key can grant access through the managed Google Search Console OAuth proxy if exposed. <br>
Mitigation: Keep MATON_API_KEY private, avoid sharing logs or command output that contain it, and rotate the key if exposure is suspected. <br>
Risk: Requests may target the wrong Google Search Console connection when multiple active connections exist. <br>
Mitigation: Set the Maton-Connection header to the intended connection ID before querying or changing account data. <br>
Risk: Sitemap create, update, or delete calls can change Search Console state. <br>
Mitigation: Review the target site URL, sitemap path, and intended effect before approving any write operation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-search-console) <br>
- [Google Search Console API Reference](https://developers.google.com/webmaster-tools/v1/api_reference_index) <br>
- [Sites: list](https://developers.google.com/webmaster-tools/v1/sites/list) <br>
- [Search Analytics: query](https://developers.google.com/webmaster-tools/v1/searchanalytics/query) <br>
- [Sitemaps](https://developers.google.com/webmaster-tools/v1/sitemaps) <br>
- [Maton](https://maton.ai) <br>
- [Maton settings](https://maton.ai/settings) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, API Calls, Configuration] <br>
**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and an active Google Search Console OAuth connection.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
