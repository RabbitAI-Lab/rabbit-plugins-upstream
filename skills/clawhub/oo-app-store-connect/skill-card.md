## Description:

App Store Connect helps agents inspect schemas and run OOMOL connector actions for reading, creating, updating, and deleting App Store Connect data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and app operations teams use this skill to manage App Store Connect records through the OOMOL App Store Connect connector, including app metadata, TestFlight, review submissions, pricing, availability, in-app purchases, subscriptions, signing resources, webhooks, and Xcode Cloud workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes executing a remotely fetched installer directly in a shell.

Mitigation: Review the installer path before installing, and prefer installing the oo CLI from official, version-pinned documentation or a verifiable package.

Risk: The skill can perform write and destructive App Store Connect actions that affect app records, testers, pricing, certificates, provisioning profiles, and review submissions.

Mitigation: Inspect the live action schema and confirm the exact JSON payload and affected app or account records before allowing write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-app-store-connect)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [App Store Connect](https://appstoreconnect.apple.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId when commands run successfully.]

## Skill Version(s):

1.0.5 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
