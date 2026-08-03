## Description: <br>
This skill analyzes fixed-camera video from multiple home zones to detect long-term inactivity in solo-living elder care settings and produce structured alerts when the configured inactivity window, default 12 hours, is exceeded. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, smart-home integrators, and elder-care service operators use this skill to analyze home monitoring videos or video URLs, summarize activity and inactivity signals, and return alerts, recommendations, and report links for follow-up review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Elder-home videos, video URLs, identity values, report metadata, and account tokens may be sent to and stored by external lifeemergence.com services. <br>
Mitigation: Use only with explicit informed consent from monitored people or authorized caregivers, verify backend retention and deletion controls, and avoid sensitive rooms unless legally and ethically justified. <br>
Risk: The skill creates persistent identity or account state with limited user control. <br>
Mitigation: Confirm account lifecycle, access, and deletion controls before deployment, and do not expose internal identity values in user-facing outputs. <br>
Risk: The skill may be mistaken for a complete emergency notification or continuous safety monitoring system. <br>
Mitigation: Treat outputs as auxiliary monitoring signals, require human verification for alerts, and maintain independent emergency response procedures. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-long-term-immobility-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Structured analysis report text or JSON, with Markdown tables for historical report lists and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include alert levels, inactivity duration, detected activity zones, recommendations, and report links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
