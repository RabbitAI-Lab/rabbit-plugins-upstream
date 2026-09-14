## Description:

Discover open-source GitHub alternatives from a product idea through bounded, multi-round search, README inspection, evidence verification, and project comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cxxcoolstar](https://clawhub.ai/user/cxxcoolstar)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product evaluators use this skill to turn a product idea into a bounded GitHub discovery process and compare candidate open-source repositories with README-based evidence, capability gaps, license, deployment, and maintenance signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A GitHub token stored in a local .env file may be exposed if the file is committed or shared.

Mitigation: Use a fine-grained read-only GitHub token through the process environment when possible, and add .env to .gitignore before storing a token locally.

Risk: The skill contacts api.github.com and writes a session JSON file, which can capture search terms and inspected repository choices.

Mitigation: Choose an appropriate local state-file path, review the session file before sharing it, and avoid including sensitive product ideas in prompts or state when confidentiality matters.

Risk: GitHub search results and README evidence can change over time, so a report may be incomplete or stale.

Mitigation: Keep the bounded query ledger, include a coverage note, and re-check high-value candidates against README, release, license, and installation evidence before adoption.

## Reference(s):

- [Source repository](https://github.com/cxxCoolStar/github-idea-finder)
- [ClawHub skill page](https://clawhub.ai/cxxcoolstar/skills/github-idea-finder)
- [Publisher profile](https://clawhub.ai/user/cxxcoolstar)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with comparison tables, evidence quotes, decision labels, and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a bounded session JSON file at the path selected by the user.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
