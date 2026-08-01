## Description: <br>
This skill helps an agent answer questions and perform confirm-gated actions for a user's own Kia vehicle through a Kia Access / Kia Owners account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent check Kia vehicle status, location, EV charge state, and charge targets, and to prepare or execute explicitly confirmed vehicle commands such as climate, charging, lock, and unlock actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Kia account credentials and can maintain a persistent vehicle session. <br>
Mitigation: Install only if the publisher and npm package are trusted, protect local credential and session storage, and never expose passwords, session IDs, or refresh tokens in chat. <br>
Risk: Confirmed commands can affect a real vehicle, including climate, charging, and door lock state. <br>
Mitigation: Require explicit user confirmation for every command, keep KIA_WRITE_MODE at none or comfort unless lock and unlock controls are intended, and re-read vehicle status when command completion matters. <br>
Risk: Cached vehicle reads and accepted commands may not reflect current physical state. <br>
Mitigation: Use refresh-and-read workflows when freshness matters and communicate whether a result is a dry run, accepted command, confirmed state, or timed-out confirmation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess) <br>
- [Publisher profile](https://clawhub.ai/user/chrischall) <br>
- [npm package](https://www.npmjs.com/package/kiaaccess-mcp) <br>
- [Project repository](https://github.com/chrischall/kiaaccess-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline JSON and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include vehicle status summaries, setup guidance, dry-run command previews, and cautions for confirmed vehicle actions.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
