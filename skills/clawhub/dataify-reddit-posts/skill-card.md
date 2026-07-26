## Description: <br>
Submits Reddit post collection jobs through Dataify Builder by post URL, keyword, or subreddit URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure and submit Dataify Reddit post collection tasks, then receive a task ID, status, and Dataify dashboard guidance for viewing results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected Reddit URLs, keywords, subreddit inputs, task settings, and authentication to Dataify. <br>
Mitigation: Install and run it only when submitting Reddit collection tasks to Dataify is intended, and review task settings before submission. <br>
Risk: DATAIFY_API_TOKEN is a credential. <br>
Mitigation: Handle it as a secret and avoid exposing it in prompts, logs, or shared command history. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-reddit-posts) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with optional shell commands and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May submit Reddit URLs, keywords, subreddit inputs, task settings, and a Dataify API token to Dataify when run.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
