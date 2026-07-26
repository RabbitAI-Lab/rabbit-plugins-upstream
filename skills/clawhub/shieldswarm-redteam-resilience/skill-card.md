## Description: <br>
ShieldSwarm is a defensive multi-agent SRE, SecOps, red-team, and purple-team resilience commander for authorized OpenClaw and Arena-like services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, SREs, SecOps teams, and authorized operators use this skill to plan defensive resilience work, incident response, model fallback review, red-team or purple-team exercises, rollback planning, and postmortems with explicit authorization and evidence-handling gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill could be misapplied to attack traffic, bypass testing, credential handling, or unapproved production changes. <br>
Mitigation: Use it only for authorized defensive operations or resilience planning, and confirm scope, approvers, rollback ownership, and data redaction rules before real-system work. <br>
Risk: Operational recommendations could expose sensitive logs, prompts, screenshots, HAR data, customer data, or secrets if evidence is not sanitized. <br>
Mitigation: Require redacted evidence summaries, avoid collecting credentials or raw tokens, and apply the bundled redaction and evidence-handling templates before sharing artifacts. <br>
Risk: Defensive red-team or incident-response plans can still disrupt production if executed without approval gates. <br>
Mitigation: Use rules of engagement, explicit abort conditions, human approval, dry runs, one-change-at-a-time execution, and documented rollback ownership before risky changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/shieldswarm-redteam-resilience) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>
- [Agent discovery card](artifact/AGENT_DISCOVERY.md) <br>
- [Quickstart template](artifact/templates/quickstart.md) <br>
- [Operator authorization template](artifact/templates/operator_authorization.yaml) <br>
- [Red-team rules of engagement template](artifact/templates/red_team_roe.yaml) <br>
- [Model resilience policy template](artifact/templates/model_resilience_policy.yaml) <br>
- [Local self-test harness](artifact/tools/shieldswarm_selftest.py) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands] <br>
**Output Format:** [Markdown guidance with YAML templates, local reports, checklists, diffs, and approval artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for human review before execution and may include redacted evidence summaries, rollback plans, incident updates, and validation logs.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
