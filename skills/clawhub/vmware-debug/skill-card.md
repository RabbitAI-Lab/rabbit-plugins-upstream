## Description:

Helps investigate VMware and vSphere incidents by correlating collected events, ranking possible causes, and recommending next checks without changing VMware systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to investigate VMware, vSphere, ESXi, or NSX incidents, assess evidence and gaps, and plan follow-up checks before handing off any remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local case folders and audit records can retain sensitive hostnames, addresses, log text, and investigation summaries.

Mitigation: Keep case storage on an approved machine, avoid adding passwords, tokens, or .env contents, and delete cases when no longer needed.

Risk: Ranked hypotheses may be mistaken for a confirmed root cause before sufficient evidence is collected.

Mitigation: Check independent evidence and open gaps, distinguish proposed checks from findings, and route fixes through the appropriate approval process.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-debug)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/vmware-skills/VMware-Debug)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON]

**Output Format:** [Markdown diagnosis and next-check guidance; structured JSON timelines and case records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Case evidence and audit records remain on the local machine until deleted.]

## Skill Version(s):

2.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
