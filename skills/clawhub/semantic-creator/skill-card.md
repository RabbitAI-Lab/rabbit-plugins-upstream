## Description: <br>
Builds evidence-only Kimball semantic layers from APIs, CLIs, or tables with an HTML decision workbench and emits OKF or YAML. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agenticweb4](https://clawhub.ai/user/agenticweb4) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data engineers use this skill to convert REST, OpenAPI, CLI, table, DDL, or CSV evidence into governed semantic-layer decisions and generated OKF or repo-YAML artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect approvals can allow unresolved or blocked modeling decisions into generated semantic-layer artifacts. <br>
Mitigation: Review the HTML decision workbench carefully and return approved:true only when all pending and blocked decisions are actually resolved. <br>
Risk: The workflow writes local review and output files, so generated artifacts may need inspection before reuse. <br>
Mitigation: Review generated OKF or YAML files and run the verification phase before deployment or downstream consumption. <br>
Risk: Much of the workflow text is Chinese, which can increase reviewer friction for teams that do not read Chinese. <br>
Mitigation: Use reviewers comfortable with the workflow language or translate decision content before approval. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/semantic-creator) <br>
- [Ingest reference](artifact/references/ingest.md) <br>
- [Review reference](artifact/references/review.md) <br>
- [OKF emit reference](artifact/references/emit-okf.md) <br>
- [YAML emit reference](artifact/references/emit-yaml.md) <br>
- [Verify reference](artifact/references/verify.md) <br>
- [Worked examples](artifact/references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown, JSON decision payloads, OKF Markdown bundles, and optional YAML semantic ontology files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local review and output files after explicit user approval; default output is an OKF v0.1 bundle.] <br>

## Skill Version(s): <br>
0.5.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
