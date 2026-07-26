## Description: <br>
Analyzes Tencent Cloud SDK client logs by identifying local .clog, .xlog, and text log types, decoding binary logs, and building TRTC/IM/TUI client timelines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-adm](https://clawhub.ai/user/tencent-adm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and support engineers use this skill to analyze user-provided Tencent Cloud TRTC, IM, and TUI client logs, decode .clog/.xlog files, generate timelines, and troubleshoot session or audio issues with line-level evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can decode and persist local logs that may contain identifiers, tokens, or customer data. <br>
Mitigation: Use sanitized logs when possible, review generated files before sharing, and avoid exposing unredacted logs or signed URLs. <br>
Risk: The local preview feature can start a persistent localhost viewer daemon. <br>
Mitigation: Set SDK_LOG_PREVIEW=0 when a web viewer is not needed and stop viewer daemons after analysis. <br>
Risk: Internal Tencent environments may allow remote log retrieval through SSO-backed CLI credentials. <br>
Mitigation: Run internal query commands only after confirming the environment check allows them and that the data is appropriate for the investigation. <br>
Risk: The decoder strategy includes runtime package execution as a fallback. <br>
Mitigation: Prefer the vendored decoder and review any runtime package execution before allowing network-backed fallback behavior. <br>


## Reference(s): <br>
- [References](references/README.md) <br>
- [Web log patterns](references/web-log-patterns.md) <br>
- [Native log patterns](references/native-log-patterns.md) <br>
- [Mini Program log patterns](references/miniprogram-log-patterns.md) <br>
- [Audio troubleshooting guide](references/audio-troubleshooting.md) <br>
- [Internal query capability](references/internal-tools.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown analysis with evidence tables, log excerpts, optional localhost preview links, and generated timeline files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create decoded log files, timeline.md, timeline.json, manifest.json, viewer-index.json, and a local preview daemon when preview is enabled.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter reports 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
