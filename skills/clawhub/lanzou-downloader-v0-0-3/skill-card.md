## Description: <br>
Downloads files from Lanzou Cloud sharing links by resolving anti-crawling checks, optional extraction passwords, real CDN download URLs, and saving the file for the user. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwqww1](https://clawhub.ai/user/wwqww1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when a user asks to download a Lanzou Cloud shared file, including links that require an extraction password. It is limited to Lanzou-style sharing links and is not intended for other cloud storage providers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports that the skill disables HTTPS certificate checks while handling passwords, cookies, remote JavaScript, and downloaded files. <br>
Mitigation: Run it only in a constrained workspace and only with trusted Lanzou links; restore normal HTTPS certificate validation before routine use. <br>
Risk: The security guidance calls out output path containment and a debug HTML dump as concerns for routine use. <br>
Mitigation: Constrain output paths to the workspace and remove or gate debug HTML dumping before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wwqww1/skills/lanzou-downloader-v0-0-3) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/wwqww1) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Text] <br>
**Output Format:** [Console status text plus a downloaded file path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Lanzou sharing URL and may use an optional output path and optional extraction password.] <br>

## Skill Version(s): <br>
0.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
