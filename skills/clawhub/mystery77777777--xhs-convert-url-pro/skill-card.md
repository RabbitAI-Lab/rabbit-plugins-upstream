## Description:

Batch conversion tool for Xiaohongshu note links, including short links, that returns browser-openable URLs containing xsec_token for downstream Xiaohongshu workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to register or log in to a Xiaohongshu conversion service, check paid quota, submit public note URLs in batches, and retrieve converted new_url values for browser access or downstream Xiaohongshu data-collection workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores account tokens in ~/.xhs-platform/config.json and can share credentials with related Xiaohongshu skills.

Mitigation: Protect the config file, avoid committing it, and use XHS_CONFIG_PATH for test isolation or separate accounts.

Risk: The default service URL uses plain HTTP, so tokens and submitted links may traverse the network without transport encryption.

Mitigation: Configure an HTTPS base URL before authenticated use whenever the provider supports it and review the network environment before submitting paid tasks.

Risk: The skill can submit paid conversion tasks against the user's quota.

Mitigation: Check quota first and confirm the URL count before registration, login, or task submission.

Risk: Setting insecure=true disables HTTPS certificate verification for the Node.js process.

Mitigation: Avoid XHS_PLATFORM_INSECURE=1 and only enable insecure TLS handling for trusted test endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mystery77777777/skills/xhs-convert-url-pro)
- [API.md](artifact/API.md)
- [OpenAPI specification](artifact/openapi.yaml)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses on stdout with operational guidance and progress on stderr]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands manage registration, login, quota checks, task submission, polling, logout, and base URL configuration.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and package.json report 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
