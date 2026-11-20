## Description:

Converts public Xiaohongshu note URLs into short xhslink.com links, with batch submission and result export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use an AI agent to turn public Xiaohongshu note links into shareable short links, submit batches of up to 50 links, and review or export the results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports collection capabilities beyond the stated short-link purpose and security weaknesses. It fully inspected only 2 of 7 components, so coverage is incomplete.

Mitigation: Install only if you need and trust the reported collection features. Review why environment, network, and shell access are needed, whether the optional TLS bypass is enabled, and how authentication tokens are protected; account for the components the scan did not fully inspect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mystery77777777/skills/xhs-short-url)

## Skill Output:

**Output Type(s):** [JSON, Short URLs, CSV files]

**Output Format:** [JSON command results with optional CSV export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts batches of 1–50 links; each valid link costs one point.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
