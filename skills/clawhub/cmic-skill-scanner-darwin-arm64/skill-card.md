## Description: <br>
Audits local skill packages or archives with auto, native, or external scanner engines, with optional LLM semantic review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyzlmh](https://clawhub.ai/user/cyzlmh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to inspect local skill packages, release bundles, or archives before installation and review scanner findings, engine status, and risk summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private package text or scan details may be sent to remote services when upload or LLM-review options are enabled. <br>
Mitigation: Leave remote upload and native LLM review disabled for private or proprietary skills unless the configured endpoint is trusted, retention is understood, and transmission of selected package text or scan details is acceptable. <br>
Risk: The scanner is a local executable, and auto mode may invoke a locally resolved external scanner with the current user's permissions. <br>
Mitigation: Verify the bundled binary checksum before use, build from source when stronger assurance is needed, and use the native engine when external scanner execution is not desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cyzlmh/skills/cmic-skill-scanner-darwin-arm64) <br>
- [Publisher profile](https://clawhub.ai/user/cyzlmh) <br>
- [Installation guide](INSTALL.md) <br>
- [Build metadata](assets/build/build-info.json) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries with inline shell commands and optional local report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save scan reports to an output directory; remote upload and LLM review are optional and require explicit configuration.] <br>

## Skill Version(s): <br>
0.11.0 (source: server release metadata; build-info.json reports v0.11.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
