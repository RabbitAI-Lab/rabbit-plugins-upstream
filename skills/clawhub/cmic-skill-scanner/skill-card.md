## Description: <br>
CMIC Skill Scanner audits local skill packages or archives with auto, native, or external engines and can optionally add LLM semantic analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyzlmh](https://clawhub.ai/user/cyzlmh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill before installing local skills, archives, or release bundles to scan for suspicious patterns, review findings, and choose native, external, or auto scanner behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Downloaded or locally resolved scanner binaries may not match a trusted source. <br>
Mitigation: Verify release checksums before running, or build the scanner from source. <br>
Risk: Auto or external engine mode can run a locally resolved scanner with the current user's permissions. <br>
Mitigation: Use --engine native when you do not want an external scanner to execute, and review external scanner configuration separately. <br>
Risk: Optional upload or LLM review features can send report data or bounded target text to configured endpoints. <br>
Mitigation: Enable --upload-url or --use-llm only for endpoints you trust and confirm the endpoint data-handling policy first. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cyzlmh/skills/cmic-skill-scanner) <br>
- [Gitee releases](https://gitee.com/random_player/cmic-skill-scanner/releases) <br>
- [v0.11.1 SHA256 checksums](https://gitee.com/random_player/cmic-skill-scanner/raw/main/releases/v0.11.1/SHA256SUMS) <br>
- [Source repository](https://gitee.com/random_player/cmic-skill-scanner.git) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scanner output may include findings, risk level, engine status, and optional local report files when an output directory is configured.] <br>

## Skill Version(s): <br>
0.11.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
