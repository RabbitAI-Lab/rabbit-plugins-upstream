## Description: <br>
This skill turns a user's Google AI Mode search request into a confirmed Dataify Scraper API call. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn Google AI Mode search requests into confirmed Dataify Scraper API calls. It helps agents collect search parameters, request confirmation, run the bundled script, and return the API response body directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and request parameters are sent to Dataify, so sensitive search terms may leave the user's environment. <br>
Mitigation: Use the skill only when Dataify is the intended search provider, and avoid submitting sensitive queries unless that data sharing is acceptable. <br>
Risk: The skill requires a Dataify API token and supports passing a token as an argument, which can expose credentials in chat or shell history. <br>
Mitigation: Set DATAIFY_API_TOKEN through a trusted secret mechanism and avoid pasting tokens into chat or command-line examples. <br>
Risk: The skill returns the raw API response body directly, so returned content may be unreviewed or unexpected. <br>
Mitigation: Review returned content before using it in decisions, publications, or follow-on automated actions. <br>


## Reference(s): <br>
- [Dataify Google AI Mode API Reference](references/google_ai_mode_api.md) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-ai-mode) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown parameter tables, shell commands, and raw API response bodies.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill asks for confirmation before real API calls and returns the Dataify response body without summarizing or reshaping it.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
