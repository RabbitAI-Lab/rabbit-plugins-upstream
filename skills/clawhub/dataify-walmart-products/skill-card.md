## Description: <br>
Submit Dataify Walmart Product Information Builder tasks for product URL, category URL, SKU, or keyword collection modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to create Dataify Walmart product collection jobs, validate mode-specific parameters, and receive the submitted task ID and status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read DATAIFY_API_TOKEN from the local environment and use it to submit Dataify Builder requests. <br>
Mitigation: Install only when Dataify task creation is intended, review token use before running, and remove or rotate DATAIFY_API_TOKEN if future automatic use is not desired. <br>
Risk: Broad invocation could submit Walmart collection jobs when the user intent or collection mode is unclear. <br>
Mitigation: Confirm the collection mode and mode-specific parameters before submitting a Builder request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-walmart-products) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with optional shell commands and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns task_id, status, selected mode, spider_id, parameters, file name, dashboard URL, and a short success message after submission.] <br>

## Skill Version(s): <br>
1.2.0 (source: evidence release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
