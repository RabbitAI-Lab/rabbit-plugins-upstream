## Description: <br>
Agent安全审计免费版 helps AI Agent developers run basic local security self-checks for code repositories, prompt-injection patterns, agent configuration, and tool-call permissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and small teams use this skill before an AI Agent release to run local baseline checks for hardcoded secrets, prompt-injection patterns, agent configuration issues, and tool permission gaps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks an agent to run local grep/find/bash-style checks over target Agent projects, including configuration and .env files, so scan output may expose sensitive filenames, secret-like patterns, or configuration weaknesses. <br>
Mitigation: Run it only on intended local repositories, review results locally, and avoid forwarding scan output to untrusted systems. <br>
Risk: Callback or export use could disclose audit output outside the local environment. <br>
Mitigation: Review and approve any callback_url or export destination before enabling it, and keep destinations trusted. <br>
Risk: Pattern-based checks can produce false positives or miss context-dependent security issues. <br>
Mitigation: Treat results as triage and manually review findings before making release or remediation decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/security-audit-agent-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with bash, Python, and JSON examples; runtime outputs are text or JSON-like scan summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local grep/find/bash-style checks; scan output may include sensitive filenames, secret patterns, or configuration weaknesses.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
