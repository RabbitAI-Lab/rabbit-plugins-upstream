## Description: <br>
Search 1+ million free high-quality AI stock photos and generate AI images through NK Images without an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tompltw](https://clawhub.ai/user/tompltw) <br>

### License/Terms of Use: <br>
NK Images License <br>


## Use Case: <br>
Developers, designers, and content creators use this skill to search NK Images for stock-photo candidates, generate custom images when searches do not match, and present image links returned by the service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, generation prompts, and feedback details are sent to NK Images. <br>
Mitigation: Avoid confidential client data, sensitive personal information, and private prompts unless the user intends to share them with NK Images. <br>
Risk: Image links may be wrong if an agent constructs URLs instead of using response fields. <br>
Mitigation: Use view, download, and thumbnail URLs exactly as returned by the NK Images API, and verify links when correctness matters. <br>
Risk: Feedback submissions may disclose user issue details or optional contact information. <br>
Mitigation: Submit feedback only after user consent and keep descriptions limited to information needed to report the issue. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tompltw/skills/nk-images-search) <br>
- [NK Images](https://nkimages.com) <br>
- [NK Images License](https://nkimages.com/license) <br>
- [NK Images public image search API](https://nkimages.com/api/public/images?source=clawhub&q={search_query}&per_page=10) <br>
- [NK Images generation quota API](https://nkimages.com/api/public/generate/quota) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with API request examples, search summaries, and image view/download links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Image URLs should be copied exactly from NK Images API responses; generation may require polling for completion.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
