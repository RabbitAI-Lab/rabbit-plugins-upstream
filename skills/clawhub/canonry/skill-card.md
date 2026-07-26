## Description: <br>
Set up and operate Canonry AEO projects: inspect mention and citation coverage, diagnose regressions, run technical audits, and act through the Canonry CLI or MCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arberx](https://clawhub.ai/user/arberx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and AEO operators use this skill to run Canonry projects, inspect AI mention and citation coverage, diagnose visibility regressions, and apply approved fixes through Canonry CLI or MCP workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Canonry can operate on connected AEO projects and services, including write-capable integrations when credentials allow it. <br>
Mitigation: Use the narrowest API key or read-only scope that fits the task and require explicit approval for every mutation or quota-consuming run. <br>
Risk: Canonry configuration can contain secret-bearing API keys and service credentials. <br>
Mitigation: Protect ~/.canonry/config.yaml, do not print or paste credentials, and run interactive initialization outside the agent transcript. <br>
Risk: Client domains, transcripts, and project memory can contain sensitive business material. <br>
Mitigation: Avoid exposing real client data in public channels and clear Aero transcripts or memory when handling sensitive material. <br>


## Reference(s): <br>
- [Canonry](https://canonry.ai) <br>
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology) <br>
- [AEO Analysis](references/aeo-analysis.md) <br>
- [Canonry CLI Reference](references/canonry-cli.md) <br>
- [Indexing Workflows for AEO](references/indexing.md) <br>
- [Server-side traffic](references/server-side-traffic.md) <br>
- [Google Business Profile Integration](references/google-business-profile.md) <br>
- [WordPress Integration](references/wordpress-integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, code] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, JSON outputs, and implementation instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the Canonry runtime and explicit approval for mutations or quota-consuming sweeps.] <br>

## Skill Version(s): <br>
4.134.0+46e3bd6 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
