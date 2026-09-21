## Description:

Waterfall (waterfall.io). Use this skill for ANY Waterfall request - reading, creating, and updating data. Whenever a task involves Waterfall, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Waterfall account actions through an OOMOL-connected account, including contact and company enrichment, email verification, job-change checks, and usage reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One-line remote installer commands can execute unreviewed installation scripts.

Mitigation: Review installer commands before use and prefer a verified package or documented installer you trust.

Risk: The skill can interact with a live Waterfall account and launch account-changing enrichment jobs.

Mitigation: Use the skill only when live account interaction is intended, and require confirmation before any job launch or account-changing action.

## Reference(s):

- [Waterfall ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-waterfall)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Waterfall Homepage](https://www.waterfall.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run live Waterfall connector actions through the oo CLI after inspecting the action schema.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
