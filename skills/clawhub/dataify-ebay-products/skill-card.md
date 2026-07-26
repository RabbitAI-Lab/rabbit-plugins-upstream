## Description: <br>
Dataify eBay Products helps agents submit Dataify Builder jobs for eBay product collection by product URL, category URL, keyword, or store URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure and submit eBay product collection tasks through Dataify, then receive the resulting task ID, status, parameters, and dashboard link. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit eBay product collection jobs to Dataify using network access. <br>
Mitigation: Install and invoke it only when the user intends to create Dataify eBay collection tasks, and confirm the collection mode and parameters before submission. <br>
Risk: The skill uses a Dataify API TOKEN and may rely on a saved DATAIFY_API_TOKEN for future tasks. <br>
Mitigation: Review prompts before use and save DATAIFY_API_TOKEN only after explicit user confirmation in an environment where future Dataify task use is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-ebay-products) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON task-submission summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful submissions return task_id, status, parameters, file_name, and a Dataify dashboard URL.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
