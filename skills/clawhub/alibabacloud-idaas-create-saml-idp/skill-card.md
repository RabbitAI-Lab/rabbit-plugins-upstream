## Description:

Create, update, inspect, validate, and troubleshoot a standard inbound SAML 2.0 identity provider in Alibaba Cloud IDaaS EIAM by using Alibaba Cloud CLI. Use when a user wants to connect an external SAML IdP to IDaaS, import or parse IdP metadata from a URL or XML file, configure Entity ID, SSO URL, binding, certificates and Response/Assertion/AuthnRequest signing, obtain IDaaS SP metadata, create or enable the identity source, run the built-in status check, inspect existing IdPs, or diagnose SAML identity-source failures. Also use to read and interpret SAML 2.0 identity-provider metadata for connecting an external IdP to Alibaba Cloud IDaaS EIAM before creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and identity administrators use this skill to connect an external SAML identity provider to Alibaba Cloud IDaaS EIAM. It helps them interpret provider metadata, configure and verify the identity source, and troubleshoot federation setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Download safeguards can be bypassed, and existing agent-session identifiers may be sent to Alibaba Cloud without notice.

Mitigation: Ask the publisher to validate redirect destinations and remove existing agent-session identifiers from request metadata or add explicit consent controls. Use a narrowly scoped RAM profile; for a staged rollout, request creation with authentication disabled.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/sdk-team/skills/alibabacloud-idaas-create-saml-idp)
- [EIAM SAML IdP OpenAPI reference](references/openapi.md)
- [SAML IdP troubleshooting](references/troubleshooting.md)
- [RAM permissions](references/ram-policies.md)

## Skill Output:

**Output Type(s):** [Configuration guidance, Shell commands, JSON, XML, Markdown]

**Output Format:** [Markdown guidance and CLI command examples; JSON metadata results and SAML XML when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow can return resolved IdP metadata and the IDaaS service-provider endpoints or complete SP Metadata XML.]

## Skill Version(s):

0.0.1-beta.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
