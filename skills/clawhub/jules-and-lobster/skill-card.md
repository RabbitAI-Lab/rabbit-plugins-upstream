## Description: <br>
Use the Jules REST API (v1alpha) via curl to list sources, create sessions, monitor activities, approve plans, send messages, and retrieve outputs such as PR URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sanjacob99](https://clawhub.ai/user/sanjacob99) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to delegate coding work to Jules through headless API workflows, including creating sessions, monitoring activities, approving plans, sending follow-up messages, and retrieving completed outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crafted prompt or session arguments may cause the shell wrapper to run local Python code. <br>
Mitigation: Use only trusted task text and avoid untrusted arguments until the wrapper passes values as data instead of interpolating them into Python source. <br>
Risk: A leaked Jules API key or overly broad repository access can expose connected coding workflows. <br>
Mitigation: Protect and rotate JULES_API_KEY, and grant Jules access only to repositories intended for this workflow. <br>
Risk: Automated Jules sessions can propose or create code changes that need human review. <br>
Mitigation: Keep plan approval enabled for important repositories and review generated plans and PRs before merging. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sanjacob99/skills/jules-and-lobster) <br>
- [Jules API documentation](https://jules.google/docs/api/reference/overview/) <br>
- [Jules sessions reference](https://jules.google/docs/api/reference/sessions/) <br>
- [Jules activities reference](https://jules.google/docs/api/reference/activities/) <br>
- [Jules sources reference](https://jules.google/docs/api/reference/sources/) <br>
- [Google Developers Jules API](https://developers.google.com/jules/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JULES_API_KEY and access to Jules-connected GitHub repositories.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
