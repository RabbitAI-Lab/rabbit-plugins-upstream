## Description:

Set up and troubleshoot a secure hybrid OpenClaw Gateway on a VPS with a paired local node, covering Tailscale pairing, exact-request approval, least-privilege remote exec, reconnects, and SSH fallback guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jkfaris94](https://clawhub.ai/user/jkfaris94)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to split OpenClaw across a VPS-hosted Gateway and a trusted local machine, then pair, approve, route, and troubleshoot the node securely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing the Gateway beyond the trusted tailnet could allow unwanted access to the pairing and control surface.

Mitigation: Keep the Gateway bound to loopback, publish it through Tailscale Serve as tailnet-only, and avoid public ports, Tailscale Funnel, plaintext routes, or broad trusted proxy ranges.

Risk: Join links, tokens, or setup codes could be leaked through chat, logs, or shell history.

Mitigation: Use single-use join links, move only the join URL through a private node-local file, restrict file permissions, and avoid relaying credentials through transcripts.

Risk: Remote exec approval could grant broader host access than intended.

Mitigation: Approve only the exact pending request, keep exec on allowlist with ask-on-miss behavior, use named absolute-path binaries, and exclude shells, interpreters with arbitrary code, wildcards, and destructive commands.

Risk: Node upgrades can request expanded capabilities that change the approved attack surface.

Mitigation: Inspect current versus pending capabilities with node describe and approve reapproval requests only when the workflow needs the new surface.

## Reference(s):

- [Upgrade Notes](references/upgrade-notes.md)
- [remote-node-ssh companion skill](https://github.com/jkfaris94/remote-node-ssh)
- [ClawHub skill page](https://clawhub.ai/jkfaris94/skills/hybrid-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Step-by-step checks and troubleshooting tables for OpenClaw Gateway and node setup.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata and README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
