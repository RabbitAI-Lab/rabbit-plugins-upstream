## Description: <br>
Pair OpenClaw with Superlore to create or upload private podcast episodes and use saved Sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adamjurgens](https://clawhub.ai/user/adamjurgens) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to pair OpenClaw with Superlore, create private podcast episodes from prompts, upload authorized audio, and use saved Superlore Sources when granted. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pairing grants OpenClaw a Superlore agent credential for approved scopes. <br>
Mitigation: Approve only the minimum scopes needed, and reconnect instead of retrying indefinitely after authorization failure. <br>
Risk: Listen URLs returned by the helper are private and may expose generated episode access if shared. <br>
Mitigation: Treat listen URLs as private and avoid printing or storing them outside the active workflow. <br>
Risk: Uploads and recurring schedules can create or publish podcast content beyond a one-time prompt. <br>
Mitigation: Authorize uploads and recurring schedules only when the user explicitly requests them. <br>


## Reference(s): <br>
- [Superlore OpenClaw integration](https://superlore.ai/integrations/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON helper output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return private listen URLs, generation status, connection test results, and saved-source context.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
