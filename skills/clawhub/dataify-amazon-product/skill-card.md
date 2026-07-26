## Description: <br>
Use for Dataify Amazon product collection Builder tasks, including Amazon product scraping by ASIN, product URL and zip code, keyword, category URL, or Best Sellers URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to create Dataify Amazon product collection jobs, confirm task parameters, submit the Builder request, and receive a task_id for later review in Dataify. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Dataify API TOKEN and sends Amazon URLs, ASINs, keywords, zip codes, and task settings to Dataify. <br>
Mitigation: Confirm parameters before submission, use DATAIFY_API_TOKEN only for intended Dataify jobs, and do not submit without user approval. <br>


## Reference(s): <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-amazon-product) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown parameter confirmations, shell command examples, and JSON task submission summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Submits task creation requests only; returns task_id and directs users to Dataify for results.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
