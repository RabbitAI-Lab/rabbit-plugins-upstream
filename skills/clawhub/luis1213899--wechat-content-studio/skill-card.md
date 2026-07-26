## Description: <br>
Wechat Content Studio helps agents produce WeChat Official Account articles end to end, including topic checks, writing self-review, confirmed cover generation, gzh-design HTML typesetting and validation, server-aware publishing, and draft verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luis1213899](https://clawhub.ai/user/luis1213899) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, operators, and agents use this skill to write, self-check, typeset, generate covers for, publish, and verify WeChat Official Account article drafts. It is intended for end-to-end article production where writing quality, cover confirmation, HTML validation, publishing preflight, and draft verification must all be handled as one workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can create or verify real WeChat drafts through local publishing scripts. <br>
Mitigation: Confirm publishing intent before running publish steps, run preflight first, and verify returned draft media IDs before treating a publish as successful. <br>
Risk: The workflow can generate cover images through the LuisClaw relay. <br>
Mitigation: Show the generated prompt to the user and generate the cover only after explicit confirmation. <br>
Risk: Local scripts and credentials are required for publishing. <br>
Mitigation: Use only trusted local scripts and credentials, and do not include API keys, AppSecrets, account names, server details, or logs in deliverables. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luis1213899/skills/wechat-content-studio) <br>
- [Workflow reference](references/workflow.md) <br>
- [image2 cover policy](references/image2-policy.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown articles, self-check records, HTML fragments, prompt text, and command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May coordinate local cover generation, HTML validation, preview wrapping, publishing preflight, draft publishing, and draft verification when the user's environment provides the required scripts and credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
