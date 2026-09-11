## Description:

Set up, administer, build, design, and publish with Webstudio self-hosted or Cloud environments, including installation, Builder UI workflows, Webstudio-native build objects in Postgres, styling, assets, publishing, domains, and advanced CMS features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cbertucci33](https://clawhub.ai/user/cbertucci33)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate Webstudio projects, especially self-hosted deployments, by building pages, modifying Webstudio build objects, managing assets, publishing sites, and verifying results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents broad Webstudio administrative operations that can expose, overwrite, or publish site data if followed carelessly.

Mitigation: Use it only in an isolated self-hosted Webstudio environment you administer, require backups, and verify one-row database updates before applying changes.

Risk: The artifact describes broad anonymous PostgREST access and postgres superuser workflows.

Mitigation: Revoke broad anonymous PostgREST access, avoid postgres superuser workflows, and use least-privilege credentials and tokens.

Risk: Following unpinned CLI package or container image examples can make behavior change over time.

Mitigation: Pin CLI packages and container images before using the guidance on real projects.

Risk: Authentication secrets may be needed for browser automation and could be exposed if read or printed unnecessarily.

Mitigation: Do not let an agent read or print AUTH_SECRET unless explicit credential use has been approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cbertucci33/skills/webstudio-cms)
- [Webstudio API Surface](artifact/api.md)
- [Webstudio Database & Stack](artifact/database.md)
- [Webstudio Build Objects](artifact/build-objects.md)
- [Webstudio Publishing, Domains & Auth](artifact/publishing.md)
- [Webstudio Verification](artifact/verification.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell, SQL, JavaScript, JSON, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pure markdown skill content; no executable code is bundled in the artifact.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
