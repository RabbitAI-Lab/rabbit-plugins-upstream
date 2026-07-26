## Description: <br>
Analyzes fixed-camera kitchen video or video URLs to detect unattended active stove conditions and return structured stove-left-on alerts, report links, and historical report listings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, family members, and elder-care operators use this skill to analyze kitchen camera footage for unattended stove-left-on conditions, review alert levels, and retrieve cloud report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Kitchen video files or URLs are sent to configured LifeEmergence cloud services for analysis and report history. <br>
Mitigation: Use only with household consent, submit only necessary media, and avoid inputs that expose unrelated private activity. <br>
Risk: The skill may create or reuse a local identity and store cloud account tokens in workspace data. <br>
Mitigation: Restrict access to the workspace data directory and plan token rotation or local data deletion during uninstall or handoff. <br>
Risk: Stove-left-on alerts and valve-shutdown suggestions may affect physical safety decisions. <br>
Mitigation: Require human confirmation and independent safety controls before acting on alerts or integrating valve shutdown. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-kitchen-stove-left-on-detection-analysis) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files, guidance] <br>
**Output Format:** [Plain text or Markdown wrapping structured JSON report data, alert details, report history, and report links; optionally saved to a local output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report export URLs and historical report lists.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter states 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
