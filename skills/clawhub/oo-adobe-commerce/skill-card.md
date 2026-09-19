## Description:

Provides Adobe Commerce product and category read access through the OOMOL adobe_commerce connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve Adobe Commerce product and category data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documentation includes remote installer commands that execute shell scripts.

Mitigation: Review the installer path before installing, prefer a verified signed or package-manager route, and do not let an agent run curl|bash or irm|iex commands automatically.

Risk: The skill depends on connected Adobe Commerce credentials through the OOMOL account.

Mitigation: For normal use, limit execution to the listed read-only product and category actions.

## Reference(s):

- [Adobe Commerce homepage](https://business.adobe.com/products/magento/magento-commerce.html)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces schema-first connector commands and JSON response guidance for read-only Adobe Commerce catalog operations.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
