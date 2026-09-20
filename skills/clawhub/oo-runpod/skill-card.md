## Description:

Operates Runpod through an OOMOL-connected account for reading pod details and managing pod lifecycle actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Runpod action schemas and list, retrieve, start, restart, reset, stop, or delete pods through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can stop, reset, restart, start, or delete Runpod pods.

Mitigation: Confirm the exact pod ID, payload, and expected effect with the user before running write or destructive actions.

Risk: The first-time setup path includes remote installer commands.

Mitigation: Prefer a verified or pinned installer path before running downloaded scripts.

Risk: The skill operates through an OOMOL-connected Runpod account.

Mitigation: Install only if the user trusts OOMOL and is comfortable connecting their Runpod account through it.

## Reference(s):

- [ClawHub Runpod skill page](https://clawhub.ai/oomol/skills/oo-runpod)
- [Runpod homepage](https://www.runpod.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runpod connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.4 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
