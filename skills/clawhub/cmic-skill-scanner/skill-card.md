## Description: <br>
Audits local skill packages or archives with auto, native, or external scan engines and can optionally use LLM semantic review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyzlmh](https://clawhub.ai/user/cyzlmh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill before installing a local skill package, archive, or release bundle to run a quick security scan and review findings and risk level. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Downloaded or locally resolved scanner binaries require trust in the release host or local tool configuration. <br>
Mitigation: Verify the published SHA-256 checksum before running a binary, or build from source after reviewing the code. <br>
Risk: Auto mode may invoke a locally resolved external scanner with the current user's permissions. <br>
Mitigation: Use the native engine when external scanner execution is not intended, and review any external scanner configuration before use. <br>
Risk: Optional upload and LLM review can transmit scan reports or bounded text packets when explicitly enabled. <br>
Mitigation: Keep network features disabled unless needed, use trusted endpoints, and review the target contents and endpoint data policy before enabling them. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/cyzlmh/skills/cmic-skill-scanner) <br>
- [Publisher profile](https://clawhub.ai/user/cyzlmh) <br>
- [Gitee releases](https://gitee.com/random_player/cmic-skill-scanner/releases) <br>
- [v0.11.0 SHA256SUMS](https://gitee.com/random_player/cmic-skill-scanner/raw/main/releases/v0.11.0/SHA256SUMS) <br>
- [Source repository clone URL](https://gitee.com/random_player/cmic-skill-scanner.git) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and scan-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include findings, risk level, engine status, and local report paths when an output directory is requested.] <br>

## Skill Version(s): <br>
0.11.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
