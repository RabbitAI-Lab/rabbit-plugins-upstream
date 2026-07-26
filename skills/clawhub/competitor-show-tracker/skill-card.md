## Description: <br>
Rank upcoming trade shows by how many listed competitors match Lensmor exhibitor records, then summarize event concentration and follow-up actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[weilun88313](https://clawhub.ai/user/weilun88313) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
B2B go-to-market, marketing, and event planning teams use this skill to compare competitor show circuits and prioritize upcoming trade shows by competitor concentration. It is intended for multi-company competitive intelligence using Lensmor exhibitor data, not as independent proof of attendance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Successful Lensmor searches may spend credits, create API activity records, and update the API-key owner's HubSpot last_search_date. <br>
Mitigation: Ask the user to approve the maximum first-page credit cost and activity logging before making live API calls. <br>
Risk: Shared or third-party Lensmor API keys can create costs and activity records for an account owner who did not approve the run. <br>
Mitigation: Use only an API key the user is authorized to operate, and do not proceed when authorization for those side effects is unclear. <br>
Risk: Lensmor exhibitor matches are database records and may include missing, incomplete, or subsidiary-level matches. <br>
Mitigation: Describe results as matches in Lensmor exhibitor records, report gaps and incomplete pages, and avoid presenting matches as independently verified attendance. <br>


## Reference(s): <br>
- [Competitor Show Tracker on ClawHub](https://clawhub.ai/weilun88313/skills/competitor-show-tracker) <br>
- [Lensmor API documentation](https://api.lensmor.com/?utm_source=github&utm_medium=skill&utm_campaign=competitor-show-tracker) <br>
- [Fictional industrial automation example](examples/industrial-automation-show-circuit.md) <br>
- [Lensmor](https://www.lensmor.com/?utm_source=github&utm_medium=skill&utm_campaign=competitor-show-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Analysis, API Calls, Shell commands, Guidance] <br>
**Output Format:** [Markdown with ranked tables, event detail sections, insights, and follow-up suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LENSMOR_API_KEY; asks for approval before paid searches or activity logging.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
