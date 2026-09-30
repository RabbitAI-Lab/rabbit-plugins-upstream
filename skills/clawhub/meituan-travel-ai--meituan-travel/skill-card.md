## Description:

Meituan Travel helps users query and plan travel services such as hotels, flights, trains, attraction tickets, deals, prices, and itineraries using Meituan travel data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[meituan-travel-ai](https://clawhub.ai/user/meituan-travel-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill as a travel assistant for China-focused trip planning and booking discovery across hotels, flights, trains, attractions, prices, deals, and itinerary ideas. The skill authenticates with Meituan Passport before calling the Meituan travel CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive Meituan authentication tokens.

Mitigation: Use only in a trusted runtime, avoid exposing tokens in prompts or logs, and confirm that users understand when Meituan authorization is being used.

Risk: The skill uses unpinned external npm tooling and automatic installs.

Mitigation: Pin package versions, review package provenance before deployment, and disable or constrain automatic global installs in managed environments.

Risk: Endpoint overrides and token injection can expand the effect of a compromised or misconfigured runtime.

Mitigation: Restrict endpoint override capability, run with least privilege, and review authentication flows before broad deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/meituan-travel-ai/skills/meituan-travel)
- [Meituan developer homepage](https://developer.meituan.com)
- [Passport user auth reference](artifact/meituan-passport-user-auth/reference.md)
- [OpenClaw runtime metadata](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown travel results with links, images when available, and concise status or error text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npx and Meituan authentication context; travel results should preserve CLI-provided prices, links, images, and wording.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
