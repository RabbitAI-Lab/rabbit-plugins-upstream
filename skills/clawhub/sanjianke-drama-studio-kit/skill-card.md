## Description:

Guides technical teams through selection, private deployment, cost estimation, operations, and compliance checks for an AI short-drama creation platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

Developers and technical leads use this skill to decide whether to self-host an AI short-drama studio, compare self-build, private deployment, and SaaS paths, estimate storage and generation costs, and follow deployment and operations checklists. It provides guidance, markdown references, shell-command examples, and a local Python cost calculator; it does not generate scripts, images, audio, or videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server-side security evidence flags the release as suspicious because the docs direct users toward third-party API-key and recharge channels while claiming a no-key-handling offline boundary.

Mitigation: Review before installing; use independently vetted vendor accounts, least-privilege keys, spend limits, key rotation, and procurement or security review before connecting production workflows or paid model services.

Risk: The artifact includes contact-based API-key acquisition guidance, which can increase credential, billing, and trust risk.

Mitigation: Do not obtain, share, or troubleshoot API keys through chat contacts; provision credentials through approved account owners and store them in environment variables or managed secrets.

Risk: The cost calculator uses placeholder pricing and excludes retries, failed reruns, and manual rework.

Mitigation: Replace all unit prices with current vendor pricing, set retry and daily usage limits, and treat estimates as order-of-magnitude planning rather than a budget guarantee.

Risk: Deployment guidance discusses AGPL-licensed upstream software and AI-generated media compliance, which may create obligations for public services.

Mitigation: Have legal or compliance reviewers confirm license duties, generated-content labeling, filing, and source-attribution requirements before external launch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-drama-studio-kit)
- [Selection Scorecard](references/selection-scorecard.md)
- [Deploy and Configure](references/deploy-and-configure.md)
- [Operations and Compliance](references/ops-and-compliance.md)
- [Cost Estimate Script](scripts/cost_estimate.py)
- [Referenced upstream project](https://gitee.com/forproject/zhenling-drama)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and a Python cost-estimation script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline documentation and local standard-library Python script; cost defaults are examples and should be replaced before relying on estimates.]

## Skill Version(s):

1.0.2 (source: evidence.release.version; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
