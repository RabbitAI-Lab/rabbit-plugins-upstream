## Description: <br>
ScraperAPI (scraperapi.com). Use this skill for ANY ScraperAPI request - reading, creating, and updating data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to check ScraperAPI account usage, scrape public URLs, and send POST or PUT requests through an OOMOL-connected ScraperAPI account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording may cause the skill to be used for many ScraperAPI-related requests, including requests that submit URLs or use account credentials. <br>
Mitigation: Review the selected ScraperAPI action before execution and confirm payload details before any action that submits URLs or uses credentialed access. <br>
Risk: The submit_url action can send POST or PUT requests to public URLs through ScraperAPI. <br>
Mitigation: Confirm the exact target URL, HTTP method, payload, and expected effect with the user before running submit_url. <br>


## Reference(s): <br>
- [ClawHub ScraperAPI skill page](https://clawhub.ai/oomol/skills/oo-scraperapi) <br>
- [ScraperAPI homepage](https://www.scraperapi.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses oo CLI connector commands; ScraperAPI responses are returned as JSON with data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
