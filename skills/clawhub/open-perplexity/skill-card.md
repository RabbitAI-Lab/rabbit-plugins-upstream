## Description:

Opens Brave browser to Perplexity AI. Access the AI-powered search engine that combines chat with real-time web search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users use this browser skill to open Perplexity AI in Brave for AI-assisted web search, citation-backed answers, and research tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad trigger phrase "open ai search" may overlap with other AI-search skills.

Mitigation: Review or remove that trigger phrase when installing multiple AI-search browser skills.

Risk: The Windows launch path uses shell=True.

Mitigation: Consider changing the Windows opener to avoid shell=True as a hardening improvement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruchir17-cmd/skills/open-perplexity)
- [Perplexity AI](https://www.perplexity.ai/)
- [Brave Browser](https://brave.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Text with shell-command behavior and YAML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Opens Perplexity AI in Brave; requires Brave browser and an internet connection.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
