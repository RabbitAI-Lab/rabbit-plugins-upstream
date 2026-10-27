## Description:

Collect what is new in AI in the last 24 hours across X, Hugging Face, GitHub and sitemaps, deduplicated, as one report of names that are starting to surge. Use when the user asks what is new or trending in AI today, wants a daily AI listening report, or needs fresh names of models, products and repositories to feed keyword research. Runs the new-term-radar command line; needs an AISA_API_KEY.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuyansen](https://clawhub.ai/user/zhuyansen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI product teams use this skill to collect emerging model, product, and repository names mentioned during the past 24 hours across X, Hugging Face, GitHub, and configured sitemaps. It produces a daily listening report with sources and signal strength for follow-up keyword research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A scan may incur API charges based on the configured accounts, and local snapshots remain between runs.

Mitigation: Review the configured accounts and sites, approve the estimated API cost before a paid run, and account for persistent local snapshots.

Risk: The pinned third-party Python release has not been independently verified.

Mitigation: Verify the release and its publisher before installation and execution.

## Reference(s):

- [Example source configuration](https://github.com/zhuyansen/new-term-radar/blob/v0.6.0/config.example.json)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Markdown listening report and JSON lead data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports names seen in the last 24 hours, where they appeared, and the strength of each signal.]

## Skill Version(s):

0.6.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
