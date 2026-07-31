## Description: <br>
Audits local skill packages or archives with auto, native, or external scanning engines and can optionally add LLM semantic review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyzlmh](https://clawhub.ai/user/cyzlmh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to inspect local skill packages before installation, review engine findings, and produce short installation risk conclusions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact documentation references a bundled scanner binary and checksum file that were not present in the inspected artifact. <br>
Mitigation: Verify the binary checksum against trusted release metadata or build the scanner from source before running it. <br>
Risk: The default auto engine can execute a locally resolved external scanner with the current user's permissions. <br>
Mitigation: Run with --engine native when external scanner execution is not intended, and review any configured external scanner separately. <br>
Risk: Optional upload and LLM review settings can disclose report findings or selected package text to configured endpoints. <br>
Mitigation: Keep --upload-url and --use-llm disabled unless needed, and use only endpoints with an acceptable data-handling policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cyzlmh/skills/cmic-skill-scanner-linux-arm64) <br>
- [CMIC Skill Scanner source link from artifact documentation](https://gitee.com/random_player/cmic-skill-scanner.git) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON scanner reports with engine status, findings, and concise installation guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports are local by default; --output-dir writes report files, --upload-url optionally sends report data, and --use-llm optionally sends a bounded text packet to a configured endpoint.] <br>

## Skill Version(s): <br>
0.11.1 (source: server release metadata; build-info.json reports v0.11.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
