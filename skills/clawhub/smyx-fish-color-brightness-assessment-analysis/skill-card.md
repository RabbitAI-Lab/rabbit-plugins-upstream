## Description: <br>
Assesses ornamental fish color vibrancy from aquarium images or videos by extracting HSV saturation and brightness signals, comparing them with species-specific baselines, and returning a structured vibrancy report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze ornamental fish footage from aquarium cameras or uploaded files, estimate color vibrancy, review HSV and baseline-comparison signals, and query prior cloud reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fish images, videos, and report queries may be sent to LifeEmergence cloud APIs. <br>
Mitigation: Use the skill only with footage approved for cloud processing, and confirm retention, authorization, and sharing expectations before deployment. <br>
Risk: The skill may silently create or reuse an internal identity and store user or token records in the workspace data directory. <br>
Mitigation: Run it in a dedicated workspace, restrict access to local data files, and review or clear stored identity and token records in shared environments. <br>
Risk: The security evidence reports incomplete disclosure around cloud uploads, report history queries, and local token handling. <br>
Mitigation: Review the ClawHub security summary and the relevant artifact behavior before using the skill with sensitive aquarium footage or production accounts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-color-brightness-assessment-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Structured JSON or Markdown text with report links and optional file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include vibrancy scores, HSV values, species baseline comparisons, trend summaries, alert levels, recommended actions, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
