## Description: <br>
Photo Captions Free generates platform-specific captions for Instagram, Flickr, X, Reddit, and VSCO based on a photo's scene, location, mood, and provided camera or film details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creators use this skill to draft differentiated social captions for a single photo across Instagram, Flickr, X, Reddit, and VSCO. It adapts tone, length, hashtags, and camera or film references to each supported platform while avoiding unsupported details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The ClawHub security scan reports that the skill requests broad local read, write, and command execution capabilities that do not fit its caption-writing purpose. <br>
Mitigation: Install only when those local capabilities are acceptable; a safer release should remove read, write, and exec tools and narrow the skill description to caption generation. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain text captions organized by requested platform] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports a five-platform default output and narrower platform subsets; X captions are constrained to 280 characters.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
