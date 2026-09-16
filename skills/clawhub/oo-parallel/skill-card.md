## Description:

Parallel lets an agent use Parallel for web search, public URL content extraction, and task-run based web research or structured data enrichment through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search the web, extract content from public URLs, and create or retrieve Parallel task runs for research and structured enrichment. It is intended for users who have the oo CLI installed, are signed in to OOMOL, and have connected Parallel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documentation includes commands that pipe remote installer scripts directly into a shell.

Mitigation: Use an official, verifiable installation path, review installer contents before running them, and avoid piping remote scripts directly into bash or PowerShell.

Risk: The skill operates through OOMOL as an intermediary for Parallel credentials and action execution.

Mitigation: Install only when comfortable with OOMOL handling the Parallel connection server-side, and confirm that the connected OOMOL and Parallel accounts are expected.

Risk: Actions tagged as write, such as create_task_run, can create Parallel state.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-parallel)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Parallel Homepage](https://parallel.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before execution; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
