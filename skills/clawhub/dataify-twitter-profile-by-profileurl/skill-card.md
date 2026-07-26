## Description: <br>
Prepare Dataify builder requests for the x.com scraper family rooted at twitter_profile_by-profileurl, including tool selection, saved parameter lookup, and generation of a scraperapi.dataify.com/builder curl request that uses DATAIFY_API_TOKEN. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to prepare authenticated Dataify builder curl requests for x.com scraping tools after choosing one supported tool and supplying any required spider parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: DATAIFY_API_TOKEN can grant authenticated access to Dataify's scraper builder if exposed. <br>
Mitigation: Treat the token as a secret, use a credential manager or session-scoped environment variable on shared machines, and avoid pasting token values into shared logs or prompts. <br>
Risk: The generated curl command authenticates to scraperapi.dataify.com and submits the selected spider parameters. <br>
Mitigation: Review the generated command, endpoint, selected tool, and spider_parameters before running it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-twitter-profile-by-profileurl) <br>
- [Dataify publisher profile](https://clawhub.ai/user/dataify-server) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify builder endpoint](https://scraperapi.dataify.com/builder) <br>
- [Tool parameter catalog](references/tool-params.json) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash or PowerShell commands and generated curl requests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated requests include spider_name, spider_id, spider_parameters, spider_errors, file_name, and an Authorization header that references DATAIFY_API_TOKEN.] <br>

## Skill Version(s): <br>
1.2.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
