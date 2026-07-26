## Description: <br>
Generates structured QA test cases from requirement documents, API documentation, design documents, and image-based flow diagrams, then formats the results for JSON and Excel-based review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, developers, and product teams use this skill to turn PRDs, API specifications, UI flows, and batch requirement documents into organized manual test cases. It is intended for test planning and coverage analysis, not for generating or running automated test scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requirement documents and generated reports may contain sensitive product or customer information. <br>
Mitigation: Keep inputs and outputs in a trusted workspace and review generated artifacts before sharing them. <br>
Risk: Generated test-case files or Excel reports may overwrite existing files if output paths are reused. <br>
Mitigation: Choose output paths deliberately and inspect the target directory before running writer or extraction scripts. <br>
Risk: Bundled examples may contain product-specific sample values that are not suitable for reuse. <br>
Mitigation: Treat example credentials, URLs, and product data as sample-only placeholders and replace them with approved test data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-testcase-generator) <br>
- [README](artifact/README.md) <br>
- [Schema reference](artifact/references/schemas.md) <br>
- [Quality reference](artifact/references/quality.md) <br>
- [Design methods reference](artifact/references/design_methods.md) <br>
- [Image analysis reference](artifact/references/image_analysis.md) <br>
- [Environment reference](artifact/references/environment.md) <br>
- [Troubleshooting reference](artifact/references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Files] <br>
**Output Format:** [Structured JSON test-case data and formatted Excel files, with Markdown guidance and shell commands when scripts are used] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write intermediate JSON files and final Excel reports to an output directory selected by the user.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
