## Description: <br>
A Chinese-language Q&A skill that helps agents answer Huawei Cloud ICP filing questions from a bundled knowledge base and optional search fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, support agents, and cloud operators use this skill to answer Huawei Cloud ICP filing process, materials, review, rejection, domain, and App filing questions. It is intended to keep answers concise, source-backed, and limited to Huawei Cloud ICP filing topics. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The optional Agent Reach/Exa search fallback may send filing questions to a third-party search service. <br>
Mitigation: Use the bundled knowledge base first, avoid prompts containing personal IDs, company secrets, domain credentials, or full filing records, and use search only when supplemental verification is needed. <br>
Risk: Search-backed or stale policy answers may be inaccurate for filing actions that affect domains, identity documents, DNS, or cancellation. <br>
Mitigation: Treat search-backed answers as supplemental and verify material filing steps against Huawei Cloud or MIIT official sources before acting. <br>


## Reference(s): <br>
- [Search fallback strategy](references/search-fallback.md) <br>
- [Verification method](references/verification-method.md) <br>
- [Acceptance criteria](references/acceptance-criteria.md) <br>
- [CLI installation guide](references/cli-installation-guide.md) <br>
- [IAM policies](references/iam-policies.md) <br>
- [Agent Reach troubleshooting](https://github.com/Panniantong/agent-reach/blob/main/docs/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown briefing with source references and optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Answers should remain scoped to Huawei Cloud ICP filing, cite local knowledge-base sources, and label search-backed supplements as supplemental.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
