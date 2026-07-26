## Description: <br>
Guides agents to search an open-source project's issue tracker and latest release before proposing custom debugging workarounds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lbwdada](https://clawhub.ai/user/lbwdada) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and support engineers use this skill when troubleshooting bugs, errors, missing features, or unexpected behavior in open-source projects. It helps them check known issues, merged fixes, and release versions before investing time in custom workarounds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Issue tracker searches can expose private repository names, tokens, or sensitive error text if copied into public queries. <br>
Mitigation: Review search terms and commands before execution, and remove secrets or private details from public GitHub or GitLab lookups. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lbwdada/skills/oss-issue-first) <br>
- [RAGFlow PR example](https://github.com/infiniflow/ragflow/pull/16525) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands] <br>
**Output Format:** [Markdown with issue links, release-check guidance, and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to perform public GitHub or GitLab issue searches before recommending fixes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
