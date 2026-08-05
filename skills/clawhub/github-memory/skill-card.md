## Description: <br>
Github Memory helps agents store, recall, and search GitHub issue and pull request context using BlueColumn persistent memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents that track repositories use this skill to remember, retrieve, and search issue and pull request context across interactions. It supports recall-first workflows and follow-up storage of interaction summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GitHub issue, pull request, or repository context may be sent to and persisted in an external BlueColumn memory service. <br>
Mitigation: Use only with repositories whose content is approved for BlueColumn storage, and avoid storing secrets, credentials, confidential issue details, or sensitive operational context unless the organization has approved the service and retention model. <br>
Risk: The skill requires a live BlueColumn API key for memory storage and recall. <br>
Mitigation: Store the API key only in the platform secret store or an approved tool configuration, and review the skill before installing it in private or company repositories. <br>


## Reference(s): <br>
- [BlueColumn API Docs](https://bluecolumn.ai/docs) <br>
- [ClawHub Skill Page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/github-memory) <br>
- [Publisher Profile](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends selected GitHub context to BlueColumn for persistent memory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
