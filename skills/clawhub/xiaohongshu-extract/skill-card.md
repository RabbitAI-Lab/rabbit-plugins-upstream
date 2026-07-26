## Description: <br>
Extract metadata from Xiaohongshu (XHS) share or discovery URLs by parsing window.__INITIAL_STATE__ and returning note details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jovijovi](https://clawhub.ai/user/jovijovi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and analysts use this skill to extract public Xiaohongshu note metadata, engagement counts, tags, user details, and video stream information from share or discovery URLs for downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The script makes outbound web requests to URLs provided by the user. <br>
Mitigation: Use public Xiaohongshu URLs only and avoid private, internal, or sensitive URLs. <br>
Risk: The script can write extracted metadata to a local path supplied with --output. <br>
Mitigation: Choose output paths carefully and avoid overwriting important files. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON, flattened JSON records, error JSON, Markdown guidance, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The extractor can print JSON to stdout or write JSON to a user-selected local output path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
