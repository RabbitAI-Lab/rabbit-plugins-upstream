## Description: <br>
Queries Zhihuiya patent simple bibliographic data by patent ID or publication number and helps present structured metadata such as titles, abstracts, applicants, inventors, classifications, dates, and citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and patent researchers use this skill to retrieve simple bibliographic metadata for known patent identifiers or publication numbers. It is useful for quickly answering patent front-page questions such as inventor, applicant, abstract, classification, filing date, publication date, and citation lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent lookup requests are sent to LinkFox/Zhihuiya. <br>
Mitigation: Avoid submitting sensitive patent identifiers unless the user is comfortable with those requests being sent to the service. <br>
Risk: Full API responses and cached results are saved locally. <br>
Mitigation: Review or clean the local linkfox output and cache directories after sensitive research. <br>
Risk: The skill includes instructions for automatic feedback reporting. <br>
Mitigation: Manually gate or disable feedback reports when they could disclose user intent, sensitive patent details, or evaluation notes. <br>
Risk: The skill can direct the agent toward remote onboarding installation when credentials or credits are missing. <br>
Mitigation: Require explicit user approval and review remote onboarding materials before downloading or installing them. <br>
Risk: Patent queries consume LinkFox/Zhihuiya credits and batch requests can increase cost. <br>
Mitigation: Confirm user intent before large or repeated requests and avoid automatic retries with altered identifiers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-simple-bibliography) <br>
- [Publisher profile](https://clawhub.ai/user/linkfox-ai) <br>
- [Zhihuiya simple bibliography API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with structured patent metadata, JSON API responses, and saved local JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script saves full responses under a local linkfox session data directory, prints small responses inline, summarizes larger responses, and uses a 24-hour local cache by default.] <br>

## Skill Version(s): <br>
1.0.6 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
