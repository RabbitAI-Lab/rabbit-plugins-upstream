## Description: <br>
Builds a highly customizable, interactive HTML dashboard using Alpine.js, modern Vanilla CSS, and a Python backend to display private data from the user's Fulcra data store locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fulcra](https://clawhub.ai/user/fulcra) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to scaffold and customize a local Fulcra data dashboard, fetch user-approved Fulcra records, preview them locally, and prepare a reviewed public export when the user consents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose private Fulcra data if raw working files or unintended public files are published. <br>
Mitigation: Preview the dashboard locally and publish only the reviewed public/ directory containing the exact files approved for sharing. <br>
Risk: The generated dashboard can load third-party CDN scripts and web fonts while displaying sensitive data. <br>
Mitigation: For stricter privacy, replace CDN scripts and Google Fonts with locally bundled assets before opening or sharing sensitive dashboards. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fulcra/skills/fulcra-dashboard) <br>
- [Fulcra publisher profile](https://clawhub.ai/user/fulcra) <br>
- [Fulcra agent skills homepage](https://github.com/fulcradynamics/agent-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated dashboard project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a local HTML/CSS/JavaScript dashboard scaffold, Python helper scripts, Fulcra data manifests, and optional public export instructions.] <br>

## Skill Version(s): <br>
0.1.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
