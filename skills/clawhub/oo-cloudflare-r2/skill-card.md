## Description:

Cloudflare R2 skill for reading, creating, updating, and deleting R2 data through an OOMOL-connected account instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Cloudflare R2 accounts and buckets, download objects through connector transit storage, and manage bucket settings or CORS policies through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change Cloudflare R2 bucket state.

Mitigation: Confirm the exact action payload and expected effect before approving create, update, or CORS replacement operations.

Risk: Destructive actions can delete buckets or bucket-level CORS policies.

Mitigation: Require explicit approval of the target account, bucket, and destructive operation before execution.

Risk: Payloads may be incorrect if they are built from stale assumptions.

Mitigation: Fetch the live connector schema before constructing each action payload.

## Reference(s):

- [ClawHub Cloudflare R2 skill](https://clawhub.ai/oomol/skills/oo-cloudflare-r2)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Cloudflare R2 homepage](https://www.cloudflare.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use live connector schemas before constructing JSON payloads; connector responses are JSON.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
