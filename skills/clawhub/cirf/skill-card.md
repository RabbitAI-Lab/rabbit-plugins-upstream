## Description: <br>
Interactive crypto deep-research framework with human-AI collaboration for superior research outcomes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kudodefi](https://clawhub.ai/user/kudodefi) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use CIRF to run structured, collaborative crypto research workflows, including market intelligence, project fundamentals, technical analysis, content transformation, and QA review. The framework guides an AI assistant through Markdown and YAML research methods while keeping the human user involved in scoping, validation, and final judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crypto research output may be incomplete, outdated, or unsuitable as a sole basis for financial decisions. <br>
Mitigation: Review generated reports, verify source data independently, and avoid relying on skill output alone for trading or investment decisions. <br>
Risk: Prompts, documents, or workspace files used during web-assisted research may expose sensitive wallet material, secrets, or private trading plans to the agent context. <br>
Mitigation: Do not place secrets, wallet material, or private trading plans in prompts, workspace documents, or research inputs. <br>
Risk: The skill reads Markdown/YAML framework files and writes local research reports plus workspace metadata. <br>
Mitigation: Review framework files before use and monitor generated files under the local workspaces directory. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kudodefi/skills/cirf) <br>
- [README](README.md) <br>
- [Security and Permissions](SECURITY.md) <br>
- [Research Methodology Guide](framework/guides/research-methodology.md) <br>
- [Output Standards Guide](framework/guides/output-standards.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, research briefs, content drafts, QA reviews, and YAML workspace metadata.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Research outputs are intended to be saved under local workspaces/{project-id}/outputs/ directories, with project metadata stored in workspace.yaml.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
