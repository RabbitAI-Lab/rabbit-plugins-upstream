## Description: <br>
Chart helps agents turn inline numeric labels and values into local bar, line, pie, or scatter chart outputs for reports, slides, and quick analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent users can use this skill to select a simple chart type, generate local PNG chart outputs from inline values, and review prior chart records for reuse in documents or presentations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documentation mixes local-only chart generation with callback URL, API-key, and external API language. <br>
Mitigation: Review the skill before installing and do not provide callback URLs, API keys, or sensitive input unless the publisher clarifies why they are required. <br>
Risk: Generated chart history and local output files may contain sensitive input values or labels. <br>
Mitigation: Store generated artifacts in an access-controlled workspace and delete history records or outputs that contain confidential data. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with bash command examples; generated chart artifacts are PNG files with JSON history records.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chart outputs and history are described as local-only artifacts under the skill workspace.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
