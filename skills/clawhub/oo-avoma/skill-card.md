## Description: <br>
Use this skill to search and read Avoma meeting, recording, transcription, user, and insight data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query Avoma meeting, recording, transcription, user, and meeting-insight data through their connected OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Avoma meeting transcripts, recordings, and related meeting data can contain sensitive information. <br>
Mitigation: Limit requests to the specific meeting IDs, date ranges, users, and filters needed for the task. <br>
Risk: The skill runs Avoma queries through a connected OOMOL account. <br>
Mitigation: Install and use it only when the account owner is comfortable allowing the agent to query Avoma data through that connection. <br>


## Reference(s): <br>
- [Avoma homepage](https://www.avoma.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub Avoma skill page](https://clawhub.ai/oomol/skills/oo-avoma) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs guide an agent to inspect the live connector schema before running Avoma read actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
