## Description: <br>
Collect Google Shopping product information by keyword through the Dataify Scraper API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to preview parameters and create Dataify Google Shopping keyword collection tasks after confirming the exact request values and API token handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports that trigger text also covers unrelated Instagram Reel collection requests. <br>
Mitigation: Use the skill only for Google Shopping keyword collection and avoid invoking it for Instagram Reel scraping. <br>
Risk: The skill handles a Dataify API token, and credential-storage guidance was assessed as under-scoped. <br>
Mitigation: Treat DATAIFY_API_TOKEN as a secret; prefer a secret manager or temporary environment variable and avoid shared or synced shell startup files unless the exposure risk is understood. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-shopping-keywords) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance, text] <br>
**Output Format:** [Markdown guidance with confirmation tables and Python command examples; helper scripts emit Markdown tables or JSON/API response text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an explicit Dataify API token or DATAIFY_API_TOKEN environment variable before creating tasks.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
