## Description: <br>
PC 200 publishes small files to probe ClawHub multipart file-count limits associated with 413 upload errors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[autogame-17](https://clawhub.ai/user/autogame-17) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers maintaining ClawHub publishing workflows use this skill as a diagnostic package to test how many small files a release upload accepts before multipart count limits are reached. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package is a diagnostic upload/file-count test rather than a functional user-facing skill. <br>
Mitigation: Install it only when intentionally testing ClawHub upload limits, and remove it after the diagnostic workflow is complete. <br>
Risk: The release intentionally contains many tiny files, which can add noise to project review or packaging workflows. <br>
Mitigation: Review the file list before deployment and keep the package isolated from normal skill projects. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/autogame-17/skills/cc-pc-200) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JavaScript source files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes 198 inert tiny JavaScript files for upload-count probing.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
