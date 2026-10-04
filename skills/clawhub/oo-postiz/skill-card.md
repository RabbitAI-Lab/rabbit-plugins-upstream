## Description:

Postiz (postiz.com). Use this skill for ANY Postiz request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Postiz through an OOMOL-connected account, including listing integrations and posts, importing media from URLs, and creating draft, published, or scheduled social posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path may execute a remote oo CLI installer script directly from the internet.

Mitigation: Review the oo CLI installation step before use and prefer a trusted, verifiable installation method.

Risk: Write actions can create drafts, publish immediately, schedule public posts, or import media into Postiz.

Mitigation: Confirm the exact payload and expected effect with the user before running any Postiz write action.

## Reference(s):

- [Postiz homepage](https://postiz.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Postiz connection settings](https://console.oomol.com/app-connections?provider=postiz)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
