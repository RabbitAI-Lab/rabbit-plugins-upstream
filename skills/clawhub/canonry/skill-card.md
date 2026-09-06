## Description:

Canonry helps agents operate the cnry/canonry CLI for Answer Engine Optimization, including project setup, provider connections, sweeps, audits, indexing, traffic sources, and visibility reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing operators, and AEO practitioners use this skill to guide Canonry CLI work for measuring AI answer-engine mentions and citations, connecting search and traffic providers, running audits, and making approved optimization changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Canonry runtime may receive broad local and provider access, including access to project data, provider integrations, and local configuration.

Mitigation: Use pinned and reviewed CLI versions, dedicated least-privilege provider accounts and tokens, and restrict permissions on ~/.canonry.

Risk: Credentials or API keys can be exposed if pasted into chat, passed directly on command lines, or printed from local configuration files.

Mitigation: Use token files or secret managers, avoid command-line secrets, never paste credentials into chat, and avoid printing ~/.canonry/config.yaml.

Risk: Schedules, webhooks, Cloudflare routes, queues, or provider connections may continue operating after a workflow ends.

Mitigation: Explicitly review and clean up schedules, webhooks, Cloudflare routes, queues, and credentials when disconnecting or decommissioning a project.

## Reference(s):

- [Canonry CLI Reference](references/canonry-cli.md)
- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [Server-side traffic (AI Visibility - Server-Side)](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [WordPress Integration](references/wordpress-integration.md)
- [Canonry Website](https://canonry.ai)
- [Canonry Documentation](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)
- [Google Business Profile API Prerequisites](https://developers.google.com/my-business/content/prereqs#request-access)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run Canonry CLI operations; mutation, live-provider read, quota-consuming sweep, scheduling, and credential-touching actions require explicit operator approval.]

## Skill Version(s):

4.180.8+420f30b (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
