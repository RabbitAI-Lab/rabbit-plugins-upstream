## Description: <br>
Prepare Dataify builder requests for TikTok scraper tools by helping users select a Dataify tool, collect parameter values, and generate a curl request using DATAIFY_API_TOKEN. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users who use Dataify can generate builder requests for TikTok comment, shop, post-list, and profile scraping tools after choosing a tool and supplying parameter values. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated curl request sends selected URLs and parameters to Dataify. <br>
Mitigation: Review the generated command before execution and use it only for the intended Dataify TikTok scraping workflow. <br>
Risk: DATAIFY_API_TOKEN exposure could grant access to the Dataify account. <br>
Mitigation: Treat DATAIFY_API_TOKEN like a password; prefer a session-scoped environment variable or secret manager and avoid storing it in shared shell profile files. <br>


## Reference(s): <br>
- [Tool parameter catalog](artifact/references/tool-params.json) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify builder endpoint](https://scraperapi.dataify.com/builder) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-tiktok-comment-by-url) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with bash or PowerShell command blocks and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns a Dataify builder curl command and may provide DATAIFY_API_TOKEN setup guidance.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
