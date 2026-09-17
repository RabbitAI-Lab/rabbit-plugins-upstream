## Description:

Higgsfield AI lets agents use the OOMOL `oo` CLI to inspect schemas, submit text-to-image or image-to-video generation requests, check request status, and cancel queued requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to operate Higgsfield AI through an OOMOL-connected account for image and video generation workflows, including request submission, status checks, output retrieval, and queued-request cancellation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes mutable remote installer commands for the `oo` CLI.

Mitigation: Do not let an agent run installer commands automatically; install from a pinned, verified release or inspect and verify downloaded installers before execution.

Risk: Write actions can submit or cancel Higgsfield generation requests.

Mitigation: Confirm the exact payload and intended effect with the user before running actions tagged as write.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-higgsfield-ai)
- [Higgsfield AI homepage](https://higgsfield.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Higgsfield AI icon](https://static.oomol.com/logo/third-party/higgsfield_ai.png)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
