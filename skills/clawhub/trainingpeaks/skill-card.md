## Description: <br>
Pull real-time training plans, workouts, fitness metrics (CTL/ATL/TSB), and personal records from TrainingPeaks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rubengarciam](https://clawhub.ai/user/rubengarciam) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, coaches, and endurance athletes use this skill to let an agent authenticate with TrainingPeaks, inspect training plans and workouts, retrieve fitness metrics, and review personal records from a command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A copied TrainingPeaks session cookie and cached bearer token can grant access equivalent to the user's TrainingPeaks web session. <br>
Mitigation: Treat the cookie and files in ~/.trainingpeaks as passwords, avoid sharing them in logs or shell history, and keep credential files private. <br>
Risk: Profile, workout, fitness, and personal-record output can include private health, training, and account details. <br>
Mitigation: Review and redact CLI text or JSON before sharing it with an agent, logs, teammates, or support channels. <br>
Risk: The skill uses TrainingPeaks web-session authentication and internal API endpoints, so access can expire or stop working when the session or endpoints change. <br>
Mitigation: Re-authenticate when prompted and validate results against TrainingPeaks before relying on them for coaching or planning decisions. <br>


## Reference(s): <br>
- [ClawHub TrainingPeaks Skill](https://clawhub.ai/rubengarciam/skills/trainingpeaks) <br>
- [TrainingPeaks Web App](https://app.trainingpeaks.com) <br>
- [TrainingPeaks API Base](https://tpapi.trainingpeaks.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Human-readable CLI text or JSON emitted by Python command-line commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include profile, workout, fitness, and personal-record data from the authenticated TrainingPeaks account.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
