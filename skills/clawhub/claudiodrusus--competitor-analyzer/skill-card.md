## Description:

Generate a detailed competitive analysis report for a company, including overview, pricing, social presence, recent news, and SWOT-lite insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[claudiodrusus](https://clawhub.ai/user/claudiodrusus)

### License/Terms of Use:


## Use Case:

Developers, analysts, and business teams use this skill to generate a quick competitive intelligence report from a company name or URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A crafted company name or URL may execute local Python code through the script's input handling.

Mitigation: Review or patch query encoding before use; pass only trusted company names or URLs and run in a restricted workspace.

Risk: The skill contacts DuckDuckGo and leaves a markdown report in the current directory.

Mitigation: Run it only where outbound web access and local report creation are acceptable, and review the report before sharing it.

## Reference(s):


## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance]

**Output Format:** [Markdown report with shell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a competitor-report markdown file in the current directory and prints the report to standard output.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
