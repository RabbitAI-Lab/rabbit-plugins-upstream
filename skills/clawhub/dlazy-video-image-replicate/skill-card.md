## Description:

Replicates a provided reference image or video by studying its look and structure, then recreating it with the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to send explicit image or video reference replication requests to the dLazy CLI-backed service, including prompts and optional reference media. It is intended for recreating the style, structure, or composition of supplied references with user-provided subjects, products, or characters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may cause prompts or attached reference media to be sent to dLazy when the user did not intend to use the hosted service.

Mitigation: Invoke only for explicit image or video reference replication requests, and confirm sensitive attachments before use.

Risk: Reference files and prompts are processed by dLazy services.

Mitigation: Use a fresh project for unrelated work, clear sessions when done, and avoid submitting confidential media unless approved.

Risk: The dLazy API key grants access to the user's organization.

Mitigation: Store it only through the documented CLI auth flow or environment variable, and rotate or revoke it when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to invoke the pinned dLazy CLI skill, attach local reference files, continue project-scoped sessions, or clear session context.]

## Skill Version(s):

1.3.18 (source: ClawHub release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
