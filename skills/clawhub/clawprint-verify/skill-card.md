## Description: <br>
Issue ClawPrint reverse-CAPTCHA challenges to verify that another user or agent is a real AI, not a human. Uses the ClawPrint API to generate speed or pattern challenges that only machines can solve within the time limit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fusionlabssource](https://clawhub.ai/user/fusionlabssource) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to issue and validate ClawPrint reverse-CAPTCHA challenges before allowing an AI-only workflow or resource access step to continue. It can support verification flows, but the security evidence says a passed challenge should not replace normal identity, policy, or approval checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may encourage treating an AI-check result as sufficient reason to release sensitive resources or credentials. <br>
Mitigation: Use ClawPrint only as one verification signal, and require normal identity, policy, and approval checks before sharing credentials, API keys, private data, or protected resources. <br>
Risk: The skill depends on an external ClawPrint service and local keys. <br>
Mitigation: Install it only when that external service is intended for the workflow, and protect CLAWPRINT_SECRET_KEY and related configuration. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/fusionlabssource/skills/clawprint-verify) <br>
- [ClawPrint API endpoint](https://dependable-adventure-production-44e3.up.railway.app/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with JSON examples and bash command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, CLAWPRINT_SERVER_URL, CLAWPRINT_SITE_KEY, and CLAWPRINT_SECRET_KEY for validation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
