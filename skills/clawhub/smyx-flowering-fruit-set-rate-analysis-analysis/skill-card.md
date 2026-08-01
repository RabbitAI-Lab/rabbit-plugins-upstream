## Description: <br>
Analyzes tomato or chili flower and fruit-cluster images or videos to count open flowers and young fruits, estimate fruit-set rate, and return grower-facing observations and recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External growers, greenhouse operators, and gardening agents use this skill to evaluate tomato or chili pollination outcomes from plant media and decide whether to adjust pollination, humidity, temperature, or water and fertilizer practices. Developers can invoke its bundled command-line workflow to analyze a local media file, analyze a remote media URL, or list prior cloud reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant photos, videos, URLs, and report history may be processed by configured lifeemergence.com services. <br>
Mitigation: Use only media that is appropriate for remote processing, and review the publisher's data handling terms before installation. <br>
Risk: The skill may silently create or reuse a user identity and store service tokens in the workspace data directory. <br>
Mitigation: Run in a controlled workspace, inspect stored credentials after use, and require clear account, token, and deletion controls before broader deployment. <br>
Risk: Security evidence marks the release as suspicious pending review. <br>
Mitigation: Review and scan the skill before deployment, especially its remote service configuration, identity behavior, and history-report access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-flowering-fruit-set-rate-analysis-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface reference](artifact/references/api_doc.md) <br>
- [Analysis API interface reference](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown report text with structured JSON content and optional report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save output to a file; historical report listing returns structured records with export links when available.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
