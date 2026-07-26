## Description: <br>
Analyzes LinkedIn users and companies through KeyAPI REST workflows for professional profiles, contact information, work history, company profiles, employees, jobs, posts, and related analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xyzzero](https://clawhub.ai/user/xyzzero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, sales and recruiting analysts, and other external users use this skill to turn LinkedIn research goals into documented KeyAPI calls and concise reports for profiles, companies, jobs, posts, and contact-data workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retrieve LinkedIn profile and personal contact data. <br>
Mitigation: Use contact-info features only for authorized, lawful, minimum-necessary purposes and confirm scope before broad reports or enrichment. <br>
Risk: The auth helper can persist a KeyAPI token in a shell profile. <br>
Mitigation: Prefer interactive or temporary environment-variable setup, avoid the --token command-line option in shared shells, and avoid syncing shell profiles that contain secrets. <br>
Risk: Live API calls may consume quota or repeat the same request when rerun. <br>
Mitigation: Resolve endpoint docs first, confirm scope for multi-call reports, and use pagination stop conditions or saved output only when needed. <br>


## Reference(s): <br>
- [KeyAPI LinkedIn docs index](https://docs.keyapi.ai/llms.txt) <br>
- [KeyAPI LinkedIn documentation](https://docs.keyapi.ai/en/linkedin/) <br>
- [KeyAPI bearer authentication](https://docs.keyapi.ai/overview/authentication#bearer-authentication) <br>
- [Global Rules](references/global-rules.md) <br>
- [Scenario Cards](references/scenarios.md) <br>
- [Routing Policy](references/routing-policy.md) <br>
- [LinkedIn Rules](references/linkedin-rules.md) <br>
- [LinkedIn User Module Rules](references/linkedin-user-rules.md) <br>
- [LinkedIn Company Module Rules](references/linkedin-company-rules.md) <br>
- [LinkedIn Jobs Module Rules](references/linkedin-jobs-rules.md) <br>
- [Setup And Auth](references/setup-and-auth.md) <br>
- [Search people endpoint](https://docs.keyapi.ai/en/linkedin/search_people.md) <br>
- [Get user profile endpoint](https://docs.keyapi.ai/en/linkedin/get_user_profile.md) <br>
- [Get user contact endpoint](https://docs.keyapi.ai/en/linkedin/get_user_contact.md) <br>
- [Get company profile endpoint](https://docs.keyapi.ai/en/linkedin/get_company_profile.md) <br>
- [Get company jobs endpoint](https://docs.keyapi.ai/en/linkedin/get_company_jobs.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Shell commands, Configuration instructions, Files] <br>
**Output Format:** [Markdown summaries with optional JSON API results and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save complete API responses to a requested JSON file; large live responses may be previewed by default.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
