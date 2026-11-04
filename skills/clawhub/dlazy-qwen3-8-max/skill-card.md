## Description:

Routes text prompts and optional images to Alibaba's Qwen reasoning model through dLazy for complex reasoning, code engineering, and long-context analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to submit text prompts and optional images to Qwen through dLazy and receive generated responses for reasoning, coding, and long-context tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy cloud services, and image files may be uploaded to its media storage.

Mitigation: Submit only prompts and images approved for that service; use the dry-run option to review payload and estimated cost before a request.

Risk: Login saves a reusable organization API key locally, and requests can consume credits.

Mitigation: Protect the saved key, rotate or revoke it if exposed, and monitor available credits before submitting requests.

Risk: The external CLI implementation and its credential-permission claims remain unverified.

Mitigation: Review the CLI package before installation and avoid relying on its local credential protections until verified.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Code, JSON]

**Output Format:** [Generated response in a JSON API envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronously when requested; generated response content depends on the prompt.]

## Skill Version(s):

1.2.33 (source: server-resolved release metadata; artifact frontmatter and CLI install pin list 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
