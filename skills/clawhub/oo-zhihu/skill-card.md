## Description: <br>
Zhihu (zhihu.com). Use this skill for ANY Zhihu request - searching and reading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search Zhihu content, inspect hot-list results, and run non-streaming Zhihu Zhida chat completions through an OOMOL-connected Zhihu account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries and prompts may be sent through the OOMOL connector to a connected Zhihu account. <br>
Mitigation: Review prompts before sending sensitive queries and install only if OOMOL oo CLI account connection is acceptable for the deployment. <br>
Risk: Future connector actions could add write or destructive behavior. <br>
Mitigation: Require explicit user confirmation for any write or destructive action and confirm the exact payload and effect before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-zhihu) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Zhihu Homepage](https://www.zhihu.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are returned as JSON data with execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
