## Description: <br>
Control Samsung TVs via SmartThings (OAuth app + device control). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[regenrek](https://clawhub.ai/user/regenrek) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to set up SmartThings OAuth credentials, identify Samsung TV devices, and guide TV control through SmartThings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow uses broad SmartThings read and device-command scopes. <br>
Mitigation: Review requested SmartThings access before installation, limit scopes if possible, and revoke or rotate the SmartThings app, PAT, and OAuth tokens when no longer needed. <br>
Risk: SmartThings client credentials and OAuth tokens are written to an environment file. <br>
Mitigation: Protect the .env file, avoid committing or sharing it, and rotate credentials if exposure is suspected. <br>
Risk: The default OAuth redirect uses httpbin.org, which is not app-owned infrastructure. <br>
Mitigation: Use a local or app-owned OAuth redirect URI instead of the default redirect when possible. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/regenrek/skills/samsung-smartthings) <br>
- [SmartThings Developer Documentation](https://developer.smartthings.com/docs) <br>
- [SmartThings Personal Access Tokens](https://account.smartthings.com/tokens) <br>
- [SmartThings OAuth Endpoint](https://api.smartthings.com/oauth) <br>
- [Default OAuth Redirect Service](https://httpbin.org/get) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text steps and command descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill asks agents to avoid code snippets and provide plain text operational guidance.] <br>

## Skill Version(s): <br>
0.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
