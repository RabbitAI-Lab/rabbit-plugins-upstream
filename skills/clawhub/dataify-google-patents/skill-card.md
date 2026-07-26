## Description: <br>
This skill turns Google Patents search requests into confirmed Dataify Scraper API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare Google Patents searches, review the full request parameter table, and call Dataify's Scraper API after explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent search queries, filters, and request metadata are sent to Dataify's Scraper API during live calls. <br>
Mitigation: Install and use the skill only when external Dataify API calls are intended, and review the full confirmation table before approving each request. <br>
Risk: A Dataify API token is required for live requests and could be exposed in an untrusted workspace. <br>
Mitigation: Provide a token only in trusted workspaces; the skill masks token status in confirmation tables and normalizes Bearer tokens before use. <br>


## Reference(s): <br>
- [Dataify Google Patents API Reference](artifact/references/google_patents_api.md) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-patents) <br>
- [Dataify Dashboard](https://dashboard.dataify.com/login?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API Calls, guidance] <br>
**Output Format:** [Markdown confirmation tables, shell commands, and raw Dataify API response bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation before live API calls and hides the full Dataify API token in review tables.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
