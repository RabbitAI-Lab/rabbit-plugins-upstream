## Description: <br>
Retrieve current, source-backed documentation for libraries, frameworks, SDKs, APIs, developer tools, open-source projects, and GitHub projects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wei840222](https://clawhub.ai/user/wei840222) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to look up current, version-aware documentation and examples before answering implementation, setup, migration, troubleshooting, and API usage questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [Context7 overview](https://context7.com/docs/overview) <br>
- [Context7 API guide](https://context7.com/docs/api-guide) <br>
- [Context7 GitHub repository](https://github.com/upstash/context7) <br>
- [Context7 via mcporter](references/mcporter-workflow.md) <br>
- [Context7 API fallback](references/api-fallback.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Code] <br>
**Output Format:** [Markdown answers with source URLs, selected library IDs, version-pin status, fallback status, and optional command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses mcporter, jq, and curl when available. Avoid sending private code, credentials, or proprietary details in documentation queries unless the user explicitly confirms.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
