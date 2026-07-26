## Description: <br>
Audits local skill packages or archives with auto, native, or external scanner engines and optional LLM semantic review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyzlmh](https://clawhub.ai/user/cyzlmh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill before installing local skills, archives, or release bundles to run a quick security review and receive engine findings, risk levels, and an installation conclusion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The visible package may not include the binary paths described in the install text. <br>
Mitigation: Verify the delivered files and checksum before running the scanner. <br>
Risk: Optional LLM review or report upload can send scan data to configured endpoints. <br>
Mitigation: Use only trusted endpoints and avoid scanning directories containing secrets unless that data exposure is acceptable. <br>
Risk: The default auto engine may execute a locally resolved external scanner with the current user's permissions. <br>
Mitigation: Use --engine native when you want the most contained built-in scanner behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cyzlmh/skills/cmic-skill-scanner-linux-arm64) <br>
- [Publisher profile](https://clawhub.ai/user/cyzlmh) <br>
- [Source repository link from skill documentation](https://gitee.com/random_player/cmic-skill-scanner.git) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and scanner findings.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write local scan reports when an output directory is configured; optional upload and LLM review modes require explicit user configuration.] <br>

## Skill Version(s): <br>
0.11.0 (source: server release metadata; bundled build metadata reports v0.11.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
