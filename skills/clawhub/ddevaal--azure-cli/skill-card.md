## Description:

Comprehensive Azure Cloud Platform management via command-line interface

This skill is ready for commercial/non-commercial use.

## Publisher:

[ddevaal](https://clawhub.ai/user/ddevaal)

### License/Terms of Use:

MIT

## Use Case:

Developers and cloud engineers use this skill to manage Microsoft Azure resources with Azure CLI commands, automation patterns, and helper shell scripts for VMs, storage, subscriptions, deployments, and resource cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsafe install guidance can encourage running downloaded shell content directly.

Mitigation: Install Azure CLI using verified Microsoft package instructions before following command examples.

Risk: Azure CLI examples can create, modify, or delete cloud resources and may affect costs or availability.

Mitigation: Confirm the active subscription and resource group, and review delete, --yes, --no-wait, and bulk xargs targets before execution.

Risk: Authentication tokens, kubeconfig files, connection strings, and service-principal secrets are sensitive.

Mitigation: Handle credentials as secrets, avoid hardcoding them, and keep them out of shared logs or generated output.

Risk: The included cleanup script's delete mode does not actually remove resources.

Mitigation: Treat cleanup output as an inventory report and verify resource-removal behavior separately before relying on it.

## Reference(s):

- [Azure CLI Complete Command Reference](references/REFERENCE.md)
- [Official Azure CLI Documentation](https://learn.microsoft.com/en-us/cli/azure/)
- [Azure CLI Command Reference](https://learn.microsoft.com/en-us/cli/azure/reference-index)
- [Azure CLI Releases](https://github.com/Azure/azure-cli/releases)
- [Azure Storage Pricing](https://azure.microsoft.com/en-us/pricing/details/storage/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, PowerShell, and Azure CLI command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Azure CLI commands and helper-script usage that require review before execution.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
