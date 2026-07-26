## Description: <br>
Send X/Twitter posts to Kindle for distraction-free reading. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brianlu365ai](https://clawhub.ai/user/brianlu365ai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to fetch an X/Twitter post or thread from a shared link, format it as a Kindle-readable email, and send it to their Kindle address. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to store a Gmail app password in a plain Markdown file. <br>
Mitigation: Use protected secret storage or a dedicated low-risk sending account instead of writing the app password into TOOLS.md. <br>
Risk: Tweet links are fetched through fxtwitter and the result is sent through the user's SMTP provider. <br>
Mitigation: Confirm the Kindle destination before sending and account for the external services that will process the content. <br>


## Reference(s): <br>
- [X to Kindle on ClawHub](https://clawhub.ai/brianlu365ai/skills/x-kindle) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTML email content and SMTP configuration details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses an X/Twitter post URL, fetched post metadata, SMTP sender settings, and a Kindle email destination.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
