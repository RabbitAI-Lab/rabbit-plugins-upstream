## Description:

Cargo Hosting guides agents through creating, deploying, promoting, inspecting, and troubleshooting Cargo-hosted Vite apps, edge workers, and their deployments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn local Cargo app or worker projects into hosted resources, manage deployments, and make successful builds live on cargo.app.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented install path uses @cargo-ai/cli@latest, which can change between reviews.

Mitigation: Pin and review a specific @cargo-ai/cli version before using the skill in a managed environment.

Risk: Deployment upload commands may include local environment files, keys, or other secrets if the source directory or ignore list is wrong.

Mitigation: Exclude .env, .env.*, keys, and other secret-bearing files before running deployment create.

Risk: Create, update, remove, and promote commands act on the active Cargo workspace and may affect public or billable resources.

Mitigation: Run cargo-ai whoami and verify target UUIDs, slugs, and workspace context before write operations.

Risk: deployment promote immediately changes the live URL target.

Mitigation: Promote only deployments whose status is success, then verify the promoted deployment with get-promoted.

Risk: app remove and worker remove delete the resource and all of its deployments with no documented undo.

Mitigation: Require explicit confirmation of the resource UUID and expected deletion outcome before removal.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [ClawHub cargo-hosting skill page](https://clawhub.ai/cargo-ai/skills/cargo-hosting)
- [App examples](references/examples/apps.md)
- [Worker examples](references/examples/workers.md)
- [Deployment examples](references/examples/deployments.md)
- [Hosting response shapes](references/response-shapes.md)
- [Hosting troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON response examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands generally emit JSON; app env outputs .env.local-style configuration.]

## Skill Version(s):

1.0.2 (source: frontmatter, skill-metadata.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
