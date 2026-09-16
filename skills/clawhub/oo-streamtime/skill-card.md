## Description:

Streamtime lets agents read, create, and update Streamtime data through the OOMOL oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read, create, and update Streamtime companies, contacts, jobs, organisation details, branches, rate cards, and users through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions execute remote installer scripts directly without verification.

Mitigation: Use a trusted OOMOL CLI distribution path, prefer a signed or package-manager installation method, or download and verify the installer before running it.

Risk: Create and update actions can change Streamtime business data.

Mitigation: Fetch the live action schema, review the exact payload and expected effect, and get user confirmation before running write actions.

## Reference(s):

- [Streamtime homepage](https://www.streamtime.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Streamtime skill page](https://clawhub.ai/oomol/skills/oo-streamtime)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
