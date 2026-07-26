## Description: <br>
Submits Dataify Builder jobs for Amazon product list collection by keyword and domain, returns the task_id, and helps configure DATAIFY_API_TOKEN. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to confirm Amazon collection parameters, submit a Dataify Builder task, and retrieve the task_id for later result review in Dataify. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use DATAIFY_API_TOKEN from the local environment to submit requests to Dataify. <br>
Mitigation: Use a token intended for Dataify task submission and avoid sharing it in prompts or persisted files. <br>
Risk: Submitted keywords, domains, page counts, and file names are sent to Dataify. <br>
Mitigation: Review the parameter table before submission and avoid sensitive terms or file names. <br>
Risk: Incorrect task parameters can submit the wrong Amazon collection job. <br>
Mitigation: Confirm required and optional values before allowing the Builder request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-amazon-product-list) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown parameter table, shell commands, and JSON task summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns task_id and Dataify dashboard URL after successful submission.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
