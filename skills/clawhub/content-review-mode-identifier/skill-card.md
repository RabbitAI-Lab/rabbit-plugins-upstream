## Description: <br>
Triage a workspace content item. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wxt-ai](https://clawhub.ai/user/wxt-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operations users use this skill to classify a supplied workspace content note, planning draft, or internal checklist into a concise review mode. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unnecessary sensitive context could be included in the content note during triage. <br>
Mitigation: Provide only the specific content note needed for review, and avoid unrelated private files, credentials, or sensitive material. <br>
Risk: A concise review mode may be too limited for ambiguous content decisions. <br>
Mitigation: Review the returned review_mode against the supplied content note before using it in content operations workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/content-review-mode-identifier) <br>
- [Publisher profile](https://clawhub.ai/user/wxt-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Concise text value for the review_mode field] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the supplied content_note and does not require credentials or private file access.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
