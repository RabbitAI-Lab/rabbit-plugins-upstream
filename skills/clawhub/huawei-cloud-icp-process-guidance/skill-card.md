## Description: <br>
This skill helps agents answer Huawei Cloud ICP filing questions from a bundled knowledge base and, when needed, supplement answers with bounded web search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and support agents use this skill to answer Huawei Cloud ICP filing questions about materials, process, eligibility, rejections, authorization codes, review status, changes, cancellations, migration, and App filing. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The optional search fallback asks users to install and use an external Agent Reach/Exa toolchain that is broader than the bundled knowledge-base purpose. <br>
Mitigation: Review the Agent Reach dependency before installing it, and use the bundled knowledge base whenever it can answer the question. <br>
Risk: Network-search prompts could expose personal filing data or return supplemental information that is less authoritative than the bundled knowledge base. <br>
Mitigation: Avoid queries containing personal filing data, treat network-search results as supplemental, and prefer Huawei Cloud or official MIIT sources. <br>


## Reference(s): <br>
- [Knowledge Base Index](kb/index.md) <br>
- [Search Fallback Strategy](references/search-fallback.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Agent Reach Installation Guide](https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md) <br>
- [Agent Reach Troubleshooting](https://github.com/Panniantong/agent-reach/blob/main/docs/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown answers with source labels and optional shell command snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Answers stay within the Huawei Cloud ICP filing scope; optional network supplements are labeled as supplemental and should favor official Huawei Cloud or MIIT sources.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
