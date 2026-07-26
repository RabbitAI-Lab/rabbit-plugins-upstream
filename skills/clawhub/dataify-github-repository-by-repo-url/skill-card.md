## Description: <br>
Prepares Dataify builder requests for the github.com scraper family rooted at github_repository_by-repo-url, including tool selection, saved parameter lookup, and a curl request that uses DATAIFY_API_TOKEN. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to prepare Dataify builder curl requests for GitHub repository scraping workflows after selecting one supported scraper tool and supplying any required values. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated curl command sends selected scraper parameters to Dataify and uses a bearer token from the local environment. <br>
Mitigation: Keep DATAIFY_API_TOKEN private, review values.json before generating requests, and run the curl command only when the selected parameters are intended for Dataify. <br>


## Reference(s): <br>
- [Dataify skill page](https://clawhub.ai/dataify-server/skills/dataify-github-repository-by-repo-url) <br>
- [Saved Dataify tool parameter catalog](references/tool-params.json) <br>
- [Dataify builder endpoint](https://scraperapi.dataify.com/builder) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with a curl command and setup instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces user-directed requests for Dataify's builder API and relies on DATAIFY_API_TOKEN from the user's environment.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
