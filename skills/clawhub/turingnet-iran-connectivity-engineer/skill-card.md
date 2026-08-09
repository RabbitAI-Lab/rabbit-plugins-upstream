## Description:

Turing-inspired privacy-first IT troubleshooting with intake templates, evidence redaction guidance, low-bandwidth offline mode, a 60-second triage workflow, and lawful evidence-based connectivity diagnostics with no bypass guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External users, help desk staff, and authorized network operators use this skill to collect minimal consented connectivity evidence, redact sensitive data, triage device, network, ISP, DNS, TLS, service, and capacity symptoms, and prepare support or incident documentation without bypassing access controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact documentation references helper scripts that are not present in the inspected files.

Mitigation: Treat script references as workflow examples unless the scripts are separately verified in the installed environment.

Risk: Connectivity evidence can contain credentials, SIM identifiers, precise location, or unredacted logs.

Mitigation: Keep raw evidence local, collect only authorized minimum details, and redact sensitive data before sharing reports or tickets.

Risk: Connectivity troubleshooting can drift into unauthorized testing or bypass guidance.

Mitigation: Use the skill only for lawful, authorized troubleshooting and follow its stated boundaries against bypass, scanning, flooding, and third-party interference.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/orionshaowswmw/skills/turingnet-iran-connectivity-engineer)
- [README](artifact/README.md)
- [Agent discovery card](artifact/AGENT_DISCOVERY.md)
- [Bilingual evidence intake template](artifact/templates/evidence_intake_bilingual.md)
- [Authorization and scope intake template](artifact/templates/authorization_intake.md)
- [Low-bandwidth playbook](artifact/templates/low_bandwidth_playbook.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with checklists, templates, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emphasizes local evidence handling, redaction, authorization checks, and low-bandwidth reporting workflows.]

## Skill Version(s):

2.1.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
