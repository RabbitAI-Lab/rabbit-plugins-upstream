## Description: <br>
Identifies individual livestock, including pigs, cattle, and sheep, from facial or body-pattern images or videos and returns a stable individual ID with confidence for precision farm management and tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Farm operators, livestock-management teams, and external users use this skill to identify pigs, cattle, or sheep from images, videos, local files, or URLs. It links visual observations to an individual ID, confidence score, matched feature regions, and report link for tracking workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends livestock media, remote media URLs, and identity or session metadata to cloud services. <br>
Mitigation: Use it only where that transfer is approved, avoid unnecessary sensitive media, and disclose cloud processing to affected operators before deployment. <br>
Risk: The skill may silently create or reuse a local account record and store tokens in a workspace SQLite database. <br>
Mitigation: Review local identity and token storage before installation, isolate workspaces that run the skill, and prefer a version that requires explicit consent for account creation and history lookup. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-individual-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON text containing livestock identification results, confidence values, matched feature regions, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can list historical reports as a Markdown table through the cloud API; analysis may also be saved to a local output file.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release metadata; SKILL.md frontmatter lists 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
