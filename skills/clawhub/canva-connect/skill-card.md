## Description: <br>
Manage Canva designs, assets, and folders via the Connect API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolmanns](https://clawhub.ai/user/coolmanns) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to automate Canva asset pipelines, design exports, folder organization, and brand template autofill through the Canva Connect API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants Canva account access and stores refreshable OAuth tokens locally. <br>
Mitigation: Install only when that access is acceptable, protect the local token file, and run auth logout or revoke the Canva integration when access is no longer needed. <br>
Risk: Delete commands can remove Canva designs or assets without strong safeguards. <br>
Mitigation: Require explicit user confirmation outside the skill and verify target IDs before running delete operations. <br>
Risk: Asset upload commands send selected local files to Canva. <br>
Mitigation: Review file contents and destination context before upload, especially for confidential or regulated material. <br>


## Reference(s): <br>
- [Canva Connect API Reference](references/api.md) <br>
- [Canva Connect documentation](https://canva.dev/docs/connect/) <br>
- [Canva developer integrations](https://canva.com/developers/integrations) <br>
- [ClawHub skill listing](https://clawhub.ai/coolmanns/skills/canva-connect) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, JSON, files] <br>
**Output Format:** [Markdown guidance with bash commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can export Canva designs to local files and upload selected local files to Canva.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
