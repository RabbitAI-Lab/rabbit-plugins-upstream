## Description: <br>
Audits local skill packages or archives with auto, native, or external scan engines and can optionally use LLM semantic analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyzlmh](https://clawhub.ai/user/cyzlmh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to inspect local skill packages, archives, or release bundles before installation and review engine findings, risk level, and installation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled or downloaded scanner binary must be trusted before execution. <br>
Mitigation: Verify the published SHA-256 checksum before running the binary, or build from source when stronger supply-chain assurance is required. <br>
Risk: Optional LLM review can send bounded target-package text to a user-configured endpoint, and basic redaction may not remove all sensitive text. <br>
Mitigation: Enable LLM review only with trusted endpoints and review the target package for sensitive data before opting in. <br>
Risk: Auto or external engine modes may execute a locally resolved external scanner with the current user's permissions. <br>
Mitigation: Use the native engine for isolated local scanning, or separately trust and configure any external scanner before enabling it. <br>
Risk: Optional report upload sends structured scan reports to the configured upload URL. <br>
Mitigation: Leave upload disabled unless the destination is approved and the instance identifier and report contents are appropriate to share. <br>


## Reference(s): <br>
- [CMIC Skill Scanner (Linux x64) on ClawHub](https://clawhub.ai/cyzlmh/skills/cmic-skill-scanner-linux-amd64) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and command-line scanner reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include engine status, findings, risk levels, and optional local output files when an output directory is configured.] <br>

## Skill Version(s): <br>
0.11.0 (source: server release metadata and build-info.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
