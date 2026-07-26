## Description: <br>
Jielong CLI helps agents manage Jielong activity workflows through local jielong commands, including creating, viewing, editing, deleting, signing up for, and managing activity records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liu-tao-hash](https://clawhub.ai/user/liu-tao-hash) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and activity organizers use this skill to operate Jielong activities from an agent, including creating signup or check-in activities, reviewing participants, modifying activity details, and managing activity state or records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may install or update the jielong CLI globally on the user's machine. <br>
Mitigation: Require explicit user confirmation before global installs or updates and review the package source before deployment. <br>
Risk: Login and account checks can expose account identifiers such as nickname, phone number, user ID, or OpenID. <br>
Mitigation: Review identity output before sharing it and avoid running the skill on shared machines or in shared logs. <br>
Risk: Activity, signup, deletion, clearing, and status commands can make real changes to Jielong data. <br>
Mitigation: Confirm the target activity, requested operation, and destructive actions before execution. <br>
Risk: Activity IDs, activity keys, and signup/order identifiers may enable later activity changes or record management. <br>
Mitigation: Treat these identifiers as sensitive and avoid persisting or disclosing them beyond the task context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liu-tao-hash/skills/jielong-cli) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/liu-tao-hash) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with CLI command snippets and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the local jielong CLI and an authenticated Jielong account.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
