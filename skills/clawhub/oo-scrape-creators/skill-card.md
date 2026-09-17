## Description:

Scrape Creators (scrapecreators.com). Use this skill for ANY Scrape Creators request - searching and reading data. Whenever a task involves Scrape Creators, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to discover Scrape Creators endpoints, check account credit balance, and invoke documented Scrape Creators GET or POST endpoints through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct remote script execution for installing the OOMOL CLI.

Mitigation: Verify the OOMOL installer source before use and prefer an official, pinned, checksum-verified installation path.

Risk: The activation scope is broad and the skill can call Scrape Creators through OOMOL when selected.

Mitigation: Use it only for requests that intentionally involve Scrape Creators through OOMOL, inspect the live action schema before payload construction, and confirm any write or destructive action with the user.

## Reference(s):

- [Scrape Creators homepage](https://scrapecreators.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-scrape-creators)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector actions; action responses are JSON objects with data and meta.executionId when commands run.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
