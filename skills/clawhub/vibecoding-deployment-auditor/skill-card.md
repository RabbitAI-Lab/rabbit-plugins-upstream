## Description: <br>
Publishes locally built static HTML/CSS/JavaScript, Vite, React, or Vue websites as public HTTPS links through a fixed ZIP upload and deployment workflow, and rejects projects that require backend, database, SSR, server runtime, or remote dependency installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyriswu](https://clawhub.ai/user/kyriswu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, makers, and non-specialist users use this skill to audit, package, upload, deploy, and verify pure static websites such as H5 games, portfolios, company sites, landing pages, and browser-only frontend tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uploads a vetted static ZIP to a fixed deployment service for public hosting. <br>
Mitigation: Use it only when the user has requested publishing, and confirm the build output contains no secrets or private data before upload. <br>
Risk: Remote retention and undeploy behavior are not described in the evidence. <br>
Mitigation: Treat published output as public and avoid deploying content that requires guaranteed deletion or private retention controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyriswu/skills/vibecoding-deployment-auditor) <br>
- [Publisher profile](https://clawhub.ai/user/kyriswu) <br>
- [Static deployment request schema](artifact/templates/static-deployment-request.v1.json) <br>
- [Deployment dossier template](artifact/templates/deployment-dossier.v1.json) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Shell commands, Configuration, Files, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown status updates, JSON deployment records, shell commands, and generated static ZIP manifest and dossier files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce blocked or not_deployed status when static eligibility, upload, deployment, or public URL verification fails.] <br>

## Skill Version(s): <br>
2.3.18 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
