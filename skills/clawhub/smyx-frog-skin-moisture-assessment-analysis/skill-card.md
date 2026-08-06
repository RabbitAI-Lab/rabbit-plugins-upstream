## Description: <br>
Analyzes frog skin images or videos from vivariums, rainforest tanks, farms, or veterinary settings to assess visible skin moisture indicators such as glossiness, wrinkles, white film, image quality, and dehydration-risk alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External keepers, amphibian farms, animal hospitals, and developers use this skill to evaluate frog skin moisture from local media or URLs and to retrieve account-linked historical moisture assessment reports. Outputs should be treated as visual assessment support rather than a veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends frog images, videos, or URLs to configured cloud services for analysis. <br>
Mitigation: Use only media that may be processed by the configured service, and review retention and deletion controls before submitting sensitive vivarium, veterinary, or business material. <br>
Risk: The skill can create or reuse a local identity, store account tokens, and retrieve account-linked report history. <br>
Mitigation: Run in a controlled workspace, protect local token storage, and verify account and history access behavior before deployment. <br>
Risk: The skill provides visual moisture assessments that could be mistaken for veterinary diagnosis. <br>
Mitigation: Treat outputs as support information and escalate severe dehydration signs or health concerns to a qualified amphibian veterinarian. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-frog-skin-moisture-assessment-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON-style structured analysis text with optional report links and history tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save analysis output to a user-specified file and may query account-linked cloud report history.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
