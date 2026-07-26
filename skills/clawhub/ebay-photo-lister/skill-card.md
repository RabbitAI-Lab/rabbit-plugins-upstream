## Description: <br>
Turn a photo and one-line caption into an eBay-validated draft listing with AI-generated title and description, category selection, item specifics, photo upload, and caption-derived price while requiring user approval before anything goes live. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scotty-1987](https://clawhub.ai/user/scotty-1987) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers and reselling operators use this skill to turn item photos and brief captions into reviewed eBay draft listings. The agent prepares job JSON, invokes the external ListBlitz pipeline, relays validation results, and publishes only after explicit user approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill delegates listing generation, photo upload, and credential handling to an external ListBlitz tool that is not bundled with the skill. <br>
Mitigation: Review the external ListBlitz code and setup instructions before installation, and provide eBay or Anthropic credentials only after trusting that pipeline. <br>
Risk: The workflow can publish live eBay listings after draft approval. <br>
Mitigation: Require explicit approval of the exact draft before running live mode, and verify listing title, description, price, category, photos, and item specifics before publishing. <br>
Risk: eBay validation can fail or produce incomplete drafts when required item specifics are missing. <br>
Mitigation: Show validation errors to the user, correct the job JSON, and rerun draft validation before requesting publication approval. <br>


## Reference(s): <br>
- [ListBlitz full kit, docs, and support](https://jenkinsscotty.gumroad.com/l/zmtxiu) <br>
- [ClawHub skill page](https://clawhub.ai/scotty-1987/skills/ebay-photo-lister) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands, job JSON, draft listing details, validation errors, and live listing URLs when approved] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a separately installed ListBlitz workspace plus configured eBay developer and Anthropic credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
