## Description: <br>
Audits local skill packages or archives with auto, native, or external scan engines and optional LLM semantic review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyzlmh](https://clawhub.ai/user/cyzlmh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill before installation to inspect local skill packages, archives, or release bundles and produce a concise risk-focused review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional upload and LLM review can expose scan findings, summaries, and bounded text packets from the scanned package. <br>
Mitigation: Keep --upload-url and --use-llm disabled unless needed, and enable them only with trusted endpoints and a clear data-handling policy. <br>
Risk: The default auto engine can invoke a locally resolved external scanner with the current user's process permissions. <br>
Mitigation: Use --engine native when you want to avoid external scanner execution and review any external scanner configuration before use. <br>
Risk: The release includes a precompiled Linux x64 binary that requires local execution trust. <br>
Mitigation: Verify the documented SHA-256 checksum before running the binary, or build from source when a higher assurance path is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cyzlmh/skills/cmic-skill-scanner-linux-amd64) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with findings, risk levels, command examples, and installation conclusions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local report files when --output-dir is used; optional upload and LLM review require explicit configuration.] <br>

## Skill Version(s): <br>
0.11.1 (source: server release metadata and assets/build/build-info.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
