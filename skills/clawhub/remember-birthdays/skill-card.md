## Description: <br>
A personal date radar for birthdays and anniversaries that helps an agent greet people on time, avoid duplicate celebration messages, and answer whose special day is coming up with a BlueColumn API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to store, recall, and filter birthdays, anniversaries, memorial days, and greeting-status notes through BlueColumn so timely greetings can be drafted after confirming the date and recipient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores names, special dates, relationship details, privacy preferences, and greeting-status notes with a third-party BlueColumn/Supabase service. <br>
Mitigation: Use the minimum detail needed, avoid storing sensitive third-party information without permission, and review BlueColumn privacy, deletion, and retention terms before relying on it for personal data. <br>
Risk: Stored date or greeting-status notes may be incomplete or stale, which could lead to a missed, duplicate, or inappropriate greeting. <br>
Mitigation: Confirm the person, date, and relationship context before drafting or sending a greeting, and store a completion note after sending. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/remember-birthdays) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BLUECOLUMN_API_KEY and sends requests to the BlueColumn/Supabase API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
