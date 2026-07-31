## Description: <br>
Generates differentiated photo captions for Instagram, Flickr, X, Reddit, and VSCO based on the photo scene, mood, and user-provided gear details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Photographers and social media creators use this skill to turn a photo description, location, subject, mood, and optional camera or film details into platform-specific captions. It helps avoid copying the same wording across communities with different tone, tag, and length expectations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad read, write, and command execution capabilities that are not needed for a caption-writing workflow. <br>
Mitigation: Install it only in an agent profile where command execution and file writing are disabled unless you have reviewed and accepted that extra authority. <br>
Risk: Generated captions can become inaccurate when the photo context, location, or gear details are missing or ambiguous. <br>
Mitigation: Review captions before posting and provide concrete scene, location, subject, mood, and equipment details when accuracy matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/photo-captions-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with separate platform-specific caption sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces captions for supported requested platforms; X output is constrained to 280 characters.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
