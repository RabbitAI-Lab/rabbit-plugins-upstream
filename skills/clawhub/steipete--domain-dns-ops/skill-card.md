## Description:

Domain/DNS ops across Cloudflare, DNSimple, and Namecheap for Peter, including Cloudflare onboarding, nameserver changes, redirects, redirect-worker mapping updates, and DNS/HTTP verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[steipete](https://clawhub.ai/user/steipete)

### License/Terms of Use:


## Use Case:

Developers and operations maintainers managing Peter's domains use this skill to route DNS work through the manager repository and prepare Cloudflare zone onboarding, nameserver flips, redirects, Worker route mapping updates, and verification steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live DNS, registrar, redirect, Worker route, and bot-protection changes for production domains.

Mitigation: Before applying changes, confirm the exact domain, registrar, target URL, current DNS and mail dependencies, required credentials, and rollback path.

## Reference(s):

- [Manager repo pointers](references/manager-repo.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and operational checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose live DNS, registrar, redirect, Worker route, and bot-protection changes that require operator confirmation before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
