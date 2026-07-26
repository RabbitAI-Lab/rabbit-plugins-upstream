## Description: <br>
Verify Claims helps an agent check factual claims and potentially misleading content against professional fact-checking services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asgraf](https://clawhub.ai/user/asgraf) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Users ask an agent to verify factual claims in articles, videos, transcripts, news, social posts, or other content. The skill guides the agent to identify checkable claims, search relevant professional fact-checking services, and present a clear synthesis with citations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review found that delayed follow-up checks can retain the user's original claim and context without clear opt-in or retention limits. <br>
Mitigation: Use scheduled follow-ups only after explicit user permission, with a clear explanation of what will be stored, how long it will be retained, and how to cancel or delete it. <br>
Risk: Fact-checking workflows can send sensitive political, medical, legal, personal, or workplace claims to web search and external sites. <br>
Mitigation: Warn users before checking sensitive claims and avoid submitting private or identifying details unless the user explicitly approves that disclosure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/asgraf/skills/verify-claims) <br>
- [List of fact-checking websites](https://en.wikipedia.org/wiki/List_of_fact-checking_websites) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown response with citations, claim-level findings, source summaries, and uncertainty notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend or prepare a follow-up check for very recent content when the host agent supports scheduling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
