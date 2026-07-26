## Description: <br>
Operates HCP Terraform through an OOMOL-connected account using the oo CLI to inspect account, organization, workspace, and run data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to inspect Terraform account details, organizations, workspaces, runs, and run history through an OOMOL-connected Terraform account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can query Terraform account, organization, workspace, and run information through OOMOL. <br>
Mitigation: Install only where that read access is acceptable, and review requested Terraform actions before execution. <br>
Risk: Future connector actions may become write-capable or destructive even though the current artifact evidence is read-oriented. <br>
Mitigation: Require explicit user confirmation for any action marked write or destructive and verify the live connector schema before building the payload. <br>
Risk: The skill may be invoked broadly for general Terraform requests. <br>
Mitigation: Use it for OOMOL connector-backed Terraform data access, and avoid unnecessary connector calls for general Terraform advice. <br>


## Reference(s): <br>
- [Terraform homepage](https://www.hashicorp.com/products/terraform) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-terraform) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and connector result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo CLI connector schemas before constructing Terraform connector payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
