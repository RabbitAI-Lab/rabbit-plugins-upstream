## Description: <br>
Manages client relationships for freelancers, consultants, and agencies across lead qualification, scoping, onboarding, delivery, scope changes, payment follow-up, retention, and offboarding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Freelancers, consultants, and agencies use this skill to manage commercial client relationships from inbound lead through proposal, delivery, payment follow-up, renewal, and offboarding. It helps the agent draft client-facing messages and maintain dated client, contact, project, receivables, revenue, and artifact records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives the agent broad authority to persistently modify and delete sensitive business, financial, contact, and project records. <br>
Mitigation: Keep ~/Clawic/data protected, ask the agent to preview planned file changes before applying them, and review changes to client, contact, project, receivables, revenue, and artifact records. <br>
Risk: Client-management sessions may involve credentials or other secrets during onboarding and access handoff. <br>
Mitigation: Do not store secrets under ~/Clawic/data; keep only pointers to a password manager, keychain, or environment variable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/clients) <br>
- [Clawic skill homepage](https://clawic.com/skills/clients) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Memory template](artifact/memory-template.md) <br>
- [Pipeline guidance](artifact/pipeline.md) <br>
- [Proposal guidance](artifact/proposals.md) <br>
- [Pricing guidance](artifact/pricing.md) <br>
- [Onboarding guidance](artifact/onboarding.md) <br>
- [Delivery guidance](artifact/delivery.md) <br>
- [Payment guidance](artifact/getting-paid.md) <br>
- [Scope guidance](artifact/scope.md) <br>
- [Retention guidance](artifact/retention.md) <br>
- [Offboarding guidance](artifact/offboarding.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, configuration, guidance] <br>
**Output Format:** [Markdown guidance, checklists, tables, local record updates, and draft client-facing messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local client, contact, and project records under ~/Clawic/data when available; durable outputs are recorded as Markdown or YAML-like business records.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
