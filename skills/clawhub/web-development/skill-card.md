## Description:

Guides agents implementing, debugging, deploying, and validating Web frontends with React, Vue, Vite, browser checks, and optional CloudBase integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Web developers use this skill to implement and troubleshoot frontend features, integrate CloudBase when needed, and validate build and browser behavior before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copying the authentication examples can allow invalid tokens to be treated as authenticated.

Mitigation: Review authentication code before production use and validate tokens on the server for each protected request.

Risk: The example stores an access token in a browser-written cookie.

Mitigation: Use server-set HttpOnly, Secure, SameSite cookies or a backend session pattern instead.

## Reference(s):

- [ClawHub Web Development skill](https://clawhub.ai/binggg/skills/web-development)
- [Framework guidance](frameworks.md)
- [Browser validation guidance](browser-testing.md)
- [CloudBase integration documentation](https://docs.cloudbase.net/integration/introduce.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific build and browser verification recommended]

## Skill Version(s):

1.27.81 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
