## Description: <br>
Query Idealista API via idealista-cli (OAuth2 client credentials). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[quifago](https://clawhub.ai/user/quifago) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to configure Idealista API credentials, obtain tokens, search property listings, and compute listing statistics through idealista-cli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on Idealista API key and secret handling for OAuth2 client credentials. <br>
Mitigation: Prefer environment variables or a secret manager; keep any config file private, avoid committing credentials, and rotate credentials if exposure is suspected. <br>
Risk: The skill installs or uses an external idealista-cli repository. <br>
Mitigation: Review the external repository before installation or pin a known commit. <br>


## Reference(s): <br>
- [ClawHub Idealista skill page](https://clawhub.ai/quifago/skills/idealista) <br>
- [idealista-cli repository](https://github.com/quifago/idealista-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local idealista-cli, python3, and Idealista OAuth2 client credentials.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
