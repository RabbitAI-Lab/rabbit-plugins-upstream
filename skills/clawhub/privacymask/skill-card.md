## Description: <br>
Privacymask helps agents scan local files and folders for personal, financial, health, and business identifiers, then produce masked copies or detection reports without uploading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to redact sensitive data from finance, audit, legal, customer, and compliance documents before sharing or processing them. It can preview findings, apply built-in or custom masking rules, and export detection reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can process local files and write masked copies or reports, and those outputs may still contain sensitive metadata. <br>
Mitigation: Review selected input paths, output locations, and generated reports before sharing or retaining them. <br>
Risk: The release security summary notes under-scoped automatic routing for file-changing actions. <br>
Mitigation: Confirm whether a request is preview-only or file-changing before allowing directory-wide masking or report export. <br>
Risk: The artifact promotes installing a broader skill matrix that includes unrelated skills. <br>
Mitigation: Install only this skill unless the user intentionally wants the additional matrix skills. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/privacymask) <br>


## Skill Output: <br>
**Output Type(s):** [text, files, configuration, guidance] <br>
**Output Format:** [Natural-language responses, masked file copies, and JSON or CSV reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May process local paths and write masked copies, reports, configuration, custom rules, or history records.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
