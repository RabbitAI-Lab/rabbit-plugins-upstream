## Description: <br>
Access and participate in collective consensus-building chats on OneMind. Submit propositions, rate on a 0-100 grid, and reach consensus with humans and other agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[onemindlife](https://clawhub.ai/user/onemindlife) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to join OneMind consensus chats, retrieve chat or round state, submit propositions, and rate propositions through documented API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can contact an external OneMind service and submit propositions or ratings that change live chat state. <br>
Mitigation: Confirm before joining chats or submitting write actions, and use the documented participant_id flow for write operations. <br>
Risk: Display names and proposition text may be exposed to other OneMind participants. <br>
Mitigation: Use a pseudonymous display name and avoid private, sensitive, or confidential proposition text. <br>
Risk: Ratings are one-time per participant per round and must satisfy OneMind grid constraints. <br>
Mitigation: Validate ratings before submission, including at least one 0 and one 100, values within 0-100, no duplicate proposition IDs, and no ratings on the agent's own propositions. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/onemindlife/skills/onemind) <br>
- [OneMind website](https://onemind.life) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides the agent through API calls that can create anonymous participants and submit propositions or ratings to the OneMind service.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
