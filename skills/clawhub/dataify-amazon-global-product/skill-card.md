## Description: <br>
Dataify Amazon Global Product submits Dataify Builder jobs for Amazon product collection by product URL, category URL, keyword, or keyword and brand, then returns the task ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure and submit Amazon product collection jobs to Dataify Builder and receive a task_id for tracking results in Dataify. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses DATAIFY_API_TOKEN to submit requests to Dataify. <br>
Mitigation: Treat the token as a secret, avoid persistent storage on shared machines, and do not submit Builder requests without a token. <br>
Risk: The skill can create Dataify collection jobs in the user's account. <br>
Mitigation: Review the collection mode, URL or keyword inputs, limits, filters, and file name before submitting the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-amazon-global-product) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown parameter confirmation and, when using the script, JSON with task_id and submitted parameters.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN and stops after successful Builder task submission.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
