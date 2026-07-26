## Description: <br>
Hosted browser automation API for agents. Screenshots, Playwright scripts, workflows - no local Chrome needed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davisdiehl](https://clawhub.ai/user/davisdiehl) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agent users use Riddle to run hosted browser automation, capture screenshots, execute Playwright workflows, and automate authenticated web sessions without running local Chrome. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated browser automation can expose cookies, headers, screenshots, and captured traffic. <br>
Mitigation: Use test or least-privilege accounts, avoid production secrets, and pass only the authentication data needed for the task. <br>
Risk: HAR capture can include sensitive request and response data. <br>
Mitigation: Leave HAR capture disabled unless it is required, and redact or delete saved traffic captures after use. <br>
Risk: Saved screenshots and browser artifacts can retain sensitive page content. <br>
Mitigation: Review captured files before sharing them and regularly delete screenshots or other saved artifacts that are no longer needed. <br>


## Reference(s): <br>
- [Riddle Website](https://riddledc.com) <br>
- [Riddle Docs](https://riddledc.com/docs) <br>
- [Riddle Plugin Source](https://github.com/riddledc/integrations) <br>
- [Riddle Skill on ClawHub](https://clawhub.ai/davisdiehl/skills/riddle) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown text with shell commands, Playwright examples, and file paths to saved browser artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Screenshots are returned as saved file paths; optional HAR capture can include network traffic.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
