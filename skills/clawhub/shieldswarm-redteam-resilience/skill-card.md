## Description:

ShieldSwarm is a defensive, authorization-gated SRE/SecOps red-team and purple-team resilience commander that provides mode selection, validation guidance, approval gates, ROE, rollback, postmortem, model-resilience, redaction, and bounded-diagnostic workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT

## Use Case:

Developers, SREs, SecOps operators, and authorized resilience teams use this skill to plan defensive incident-response, red-team, purple-team, model-resilience, approval, rollback, and evidence-handling workflows. It is intended for authorized systems and explicitly excludes offensive testing, login bypass, credential collection, spam, and unapproved production changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may rely on referenced helper scripts that are not present in the published artifact.

Mitigation: Verify or add the referenced validator and approval scripts before relying on enforcement claims; use the shipped self-test and inspect available files before use.

Risk: Approval records, evidence logs, screenshots, HAR files, and diagnostics can contain secrets, private prompts, or sensitive operational data.

Mitigation: Scope file and shell access to the working directory, redact secrets before sharing artifacts, and protect locally written approval or evidence logs.

Risk: Defensive red-team or incident-response workflows can be misused outside authorized scope.

Mitigation: Install and use only for authorized defensive operations with explicit rules of engagement, least privilege, abort conditions, and rollback ownership.

## Reference(s):

- [Skill definition](artifact/SKILL.md)
- [README](artifact/README.md)
- [Agent discovery card](artifact/AGENT_DISCOVERY.md)
- [Changelog](artifact/CHANGELOG.md)
- [Authorization intake template](artifact/templates/authorization_intake.yaml)
- [Red-team rules of engagement template](artifact/templates/red_team_roe.yaml)
- [Model resilience policy template](artifact/templates/model_resilience_policy.yaml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance, Shell commands]

**Output Format:** [Markdown guidance with YAML templates and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed by an authorized human operator; approval, rollback, and evidence logs may contain sensitive operational context and should be protected.]

## Skill Version(s):

2.0.1 (source: artifact/SKILL.md frontmatter, artifact/CHANGELOG.md, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
