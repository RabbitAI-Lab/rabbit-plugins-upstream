## Description: <br>
Helps an agent store and search podcast episodes, timestamps, notes, quotes, and takeaways using BlueColumn's hosted API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent record podcast listening notes, preserve timestamps and quotes, search past episodes for relevant ideas, and queue episodes or clips for later follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Podcast notes, timestamps, summaries, and searches are sent to BlueColumn's hosted service. <br>
Mitigation: Install only when this data sharing is acceptable, and avoid submitting confidential or regulated content unless approved by the organization. <br>
Risk: The skill requires a BlueColumn API key for operations. <br>
Mitigation: Treat BLUECOLUMN_API_KEY like a password and avoid exposing it in logs, shared prompts, or committed files. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/remember-podcasts) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BLUECOLUMN_API_KEY for API calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
