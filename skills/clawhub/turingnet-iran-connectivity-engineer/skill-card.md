## Description: <br>
TuringNet Iran Connectivity Engineer provides privacy-first connectivity troubleshooting, outage reporting, authorized telecom resilience guidance, and bilingual support templates for lawful, evidence-based work without bypass guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, help desk teams, and authorized operators use this skill to collect privacy-minimized connectivity evidence, triage device, network, and service reachability issues, draft support or escalation reports, and plan authorized resilience changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release describes redactor, triage, rate limiter, and report scripts that are not present in the artifact files. <br>
Mitigation: Use the included templates and guidance only; do not rely on advertised scripts unless those files are separately provided and reviewed. <br>
Risk: The skill references an external sandbox-selfheal-guard shell integration that was not inspected in this artifact. <br>
Mitigation: Inspect and approve that separate skill before sourcing or running any external self-heal command. <br>
Risk: Connectivity troubleshooting can expose sensitive personal, account, device, subscriber, or location information. <br>
Mitigation: Follow the skill's privacy-minimized intake templates, keep original evidence local, redact identifiers, and use city or province-level location only when volunteered and relevant. <br>
Risk: Connectivity or censorship hypotheses can be overstated without operator-grade evidence. <br>
Mitigation: State only observed facts, avoid unsupported attribution, and escalate through official support or authorized operator workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/turingnet-iran-connectivity-engineer) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>
- [Agent discovery card](artifact/AGENT_DISCOVERY.md) <br>
- [Authorization intake template](artifact/templates/authorization_intake.md) <br>
- [Bilingual evidence intake template](artifact/templates/evidence_intake_bilingual.md) <br>
- [Low-bandwidth playbook](artifact/templates/low_bandwidth_playbook.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with templates and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces privacy-preserving troubleshooting playbooks, intake forms, escalation drafts, continuity checklists, and authorized change review guidance.] <br>

## Skill Version(s): <br>
2.1.2 (source: server release metadata; artifact frontmatter states 2.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
