## Description: <br>
深知晓 helps agents answer and research Chinese public-service, policy, tax, benefits, standards, permitting, subsidy, compliance, and business-policy questions with source-linked responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dknownai](https://clawhub.ai/user/dknownai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill to obtain grounded Chinese public-service guidance, trusted source retrieval, policy comparison, subsidy and tax analysis, compliance checks, and research or drafting support. It is intended for questions where the agent should preserve traceability to returned reports or knowledge-base links. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: User questions and context are sent to dknowc.cn remote services, and may include public-service, policy, tax, benefit, or business-policy details. <br>
Mitigation: Use the skill only with information appropriate for that service and avoid submitting sensitive personal or business data unless approved. <br>
Risk: The skill stores a remote-service API key in a local config.ini and can copy a same-family key after user confirmation. <br>
Mitigation: Keep config.ini local, require explicit user confirmation before key reuse, and never print, share, or package API keys. <br>
Risk: Policy, tax, benefit, and compliance guidance can affect consequential decisions. <br>
Mitigation: Review returned trace reports or knowledge-base links and confirm high-impact conclusions with authoritative agencies or qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknowc-know) <br>
- [Dknowc platform](https://platform.dknowc.cn) <br>
- [Dknowc open API](https://open.dknowc.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Human-readable text or Markdown with source links; JSON is available for script-level integration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include trusted trace-report links or knowledge-base links. Initial setup can create a local config.ini containing the service API key.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release evidence and CHANGE_log.md, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
