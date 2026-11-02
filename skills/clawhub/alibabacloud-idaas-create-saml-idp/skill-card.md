## Description:

Create, update, inspect, validate, and troubleshoot a standard inbound SAML 2.0 identity provider in Alibaba Cloud IDaaS EIAM by using Alibaba Cloud CLI. Use when a user wants to connect an external SAML IdP to IDaaS, import or parse IdP metadata from a URL or XML file, configure Entity ID, SSO URL, binding, certificates and Response/Assertion/AuthnRequest signing, obtain IDaaS SP metadata, create or enable the identity source, run the built-in status check, inspect existing IdPs, or diagnose SAML identity-source failures. Also use to read and interpret SAML 2.0 identity-provider metadata for connecting an external IdP to Alibaba Cloud IDaaS EIAM before creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and identity administrators use this skill to connect an external SAML identity provider to Alibaba Cloud IDaaS EIAM. It guides metadata review, configuration planning, verification, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote metadata redirects can trigger requests to private services.

Mitigation: Fix redirect handling or block access to internal services before downloading remote metadata. Use local XML or supplied original SP XML to avoid those download paths.

Risk: Creating an identity provider enables it by default, so incorrect authentication settings can expose a misconfigured identity source.

Mitigation: Use a narrowly scoped Alibaba Cloud profile, review authentication settings carefully, and preserve operation state for safe recovery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-idaas-create-saml-idp)
- [EIAM SAML IdP OpenAPI reference](artifact/references/openapi.md)
- [SAML IdP troubleshooting](artifact/references/troubleshooting.md)
- [RAM permissions](artifact/references/ram-policies.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration instructions]

**Output Format:** [Markdown with CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include metadata assessments, configuration plans, verification results, and troubleshooting guidance.]

## Skill Version(s):

0.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
