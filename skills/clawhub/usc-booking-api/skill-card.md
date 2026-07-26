## Description: <br>
Scan Urban Sports Club venues, list courses with booking links, and book or cancel courses using USC login credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[niklaspriddat](https://clawhub.ai/user/niklaspriddat) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Individuals or agents assisting Urban Sports Club users can scan configured venues for available classes, list upcoming bookings, and run user-invoked booking or cancellation commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores Urban Sports Club credentials in a local credentials.json file for login-based actions. <br>
Mitigation: Keep credentials.json private, avoid committing or sharing it, and use the file only on trusted local systems. <br>
Risk: Booking and cancellation commands make live changes to the user's Urban Sports Club account. <br>
Mitigation: Double-check class IDs before running --book or --cancel, and reserve those commands for explicit user intent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/niklaspriddat/skills/usc-booking-api) <br>
- [Publisher profile](https://clawhub.ai/user/niklaspriddat) <br>
- [Urban Sports Club](https://urbansportsclub.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands can emit class or booking lists as JSON; booking and cancellation commands act on the user's live Urban Sports Club account.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
