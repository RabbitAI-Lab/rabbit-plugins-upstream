## Description:

APIpie AI (apipie.ai). Use this skill for APIpie AI requests that read, create, or update data through the OOMOL-connected connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect APIpie AI connector schemas, create non-streaming chat completions, generate embeddings, and list available model metadata through an authenticated OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions ask users to run unverified remote installer scripts for the oo CLI.

Mitigation: Review the installer source first, prefer a pinned release or verified package-manager install, and avoid running pipe-to-shell commands from an elevated shell.

Risk: Write actions can create APIpie AI chat completions or embeddings using the connected account.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [APIpie AI homepage](https://apipie.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-apipie-ai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
