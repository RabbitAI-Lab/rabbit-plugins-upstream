## Description: <br>
Use when the user wants to check restaurant availability or make, change, or cancel a table reservation at a restaurant that books through easyTable (a book.easytable.com/book/?id=<id> widget). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to inspect availability and manage reservations for restaurants that expose an easyTable booking widget. It supports listing booking areas, dates, and times, then previewing and confirming creation, modification, or cancellation of bookings through the user's browser session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a paired browser bridge to act through the user's own browser session. <br>
Mitigation: Review the fetchproxy extension before installing and use the skill only with easyTable booking tabs intentionally opened for the reservation task. <br>
Risk: Create, modify, and cancel actions can change restaurant reservations. <br>
Mitigation: Check the dry-run preview and provide explicit confirmation only when the proposed reservation change or cancellation is correct. <br>


## Reference(s): <br>
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with tool-call guidance and concise status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Write actions are dry-run previewed and require explicit confirmation before reservation changes are applied.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
