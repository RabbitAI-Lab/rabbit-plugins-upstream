## Description: <br>
Deploy interactive Telegram Mini App (TWA) answers from OpenClaw as inline Telegram buttons backed by Vercel-hosted HTML pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shlomizaig](https://clawhub.ai/user/shlomizaig) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw agent users use this skill to turn a rich HTML response into a Telegram Mini App link, deploy it to Vercel, and send it through Telegram as an inline button. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML may be published publicly through Vercel and reachable by Telegram users. <br>
Mitigation: Review generated pages for secrets, personal data, internal links, and confidential content before deployment. <br>
Risk: The workflow can change Vercel access settings for the deployed project. <br>
Mitigation: Use a dedicated Vercel project and token where possible, and confirm public access is intended before disabling access protection. <br>
Risk: Telegram bot credentials are required to send the inline button. <br>
Mitigation: Read bot tokens programmatically, avoid displaying them in chat, and rotate the token if it is exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shlomizaig/skills/tg-rich-reply) <br>
- [Telegram Web App SDK](https://telegram.org/js/telegram-web-app.js) <br>
- [Vercel deployments API](https://api.vercel.com/v13/deployments) <br>
- [Vercel files API](https://api.vercel.com/v2/files) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with HTML, JSON, Python, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces deployable single-file HTML guidance plus Vercel and Telegram API command patterns.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
