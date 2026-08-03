## Description: <br>
Builds a customizable interactive HTML dashboard with Alpine.js, Vanilla CSS, and a Python local server to display Fulcra data locally and optionally export an isolated public directory for sharing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fulcra](https://clawhub.ai/user/fulcra) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to scaffold and customize a local Fulcra data dashboard, ingest approved Fulcra records, and optionally prepare a specific public export directory for sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private Fulcra data or intermediate files could be exposed if the working application root is published. <br>
Mitigation: Publish only the reviewed public directory after confirming exactly which JSON and JSONL files it contains. <br>
Risk: The dashboard uses third-party CDN and font assets that introduce external dependencies when viewing or sharing sensitive dashboards. <br>
Mitigation: Vendor JavaScript and font assets locally or remove external CDN dependencies before sensitive use. <br>
Risk: Fulcra data fetches, third-party scripts, external tools, or public deployment may process or expose user data. <br>
Mitigation: Request explicit consent before data ingestion, external asset use, image generation, or publication. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fulcra/skills/fulcra-dashboard) <br>
- [Publisher Profile](https://clawhub.ai/user/fulcra) <br>
- [Fulcra Agent Skills Homepage](https://github.com/fulcradynamics/agent-skills) <br>
- [Prefab](https://gofastmcp.com/apps/prefab) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands plus HTML, CSS, JavaScript, Python, and JSON or JSONL dashboard files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May scaffold a local dashboard, fetch Fulcra data with consent, and export an isolated public directory for optional sharing.] <br>

## Skill Version(s): <br>
0.1.8 (source: evidence release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
