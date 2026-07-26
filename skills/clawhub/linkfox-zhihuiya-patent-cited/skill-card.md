## Description: <br>
This skill helps agents query Zhihuiya (PatSnap) for forward citation counts and citing-patent details for a single patent by publication number or internal patent ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to retrieve factual patent forward-citation metrics and citing-patent details from Zhihuiya (PatSnap). It is intended for single-patent citation lookup and tabular reporting, not patent valuation, legal-status review, or backward-citation research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent queries, API keys, and session metadata are sent to external LinkFox endpoints. <br>
Mitigation: Install and use the skill only when LinkFox is trusted for the relevant patent data and credentials. <br>
Risk: The API gateway can be configured through LINKFOX_TOOL_GATEWAY. <br>
Mitigation: Verify that LINKFOX_TOOL_GATEWAY is unset or points to a trusted HTTPS endpoint before running the helper script. <br>
Risk: Full API responses are written to a local linkfox directory and cache. <br>
Mitigation: Review local storage policies and clean saved response files when patent query data should not persist. <br>
Risk: The security review flagged under-scoped feedback reporting and possible onboarding-support installation. <br>
Mitigation: Review feedback and onboarding behavior before deployment, especially in environments with strict data-sharing or installation controls. <br>


## Reference(s): <br>
- [智慧芽-专利被引用 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-cited) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON parameters, shell commands, and tabular patent-citation summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper script saves full JSON API responses locally, uses a 24-hour cache by default, and summarizes large responses unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
