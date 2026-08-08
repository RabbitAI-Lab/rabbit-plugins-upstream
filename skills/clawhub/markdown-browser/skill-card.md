## Description: <br>
Wrapper skill for OpenClaw web_fetch results that post-processes fetched pages with Content-Signal policy decisions, privacy-preserving URL redaction, optional markdown normalization, and a stable output schema. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2233admin](https://clawhub.ai/user/2233admin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill after an OpenClaw web_fetch call to normalize fetched content, preserve relevant policy signals, redact sensitive URL components, and return a consistent JSON object for downstream agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the skill requires npm dependency resolution. <br>
Mitigation: Install dependencies from a trusted registry, review the lockfile, and verify package integrity before deployment in sensitive environments. <br>
Risk: Fetched webpage content can contain prompt-like or untrusted text even after normalization. <br>
Mitigation: Treat normalized content as untrusted input, review policy_action before use, and keep downstream agent safeguards in place. <br>
Risk: Content-Signal policy handling depends on optional header values supplied with the web_fetch result. <br>
Mitigation: Route unknown or missing policy signals through review before using fetched content in sensitive workflows. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/2233admin/markdown-browser) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [JSON object with normalized content, policy action, content signal, redacted source URL, status code, token estimate, and fallback flag] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an existing OpenClaw web_fetch result as input; HTML content may be converted to markdown with turndown.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
