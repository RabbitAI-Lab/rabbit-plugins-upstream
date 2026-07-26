## Description: <br>
Busca conteudo no Stremio Web e transmite para dispositivos Chromecast usando CATT e Playwright. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pedro-valentim](https://clawhub.ai/user/pedro-valentim) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to search for movies or series in Stremio Web and cast the selected stream to a named Chromecast device. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence flags under-disclosed network and browser-security behavior. <br>
Mitigation: Review before installing, change the script to a trusted local Stremio service, and remove or justify disabled browser protections. <br>
Risk: The artifact can log full stream URLs and send them to a Chromecast device. <br>
Mitigation: Avoid logging full stream URLs and confirm the selected title and Chromecast device before casting. <br>
Risk: The automation depends on Stremio Web selectors, a local streaming service, and browser session behavior that may change or fail. <br>
Mitigation: Verify the local service, Playwright, CATT, and selectors before use; keep the browser session open if the stream depends on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pedro-valentim/skills/stremio-cast) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance] <br>
**Output Format:** [Text with shell command execution guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local Stremio service, Playwright, CATT, and access to the target Chromecast device.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
