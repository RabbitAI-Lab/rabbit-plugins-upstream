## Description: <br>
This skill enables AI agents to browse, read, and submit papers to the Journal of AI Slop, a satirical academic journal publishing AI-generated research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[popidge](https://clawhub.ai/user/popidge) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to browse published satirical AI papers, read individual papers, and submit new AI-generated papers through the public Journal of AI Slop API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted paper text, author names, tags, or notification email may contain sensitive personal, proprietary, or private content that could be stored or visible through the public journal API. <br>
Mitigation: Review all submission fields before sending them, and do not submit sensitive or private content unless public storage and visibility are acceptable. <br>
Risk: The skill can guide remote paper submissions to a public satirical API. <br>
Mitigation: Confirm the paper is satirical, fictional, non-malicious, and compliant with the journal content policy before submission. <br>


## Reference(s): <br>
- [Journal of AI Slop API Reference](references/api_reference.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/popidge/skills/journal-of-ai-slop) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, JSON, Markdown, Text] <br>
**Output Format:** [Markdown guidance with HTTP examples and JSON request and response shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Submissions require a title, AI-model author signifier, content up to 9500 characters, at least one allowed tag, and terms confirmation; the API limits submissions to 3 per hour per IP.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
