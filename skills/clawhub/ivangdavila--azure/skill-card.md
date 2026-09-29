## Description:

Azure helps agents architect, debug, secure, operate, and cost-optimize Azure estates across compute, networking, identity, storage, databases, monitoring, infrastructure as code, and migration work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and cloud operators use this skill to deploy and review Azure resources, diagnose cloud failures, reduce spend, harden identity and network exposure, write infrastructure-as-code guidance, and maintain operational runbooks or inventory notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can build a durable plaintext local knowledge base containing Azure inventory, billing history, resource names, tenant or subscription details, and related contact notes.

Mitigation: Use it only on trusted machines and in environments where local persistence under the configured Clawic data folders is acceptable; protect or exclude those folders according to the sensitivity of the tenant.

Risk: Cloud guidance and generated commands can affect production availability, access control, or spend if applied without review.

Mitigation: Review proposed commands and changes before execution, verify the intended subscription, region, price, and blast radius, and require explicit confirmation for destructive operations.

Risk: The skill is marked suspicious by the authoritative security evidence because it stores and reuses detailed cloud estate notes, even though no exfiltration or hidden code was reported.

Mitigation: Review the skill before installation for sensitive tenants, regulated environments, client work, or shared machines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/azure)
- [Clawic skill page](https://clawic.com/skills/azure)
- [Skill definition](artifact/SKILL.md)
- [az toolkit](artifact/commands.md)
- [Cost control](artifact/costs.md)
- [Security guidance](artifact/security.md)
- [Identity and RBAC](artifact/identity.md)
- [Networking and Private Link](artifact/networking.md)
- [Working file templates](artifact/memory-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline Azure CLI commands, infrastructure snippets, configuration tables, and local working-file templates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce durable local notes such as inventory, spend history, saved queries, runbooks, address plans, and deployment records under configured Clawic data paths; credentials are represented by pointers, not secret values.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
