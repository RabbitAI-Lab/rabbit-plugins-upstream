## Description: <br>
Secrets (Zero to One) helps agents coach users through finding and stress-testing a falsifiable startup or product secret: the important, non-consensus truth their business edge depends on. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, founders, product strategists, and startup teams use this skill to test whether an idea is built around a real secret rather than a crowded convention, mystery, or unfalsifiable vision. The skill guides the agent to classify the claim, name why others miss it, design a cheap verification test, and produce an honest verdict. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may discuss proprietary business insights, customer data, or sensitive internal strategy. <br>
Mitigation: Avoid sharing confidential plans, customer data, or sensitive internal strategy unless those details are appropriate to use in the agent session. <br>
Risk: The skill can produce persuasive business-strategy coaching that may be wrong or overconfident if the user's evidence is weak. <br>
Mitigation: Use the skill's falsifiability, kill-condition, and verification gates before relying on its verdict for business decisions. <br>
Risk: The activation phrase 'secret' could be confused with credentials, API keys, passwords, encryption, or secret management. <br>
Mitigation: Route security, privacy, and credential-management requests to an appropriate security skill instead of using this business-opportunity skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/zero-to-one-secrets) <br>
- [deciqAI Zero to One Secrets page](https://www.deciqai.com/c/zero-to-one-secrets) <br>
- [Machine-readable skill metadata](https://www.deciqai.com/s/zero-to-one-secrets.json) <br>
- [deciqAI Knowledge Skills repository](https://github.com/deciqAI/knowledge-skills) <br>
- [Blake Masters, CS183 Startup Class 11 Notes: Secrets](https://blakemasters.com/post/20400301508/cs183class11) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown, Configuration] <br>
**Output Format:** [Markdown with structured coaching prompts and a concise secret-hunt verdict] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask the user to pause and provide a concrete idea, market, or belief before continuing.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
