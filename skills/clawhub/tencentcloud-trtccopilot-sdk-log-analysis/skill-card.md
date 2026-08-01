## Description: <br>
Analyzes local Tencent Cloud TRTC, IM, and TUI SDK client logs by identifying log types, decoding .clog/.xlog files, building timelines, and offering a local web preview. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-adm](https://clawhub.ai/user/tencent-adm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and support engineers use this skill to diagnose customer-provided Tencent Cloud SDK client logs, extract evidence-backed timelines, identify likely root causes, and prepare concise troubleshooting guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes raw SDK logs that may contain identifiers, tokens, signed URLs, device data, or user metadata. <br>
Mitigation: Keep analysis local where possible, redact logs before sharing, and include only bounded, sanitized evidence snippets in final reports. <br>
Risk: Decoder selection can run environment-selected or npm-fetched code. <br>
Mitigation: Prefer the bundled decoder and avoid setting CLOG_DECODER_BIN or custom npm registry and package environment variables unless the source is trusted. <br>
Risk: The local web preview can expose sensitive log contents while it is running. <br>
Mitigation: Use the preview only on loopback, stop or disable the service when it is no longer needed, and avoid sharing preview links outside the local machine. <br>


## Reference(s): <br>
- [TRTC analysis playbook](references/trtc-analysis-playbook.md) <br>
- [TRTC deep log patterns](references/trtc-deep-log-patterns.md) <br>
- [TRTC known issues](references/trtc-known-issues.md) <br>
- [TRTC audio diagnostics](references/trtc-audio-diagnostics.md) <br>
- [TRTC screen share diagnostics](references/trtc-screen-share-diagnostics.md) <br>
- [TRTC SDK versions](references/trtc-sdk-versions.md) <br>
- [TRTC product concepts](references/trtc-product-concepts.md) <br>
- [TRTC event ID mapping](references/trtc-event-id-mapping.md) <br>
- [Web log patterns](references/web-log-patterns.md) <br>
- [Native log patterns](references/native-log-patterns.md) <br>
- [Mini Program log patterns](references/miniprogram-log-patterns.md) <br>
- [IM xlog patterns](references/im-xlog-patterns.md) <br>
- [SDK crash analysis](references/sdk-crash-analysis.md) <br>
- [Audio troubleshooting](references/audio-troubleshooting.md) <br>
- [ClawHub skill page](https://clawhub.ai/tencent-adm/skills/tencentcloud-trtccopilot-sdk-log-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown analysis with evidence tables, redacted code blocks, generated timeline files, JSON manifests, and local preview links when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should cite log files and line numbers, redact sensitive log content, and keep raw log evidence bounded and non-clickable.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release metadata; artifact frontmatter says 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
