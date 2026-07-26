## Description: <br>
WebScraping.AI helps agents use an OOMOL-connected WebScraping.AI account to extract visible text, fetch rendered HTML, select page areas, and inspect account details through the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate WebScraping.AI through an OOMOL-connected account for page text extraction, rendered HTML retrieval, selected-area HTML retrieval, and account quota checks. It is intended for workflows that need scraping results without exposing raw WebScraping.AI API tokens. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated scraping payloads could target the wrong URL or selector. <br>
Mitigation: Review target URLs, selectors, and JSON payloads before running connector actions. <br>
Risk: Setup commands can initiate authentication, account connection, installation, or billing flows. <br>
Mitigation: Run setup only after an action fails for the matching missing CLI, authentication, connection, or billing condition. <br>
Risk: The skill depends on OOMOL's CLI and the user's connected WebScraping.AI account. <br>
Mitigation: Install and use the skill only when the user is comfortable with that CLI and account connection. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-webscraping-ai) <br>
- [WebScraping.AI homepage](https://webscraping.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, HTML, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands; connector responses are JSON containing extracted text, rendered HTML, selected HTML, or account data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL sign-in, and a connected WebScraping.AI account; setup commands are used only when an action fails due to missing authentication or connection.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
