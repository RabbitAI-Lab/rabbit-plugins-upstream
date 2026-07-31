## Description: <br>
CMIC Skill Scanner helps agents audit local skill packages or archives with auto, native, or external scanner engines and optional LLM semantic review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyzlmh](https://clawhub.ai/user/cyzlmh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill before installing or reviewing local skill packages, archives, or release bundles to inspect scanner findings, engine status, and installation risk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The reviewed package is missing the executable and checksum that its documentation tells users to run and verify. <br>
Mitigation: Resolve the package mismatch before installation by confirming the actual skillscan executable source and independently verifying its checksum. <br>
Risk: Auto mode may invoke a locally resolved external scanner with separate trust and data-handling behavior. <br>
Mitigation: Use --engine native when external scanner execution is not desired, and trust external scanners only after reviewing their configuration and policies. <br>
Risk: Optional upload and LLM review modes can share reports or bounded target-package text with configured endpoints. <br>
Mitigation: Enable --upload-url and --use-llm only with trusted endpoints and confirm the data-handling policy before sending review data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cyzlmh/skills/cmic-skill-scanner-darwin-arm64) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and scan summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe engine findings, risk level, installation conclusions, optional upload behavior, and LLM review configuration.] <br>

## Skill Version(s): <br>
0.11.1 (source: server release evidence and bundled build metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
