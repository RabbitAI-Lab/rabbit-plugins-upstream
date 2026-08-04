## Description: <br>
Privacymask helps agents locally detect, mask, classify, and report sensitive data across common document formats without uploading files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to scan documents or folders for personal, financial, health, and business identifiers, create masked copies, classify sensitivity levels, and export audit-friendly reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated reports and diff outputs may contain sensitive original values. <br>
Mitigation: Store reports in access-controlled locations and avoid exporting full original values unless needed for review. <br>
Risk: Local state and history can preserve traces of sensitive masking activity. <br>
Mitigation: Use protected local storage, clear history after sensitive work, and limit access to the configured data directory. <br>
Risk: The skill advertises installing a broader skill matrix, which can expand the user's installed tool surface. <br>
Mitigation: Review any prompt to install the full skill matrix before accepting it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/privacymask) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown, JSON, CSV, and masked document files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local masked copies, diff reports, audit reports, and local configuration or history files.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
