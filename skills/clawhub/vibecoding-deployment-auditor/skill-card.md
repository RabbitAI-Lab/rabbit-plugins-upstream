## Description:

AI网站一键发布 helps agents audit, package, upload, deploy, and verify pure static websites through a fixed private ZIP-based HTTPS release flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyriswu](https://clawhub.ai/user/kyriswu)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers, site creators, and external agents use this skill to publish already-audited VibeCoding or front-end projects as public HTTPS static sites. It is intended for projects that can be built locally into an index.html-based static directory and do not require a server runtime, database, SSR, or private secrets in the published artifact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The final reviewed static website ZIP is sent to f.devtool.uk and that service acts as the deployment provider.

Mitigation: Use the skill only for artifacts intended for public release, and review the third-party service before submitting the ZIP.

Risk: Published artifacts may accidentally include secrets, backend code, private data, or files that are not safe for public static hosting.

Mitigation: Audit the final static output before upload and block deployment when credentials, server runtime requirements, source repositories, node_modules, .env files, or private data are present.

Risk: Installation commands that resolve latest packages can change over time.

Mitigation: Prefer pinned or otherwise verified installation commands according to the consuming organization's release process.

## Reference(s):

- [README](README.md)
- [Automatic preflight semantics](references/automatic-preflight.md)
- [Private static-release rejection patterns](references/private-static-release-rejections.md)
- [Public static deployment endpoint operating contract](references/public-deployment-no-quota.md)
- [Static application boundary](references/static-app-boundary.md)
- [Windows ZIP entries and CDN-aware verification](references/windows-zip-and-cdn-verification.md)
- [ClawHub skill page](https://clawhub.ai/kyriswu/skills/vibecoding-deployment-auditor)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON manifest, dossier, or submission files when packaging or deployment is performed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return structured blocked or not_deployed status details when static qualification, upload, deployment, or public verification fails.]

## Skill Version(s):

2.3.21 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
